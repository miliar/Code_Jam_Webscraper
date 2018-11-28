#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
 
#define forn(i, n) for (int i = 0; i < n; i ++)
#define ford(i, n) for (int i = n - 1; i >= 0; i --)
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define pi 3.1415926535897932
#define ll long long
#define ld long double
 
using namespace std;

int t;
int n;
struct go
{
	char a;
	int b;	
};
go a[20];
int findn (int b, char c)
{
	for(int i = b + 1; i < n; i ++)
		if (a[i].a == c)
			return i;
	return -1;
}

void make (int i)
{
	printf("Case #%d: ", i + 1);
	cin>> n;
	
	forn(i , n)
		cin>>a[i].a>>a[i].b;
	int sum = 0;
	int b=1,or = 1;
	int bs = findn(-1, 'B') , os = findn(-1,'O');
	
	forn(i, n)
	{
		if (a[i].a == 'O')
		{
			int d = abs(a[i].b - or) + 1;
			sum += d ;
			os = findn(os,'O');
			if (bs != -1)
			if (abs(a[bs].b - b) <= d)
				b = a[bs].b;
			else
				
				if (a[bs].b > b)
					b += d;
				else b -= d;
			or = a[i].b;
		}
		if (a[i].a == 'B')
		{
			int d = abs(a[i].b - b) + 1;
			sum += d;
			bs = findn(bs,'B');
			if (os != -1)
			if (abs(a[os].b - or) <= d)
				or = a[os].b;
			else
				
				if (a[os].b > or)
					or += d;
				else or -= d;
			b = a[i].b;			
		}
	}
	cout<<sum<<endl;
}

int main(){
        freopen ("input.txt","rt",stdin);
        freopen ("output.txt","wt",stdout);
		cin >> t;	
		forn(i, t)
		{
			make(i);
		}

		return 0;
		}