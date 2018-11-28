#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <stdlib.h>

using namespace std;

struct Case
{
	vector<int> vec;
	int K, result;
	int &cell(int r, int c)
	{
		return vec.at(r * K + c);
	}
	int &scell(int r, int c)
	{
		//cout << "Access " << r << " " << c << " = " << (r * (K+1) - c * (K-1) + K*K-1)/2 << ":" << vec[(r * (K+1) - c * (K-1) + K*K-1)/2] << endl;
		return vec.at((r * (K+1) - c * (K-1) + K*K-1)/2);

	}
	bool isVerticalElegant(int r)
	{
		//cout << "Row elegance: " << r << endl;
		for(int i = 0; i < K-abs(r); ++i)
		{
			//cout << "\tColumn offset: " << i << endl;
			for(int j = (r+i+K)%2+1; j < K - abs(r) - i; j += 2)
			{
				//cout << "\t\tComparing (" << r+j << "," << i << ")=" << scell(r+j, i) <<
				//		" with (" << r-j << "," << i << ")=" << scell(r-j, i) << endl;
				//cout << "\t\tComparing (" << r+j << "," << -i << ")=" << scell(r+j, -i) <<
				//		" with (" << r-j << "," << -i << ")=" << scell(r-j, -i) << endl;
				if(scell(r+j, i) != scell(r-j, i)
						|| scell(r+j, -i) != scell(r-j, -i))
					return false;
			}
		}
		return true;
	}
	bool isHorizontalElegant(int c)
	{
		//cout << "Column elegance: " << c << endl;
		for(int i = 0; i < K-abs(c); ++i)
		{
			//cout << "\tRow offset: " << i << " " << (i+K)%2+1 << " " << K - abs(c) << endl;
			for(int j = (c+i+K)%2+1; j < K - abs(c) - i; j += 2)
			{
				//cout << "\t\tComparing (" << i << "," << c+j << ")=" << scell(i, c+j) <<
				//		" with (" << i << "," << c-j << ")=" << scell(i, c-j) << endl;
				//cout << "\t\tComparing (" << -i << "," << c+j << ")=" << scell(-i, c+j) <<
				//		" with (" << -i  << "," << c-j << ")=" << scell(-i, c-j) << endl;
				if(scell(i, c+j) != scell(i, c-j)
						|| scell(-i, c+j) != scell(-i, c-j))
					return false;
			}
		}
		return true;
	}

	Case(int K)
		: K(K), vec(K*K, 0)
	{
		for(int r = -K+1; r < K; ++r)
			for(int c = -(K-1-abs(r)); c <= (K-1)-abs(r); c += 2)
				cin >> scell(r, c);

		unsigned v_nearest = 0;
		if(!isVerticalElegant(v_nearest))
			while(++v_nearest < K
					&& !isVerticalElegant(v_nearest)
					&& !isVerticalElegant(-v_nearest));
		//cout << "Nearest row " << v_nearest << endl;


		unsigned h_nearest = 0;
		if(!isHorizontalElegant(h_nearest))
			while(++h_nearest < K
					&& !isHorizontalElegant(h_nearest)
					&& !isHorizontalElegant(-h_nearest));
		//cout << "Nearest col " << h_nearest << endl;

		int nearest = v_nearest + h_nearest;
		//cout << "Nearest " << nearest << endl;
		result = (K + nearest) * (K + nearest) - K * K;
	}
};

int main(int argc, char *argv[])
{
	int cases;
	cin >> cases;
	vector<pair<int, int> > biggests;

	for(int ci = 0; ci < cases; ++ci)
	{
		int K;
		cin >> K;
		Case c(K);
		cout << "Case #" << ci + 1 << ": " << c.result << endl;
	}

	return 0;
}
