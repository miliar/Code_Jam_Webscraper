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
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

#define vs vector<string>
#define vi vector<int>
#define vii vector<vector<int>>
#define ll long long
#define pb push_back
#define si size()
#define FOR(i,j,k) for(int i = (j) ; i <= (k) ; i++ )
#define FORN(i,j,k) for(int i = (j) ; i >= (k) ;i--)
#define MAX 1000000

int calc(int *button,char *col,int but)
{
	char last = col[0];
	int lb, lo;
	int time = button[0], temp = button[0];
	
	if(last == 'B')
	{
		lb = button[0];
		lo = 1;
	}
	else
	{
		lb = 1;
		lo = button[0];
	}


//	cout << "\n1" << " " << time << endl;

	FOR(i,1,but - 1)
	{
		char curr = col[i];

		if(curr == last)
		{
			int step = button[i],k;

			if(curr == 'B')
			{
				k = abs(step - lb);
				lb = step;
			}
			else
			{
				k = abs(step - lo);
				lo = step;
			}

			time += k + 1;
			temp += k + 1;
		}
		else
		{	int step = button[i],k;

			if(curr == 'B')
			{
				k = abs(step - lb);
				lb = step;
			}
			else
			{
				k = abs(step - lo);
				lo = step;
			}
			
			if(temp >= k)
			{
				time++;
				temp = 1;
			}
			else
			{
				time += k - temp + 1;
				temp =  k - temp + 1;
			}
		}
		
		last = curr;

//		cout <<  i + 1 << " " << time << endl;
	
	}
	
	return time;

}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("out1.in");

	int t, i = 1,but;
	int  button[1000];
	char col[1000];   	
	
	fin >> t;

	while(i <= t)
	{
		fin >> but;
			
		FOR(j,0,but - 1)
		{
			fin >> col[j] >> button[j];
		}
		
		fout << "Case #" << i << ": ";
		fout << calc(button,col,but) << endl;
		i++;
	}

	return 0;
}
