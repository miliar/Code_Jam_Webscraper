#define _USE_MATH_DEFINES 1
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
#include <iterator>
#include <cassert>
#include <cmath>

using namespace std;

template<typename X> class sequence_lister;		// Forward reference

template<typename InIter>
inline ostream& operator<<(ostream& os, sequence_lister<InIter> const& sl) {
//	copy(sl._first, sl._last, ostream_iterator<typename InIter::value_type>(os, sl._delim));
	for (InIter i = sl._first; i != sl._last; ++i) {
		if (i != sl._first) {
			os << sl._delim;
		}
		
		os << *i;
	}
	
	return os;
}

template<typename InIter>
class sequence_lister {
public:
	sequence_lister(InIter first, InIter last, char* delim = "") :
		_first(first),
		_last(last),
		_delim(delim)
	{}
	
	// Also allow construction from any container supporting begin() and end()
	template<typename Cont>
	sequence_lister(Cont& cont, char* delim = "") :
		_first(cont.begin()),
		_last(cont.end()),
		_delim(delim)
	{}
	
	sequence_lister(sequence_lister const& x) :
		_first(x._first),
		_last(x._last),
		_delim(x._delim)
	{}
	
	sequence_lister& operator=(sequence_lister const& x) {
		_first = x._first;
		_last = x._last;
		_delim = x._delim;
	}
	
	friend ostream& operator<< <>(ostream& os, sequence_lister<InIter> const& sl);
	
private:
	InIter _first, _last;
	char* _delim;
};

template<typename InIter>
inline sequence_lister<InIter> list_sequence(InIter first, InIter last, char* delim = "") {
	return sequence_lister<InIter>(first, last, delim);
}

template<typename Cont>
inline sequence_lister<typename Cont::const_iterator> list_sequence(Cont& cont, char* delim = "") {
	return sequence_lister<typename Cont::const_iterator>(cont, delim);
}

int timeToMinute(string s) {
	assert(s.size() == 5);
	assert(s[2] == ':');
	
	return ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + s[4] - '0';
}

template <typename T>
T sq(T x) {
	return x * x;
}

//HACK
bool isApproxEqual(double a, double b, double prec = 1e-15) {
	if (a == 0) {
		return abs(b) < prec;
	} else {
		return b / a < (1 + prec) && b / a > (1 - prec);
	}
}

// Calculate the area under a chord by subtracting an isosceles triangle from
// a pie slice.
double areaUnderChord(double x1, double y1, double x2, double y2, double r) {
//	double x = (x1 + x2) / 2;
//	double y = (y1 + y2) / 2;
	
//	cerr << "areaUnderChord((" << x1 << ", " << y1 << "), (" << x2 << ", " << y2 << "), r=" << r << ") called.\n";
	assert(x1 <= x2);
	assert(y1 >= y2);
	
	assert(isApproxEqual(sq(x1) + sq(y1), sq(r)));
	assert(isApproxEqual(sq(x2) + sq(y2), sq(r)));
	
	double d = sqrt(sq(x2 - x1) + sq(y2 - y1)) / 2;
//cerr << "d = <" << d << ">\n";		//DEBUG
	double ang = 2 * asin(d / r);		// Angle of pie slice in radians
	assert(ang > 0);
//cerr << "ang = <" << ang << "> (" << (ang * 180 / M_PI) << " degrees)\n";		//DEBUG
	double triArea = cos(ang / 2) * r * d;		// Alternatively could calculate the midpoint of (x1, y1) and (x2, y2) and calculate the triangle edge length from that.
	double pieSliceArea = sq(r) * ang / 2;
//cerr << "triArea = <" << triArea << ">\n";		//DEBUG
//cerr << "pieSliceArea = <" << pieSliceArea << ">\n";		//DEBUG
	if (triArea > pieSliceArea) {
cerr << "triArea = <" << triArea << ">\n";		//DEBUG
cerr << "pieSliceArea = <" << pieSliceArea << ">\n";		//DEBUG
cerr << "(triArea - pieSliceArea) = <" << (triArea - pieSliceArea) << ">\n";		//DEBUG
		return 0.0;
	}
//	assert(triArea <= pieSliceArea);
	return pieSliceArea - triArea;
//	return 0.0;			//DEBUG
}

double solve(double f, double R, double t, double r, double g) {
	double safeArea = 0.0;
	double totalArea = sq(R) * M_PI;
	double rim = sq(R - t - f);
	
	if (f * 2 >= g) {
		// There are no gaps smaller than the fly.
		return 1.0;
	}
	
	for (int row = 0; ; ++row) {
		double bot = row * (2 * r + g) + r + f;
		double top = bot + g - 2 * f;
		
		// For speed, first quickly calculate how many full squares are on this
		// row.
		int col = 0;
		if (rim > sq(top)) {
			double x_cut = sqrt(rim - sq(top));
//	cerr << "top = <" << top << ">\n";		//DEBUG
//	cerr << "x_cut = <" << x_cut << ">\n";		//DEBUG
	
			col = (x_cut - r - f) / (2 * r + g);		// Rounds down, doesn't matter if imprecision causes it to be 1 too few.
		}
//cerr << "col = <" << col << ">\n";		//DEBUG

		safeArea += (top - bot) * (g - 2 * f) * col;
		
//		for (int col = 0; ; ++col) {
		for (; ; ++col) {
			double left = col * (2 * r + g) + r + f;
			
//			cerr << "(row, col) = (" << row << ", " << col << "), (bot, left) = (" << bot << ", " << left << ").\n";
			
			if (sq(bot) + sq(left) >= rim) {
				// The lower-left corner is outside the circle: no gap here.
				if (col == 0) {
					goto end_of_outer_loop;		// Ooh!  Isn't this bad?  Ooh!
				} else {
					break;
				}
			}
			
			// If we get to here then there is some safe area with (bot, left)
			// as its lower-left corner.  Of the three remaining corners, we
			// have five possibilities: 
			// 1. None are cut off (a full square);
			// 2. Only the top-right corner is cut off;
			// 3. Both top corners are cut off;
			// 4. Both right corners are cut off;
			// 5. All three corners are cut off.
			
			double right = left + g - 2 * f;
			if (sq(top) + sq(right) <= rim) {
				// 1. A full square.
				safeArea += (top - bot) * (right - left);
			} else if (sq(top) + sq(left) <= rim) {
				double p1_x = sqrt(rim - sq(top));		// Intersection of horiz line at top with rim
				
				if (sq(bot) + sq(right) <= rim) {
					// 2. Only the top-right corner is cut off.
					double p2_y = sqrt(rim - sq(right));	// Intersection of vert line at right with rim
					safeArea += areaUnderChord(p1_x, top, right, p2_y, R - t - f);
					safeArea += (p1_x - left) * (top - bot) + (right - p1_x) * (p2_y - bot) + (right - p1_x) * (top - p2_y) / 2;
				} else {
					// 4. Both right corners are cut off.
					double p2_x = sqrt(rim - sq(bot));		// Intersection of horiz line at bottom with rim
					safeArea += areaUnderChord(p1_x, top, p2_x, bot, R - t - f);
					safeArea += (p1_x - left) * (top - bot) + (p2_x - p1_x) * (top - bot) / 2;
				}
			} else {
				double p1_y = sqrt(rim - sq(left));		// Intersection of vert line at left with rim
				
				if (sq(bot) + sq(right) <= rim) {
					// 3. Both top corners are cut off.
					double p2_y = sqrt(rim - sq(right));	// Intersection of vert line at right with rim
					safeArea += areaUnderChord(left, p1_y, right, p2_y, R - t - f);
					safeArea += (right - left) * (p2_y - bot) + (right - left) * (p1_y - p2_y) / 2;
				} else {
					// 5. All three corners are cut off.
					double p2_x = sqrt(rim - sq(bot));		// Intersection of horiz line at bottom with rim
					safeArea += areaUnderChord(left, p1_y, p2_x, bot, R - t - f);
					safeArea += (p2_x - left) * (p1_y - bot) / 2;
				}
			}
		}
	}
	
end_of_outer_loop:
	return 1.0 - ((safeArea * 4) / totalArea);
}

int main(int argc, char **argv) {
	int nCases;
	{ string s; getline(cin, s); istringstream iss(s); iss >> nCases; }
	
	for (int iCase = 0; iCase < nCases; ++iCase) {
		double f, R, t, r, g;
		{ string s; getline(cin, s); istringstream iss(s); iss >> f >> R >> t >> r >> g; }
		double result = solve(f, R, t, r, g);
		
		cout << "Case #" << (iCase + 1) << ": " << result << endl;
	}
	
	return 0;
}
