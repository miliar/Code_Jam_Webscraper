#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()
#define sz(a) a.size()
#define For(i, a, b) for(int i = a; i < b; i++)
#define Ror(i, a, b) for(int i = a - 1; i >= b; i--)

typedef pair<int, int> pii;
typedef long long lint;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int Size = 10000;
char buffer[Size];

const int inf = 0x0fffffff;
const int white = 0, gray = 1, black = 2;

const double eps = 10e-6;



int Solution(int nTest)
{
	int n, d;
	scanf("%d%d", &n, &d);
	vvi ar(n, vi(n));
	getchar();
	For(i, 0, n)
	{
		For(j, 0, n)
			ar[n-i-1][j] = getchar();
		getchar();
	}
	vector<vector<char> >  m(n, vector<char>(n));
	For(i, 0, n)
		For(j, 0, n)
		{
			m[i][j] = ar[j][n-i-1];
	}
	For(j, 0, n)
	{
		int i = 0;
		int t = 0;
		while(i < n)
		{
			if(m[i][j] == '.')
			{
				i++;
				continue;
			}
			else
			{
				int l = m[i][j];
				m[i][j] = '.';
				m[t][j] = l;
				i++;
				t++;
			}
		}
		

	}
	bool red = false, blue = false;
	For(i, 0, n)
	{
		int cnt = 0;
		int last = 0;
	For(j, 0, n)
	{
		if(m[i][j] == 'R')
		{
			if(last == 'R')
			{
				cnt++;
				if(cnt == d)
					red = true;
			}
			else
			{
				last = 'R';
				cnt = 1;
				if(d == 1)
					red = true;
			}
		}
		else
		if(m[i][j] == 'B')
		{
			if(last == 'B')
			{
				cnt++;
				if(cnt == d)
					blue = true;
			}
			else
			{
				cnt = 1;
				if(d == 1)
					blue = true;
				last = 'B';
			}
		}
	}
	}
	For(j, 0, n)
	{
		int cnt = 0;
		int last = 0;
	For(i, 0, n)
	{
		if(m[i][j] == 'R')
		{
			if(last == 'R')
			{
				cnt++;
				if(cnt == d)
					red = true;
			}
			else
			{
				last = 'R';
				cnt = 1;
			}
		}
		else
		if(m[i][j] == 'B')
		{
			if(last == 'B')
			{
				cnt++;
				if(cnt == d)
					blue = true;
			}
			else
			{
				cnt = 1;
				last = 'B';
			}
		}
	}
	}
	For(k, 0, n)
	{
		int cnt = 0;
		int last = 0;
		
	For(l, 0, k+1)
	{
		int j = l;
		int i = k - l;
		if(m[i][j] == 'R')
		{
			if(last == 'R')
			{
				cnt++;
				if(cnt == d)
					red = true;
			}
			else
			{
				last = 'R';
				cnt = 1;
			}
		}
		else
		if(m[i][j] == 'B')
		{
			if(last == 'B')
			{
				cnt++;
				if(cnt == d)
					blue = true;
			}
			else
			{
				cnt = 1;
				last = 'B';
			}
		}
	}
	}		
	For(k, 0, n)
	{
		int cnt = 0;
		int last = 0;
		
	For(l, 0, n - k)
	{
		int j = l;
		int i = k + l;
		if(m[i][j] == 'R')
		{
			if(last == 'R')
			{
				cnt++;
				if(cnt == d)
					red = true;
			}
			else
			{
				last = 'R';
				cnt = 1;
			}
		}
		else
		if(m[i][j] == 'B')
		{
			if(last == 'B')
			{
				cnt++;
				if(cnt == d)
					blue = true;
			}
			else
			{
				cnt = 1;
				last = 'B';
			}
		}
	}
	}		

///dfdfddddddddd

	For(k, 0, n)
	{
		int cnt = 0;
		int last = 0;
		
	For(l, 0, k+1)
	{
		int j = n-l-1;
		int i = k - l;
		if(m[i][j] == 'R')
		{
			if(last == 'R')
			{
				cnt++;
				if(cnt ==d)
					red = true;
			}
			else
		{
				last = 'R';
				cnt = 1;
			}
		}
		else
		if(m[i][j] == 'B')
		{
			if(last == 'B')
			{
				cnt++;
				if(cnt == d)
					blue = true;
			}
			else
			{
				cnt = 1;
				last = 'B';
			}
		}
	}
	}		
	For(k, 0, n)
	{
		int cnt = 0;
		int last = 0;
		
	For(l, 0, n - k)
	{
		int j = n - l-1;
		int i = k + l;
		if(m[i][j] == 'R')
		{
			if(last == 'R')
			{
				cnt++;
				if(cnt == d)
					red = true;
			}
			else
		{
				last = 'R';
				cnt = 1;
			}
		}
		else
		if(m[i][j] == 'B')
		{
			if(last == 'B')
			{
				cnt++;
				if(cnt ==d)
					blue = true;
			}
			else
			{
				cnt = 1;
				last = 'B';
			}
		}
	}
	}	
	printf("Case #%d: ", nTest + 1);
	if(blue && red)
		printf("Both\n");
	else
		if(blue)
			printf("Blue\n");
		else
			if(red)
				printf("Red\n");
			else
				printf("Neither\n");



	return 1;
}

int main()
{
	
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 9999;
	
	scanf("%d", &n);

	while(i < n && Solution(i))
		i++;

	return 0;
}