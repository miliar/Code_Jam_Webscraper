#include<string>
#include<cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

void print(vector<vector<int> > & source)
{
	return;
	int mid = source.size()/2;
	int spaces = mid + 1;
	bool back = false;
	for(int i=0;i<source.size();i++)
	{
		if(i==mid)
		{
			back = true;
			spaces--;
		}
		else
		{
			if(back)
			{
				spaces++;
			}
			else
			{
				spaces--;
			}
			if(spaces>0)
			{
				cerr << string(spaces,' ');
			}
		}

		for(int j=0;j<source[i].size();j++)
		{
			if(source[i][j]==-1)
			{
				cerr << "X" << " ";
			}
			else
			{
				cerr << source[i][j] << " ";
			}
		}
		cerr << endl;
	}

}

void readin(int size, vector<vector<int> > & source)
{
	for(int i=1;i<=size;i++)
	{
		for(int j=0;j<i;j++)
		{
			int temp;
			cin >> temp;
			source[i-1].push_back(temp);
		}
	}
	int index = size;
	for(int i=size-1;i>=0;i--)
	{
		for(int j=0;j<i;j++)
		{
			int temp;
			cin >> temp;
			source[index].push_back(temp);
		}
		index++;
	}
//	cerr << "Start read: " << endl;
//	print(source);
//	cerr << "End read: " << endl;

}

bool comp(vector<int> & x, vector<int> & y)
{
	if(x.size() != y.size())
	{
		return false;
	}
	for(int i=0;i<x.size();i++)
	{
		if(x[i] == y[i])
		{
			continue;
		}
		if((x[i] == -1) || (y[i] == -1))
		{
			continue;
		}
		return false;
	}
	return true;
}

bool check(vector<vector<int> > & source)
{
	for(int i=0;i<source.size();i++)
	{
		vector<int> temp(source[i].rbegin(),source[i].rend());
		if(!comp(temp,source[i]))
		{
			return false;
		}
	}
	return true;
}

void rotate(vector<vector<int> > & old)
{
	vector<vector<int> > source(old);
	int row = 0;
	int count = 0;
	int at = (old.size()/2) + 1;
	int mid = at;
	bool back = false;
	for(int i=0;i<old.size();i++)
	{
		old[i].clear();
	}
	for(int i=0;i<source.size();i++)
	{
		for(int j=0;j<source[i].size();j++)
		{
//			cerr << "Inserting: " << source[i][j] << endl;
//			cerr << "At: row: " << row << " count: " << count << " at: " << at-1 << " mid: " << mid << endl;
			if(row == count)
			{
//				cerr << "End row" << endl;
				row++;
				old[at-1].push_back(source[i][j]);

				if(row>=mid)
				{
					if(!back)
					{
//						cerr << "Midpoint: " << endl;
						back = true;
					}
					at = (2*mid) - (row-mid) - 2;
					count = row - mid + 1;
					count *=2;
				}
				else
				{
					at = mid + row;
					count = 0;
				}
			}
			else
			{
				old[at-1].push_back(source[i][j]);
				at-=2;
				count++;
			}
		}
	}
}

int append(vector<vector<int> > & diamond)
{
	int retval = diamond.size() + 2;
	diamond.insert(diamond.begin(),vector<int>(1,-1));
	for(int i=1;i<diamond.size();i++)
	{
		diamond[i].push_back(-1);
	}
	diamond.push_back(vector<int>(1,-1));
	return retval;
}

int main()
{
	int num;
	cin >> num;
	for(int x=1;x<=num;x++)
	{
		int k;
		cin >> k;
		vector<vector<int> > diamond(2*k-1,vector<int>());
		readin(k, diamond);

//		print(diamond);
//		cerr << endl;

		vector<vector<int> > orig(diamond);

		int retval = 0;
//		while(1)
		{
			while(!check(diamond))
			{
				retval += append(diamond);
//				cerr << "Failed, new retval: " << retval << endl;
			}

			rotate(diamond);
			while(!check(diamond))
			{
				retval += append(diamond);
//				cerr << "Failed (Rotate), new retval: " << retval << endl;
			}
//			break;
		}

		int temp = 0;
		diamond = orig;
		{
			while(!check(diamond))
			{
				temp += append(diamond);
//				cerr << "Failed, new retval: " << retval << endl;
			}

			rotate(diamond);
			rotate(diamond);
			rotate(diamond);
			while(!check(diamond))
			{
				temp += append(diamond);
//				cerr << "Failed (Rotate), new retval: " << retval << endl;
			}
		}
		retval = min(temp,retval);

		rotate(orig);
		rotate(orig);

		temp = 0;
		diamond = orig;
		{
			while(!check(diamond))
			{
				temp += append(diamond);
//				cerr << "Failed, new retval: " << retval << endl;
			}

			rotate(diamond);
			while(!check(diamond))
			{
				temp += append(diamond);
//				cerr << "Failed (Rotate), new retval: " << retval << endl;
			}
		}
		retval = min(temp,retval);

		temp = 0;
		diamond = orig;
		{
			while(!check(diamond))
			{
				temp += append(diamond);
//				cerr << "Failed, new retval: " << retval << endl;
			}

			rotate(diamond);
			rotate(diamond);
			rotate(diamond);
			while(!check(diamond))
			{
				temp += append(diamond);
//				cerr << "Failed (Rotate), new retval: " << retval << endl;
			}
		}
		retval = min(temp,retval);

//		print(diamond);
//		cerr << endl;

//		rotate(diamond);
//		print(diamond);
//		cerr << endl;

		cout << "Case #" << x << ": ";
		cout << retval;
		cout << endl;
	}
	return 0;
}
