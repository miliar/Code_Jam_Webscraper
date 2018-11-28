#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <numeric>
using namespace std;


struct rectangle {
	int x1,y1,x2,y2;
	rectangle() : x1(0),y1(0),x2(0),y2(0) {}
	rectangle(const int& x1,const int& y1,const int& x2,const int& y2) : x1(x1),y1(y1),x2(x2),y2(y2) {}
	void apply(const int& xmax,const int& ymax, int* tab) const
	{
		for (int y = y1-1; y < y2; ++y)
		{
			for (int x = x1-1; x < x2; ++x)
			{
				tab[y*xmax+x] = 1;
			}
		}
	}
};

istream& operator >>(istream& is, rectangle& r)
{
	is >> r.x1;
	is >> r.y1;
	is >> r.x2;
	is >> r.y2;
	return is;
}

void evolve(int * tab, const int& xmax, const int& ymax)
{
	for (int y = ymax-1 ; y >= 0; --y)
	{
		for (int x = xmax-1 ; x >= 0; --x)
		{
			if (y > 0)
				tab[y*xmax+x] += tab[(y-1)*xmax+x];
			if (x > 0)
				tab[y*xmax+x] += tab[y*xmax+x-1];
		}
	}
	for (int y = 0 ; y < ymax; ++y)
	{
		for (int x = 0 ; x < xmax; ++x)
		{
			tab[y*xmax+x] >>= 1;
		}
	}
}

void print (int * tab, const int& xmax, const int& ymax)
{
	for (int y = 0 ; y < ymax; ++y)
	{
		for (int x = 0 ; x < xmax; ++x)
		{
			cout << tab[y*xmax+x] << " ";
		}
		cout << endl;
	}
}

int main (int argc, char * argv[])
{
	ifstream file(argv[1]);
	int C = 0;
	file >> C;
	for (int i = 0 ; i < C; ++i)
	{
		int R = 0;
		file >> R;
		vector<rectangle> rectangles;
		rectangles.reserve(R);
		int xmax = 0, ymax = 0;
		for (int l = 0 ; l < R; ++l)
		{
			rectangle r;
			file >> r;
			rectangles.push_back(r);
			xmax = max<int>(xmax, r.x2);
			ymax = max<int>(ymax, r.y2);
		}
		xmax*=2;
		ymax*=2;
		int *tab = new int[xmax*ymax];
		int* tabend = tab+xmax*ymax;
		fill(tab, tabend, 0);
		for (vector<rectangle>::const_iterator it = rectangles.begin(), itend = rectangles.end(); it != itend; ++it)
		{
			it->apply(xmax,ymax, tab);
		}
		int seconds = 0;
		for (seconds = 0; accumulate(tab, tabend, 0) > 0; ++seconds)
		{
			//cout << "Sum: " << accumulate(tab, tabend, 0) << "\tSeconds: " << seconds << endl;
			//print(tab, xmax, ymax);
			evolve(tab, xmax, ymax);
		}
			//cout << "Sum: " << accumulate(tab, tabend, 0) << "\tSeconds: " << seconds << endl;
			//print(tab, xmax, ymax);
		cout << "Case #" << (i + 1) << ": " << seconds << endl;
	}
	file.close();
}
