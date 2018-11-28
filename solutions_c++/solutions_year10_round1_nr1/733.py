#include <vector>
#include <list>
#include <map>
#include <set>
#include <set>
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
#include <climits>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define Long long long
 
 char g[52][52];
 char r[52][52];
 
 void print(char a[][52], int n, int m)
 {
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<m; j++)
			printf("%c", a[i][j]);
		printf("\n");
	}
	printf("\n\n");
 }	
 
 int main()
 {
	freopen("data.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int t;
	scanf("%d", &t);
	
	for (int x=1; x<=t; x++)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		
		for (int i=0; i<n; i++)
			scanf("%s", g+i);
		
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
				r[j][n-1-i] = g[i][j];
		
		bool flag = true;
		while (flag)
		{
			flag = false;
			for (int i=n-1; i>0; i--)
				for (int j=0; j<n; j++)
					if (r[i][j] == '.' && r[i-1][j] != '.')
					{
						swap(r[i-1][j], r[i][j]);
						flag = true;
					}
		}
				
				
		//print(g, n, n);
		//print(r, n, n);
		
		bool a = false, b = false;
		for (int i=0; i<n; i++)
			for (int j=0; j<n; j++)
			{
				char c = r[i][j];
				if (c == '.') break;
				
				if (i+k-1<n)
				{
					int q;
					for (q=1; q<k; q++)
						if (r[i+q][j] != c) break;
					
					if (q == k)	
					{
						if (c=='R') a = true;
						else b = true;
						//cout << i << " " << j << endl;
					}
				}
				
				if (j+k-1<n)
				{
					int q;
					for (q=1; q<k; q++)
						if (r[i][j+q] != c) break;
					
					if (q == k)	
					{
						if (c=='R') a = true;
						else b = true;
						//cout << i << " " << j << endl;
					}
				}

				if (i+k-1<n && j+k-1<n)
				{
					int q;
					for (q=1; q<k; q++)
						if (r[i+q][j+q] != c) break;
					
					if (q == k)	
					{
						if (c=='R') a = true;
						else b = true;
						//cout << i << " " << j << endl;
					}
				}

				if (i+k-1<n && j-k+1>=0)
				{
					int q;
					for (q=1; q<k; q++)
						if (r[i+q][j-q] != c) break;
					
					if (q == k)	
					{
						if (c=='R') a = true;
						else b = true;
						//cout << i << " " << j << endl;
					}
				}
			}
		
		string str;
		if (a && b) str = "Both";
		else if (a) str = "Red";
		else if (b) str = "Blue";
		else str = "Neither";
		
		printf("Case #%d: %s\n", x, str.c_str());
	}	
	
	
 }