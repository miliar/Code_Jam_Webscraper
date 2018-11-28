#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>

using namespace std;

string s,tmp;
set < string > S;

void err()
{
	cout << "errror!!!!";
}

struct ifer
{
	ifer()
	{
		p = 1;
		s = "";
		left = 0;
		right = 0;
	}
	double p;
	string s;
	int left,right;
} a[100000];
int a_size = 0;

int f(int &i)
{
	i++;
	a_size++;
	
	a[a_size].p = 1.0;
	a[a_size].s = "";
	a[a_size].left = 0;
	a[a_size].right = 0;
	
	int cur_a = a_size;
	
	for(;i < (int)s.length()-1; i++)
	{
		
		if( isdigit(s[i]) )
		{
			tmp = "";
			while( isdigit(s[i]) || s[i] == '.' )
			{
				tmp += s[i]; i++;
			}
			a[ cur_a ].p = atof( tmp.c_str() );
		}
		
		if( isalpha(s[i]) )
		{
			tmp = "";
			while( isalpha(s[i]) )
			{
				tmp += s[i++];
			}
			a[ cur_a ].s = tmp;
		}
		
		if( s[i] == '(' )
		{
			if( a[ cur_a ].left == 0 ) a[ cur_a ].left = f(i); else
			if( a[ cur_a ].left != 0 && a[ cur_a ].right == 0 ) a[ cur_a ].right = f(i); else err();
		}
		
		if( s[i] == ')' ) break;
		
	}
	
	//cout << cur_a << " " << a[cur_a].s << " " << a[cur_a].left << " " << a[cur_a].right << endl;
	
	i++;
	return cur_a;
}

void solve()
{
	s.clear();
	int n;
	scanf("%d\n",&n);
	for(int i = 0; i < n; i++)
	{
		getline( cin, tmp );
		s += " "+tmp;
	}
	
	a_size = 0;
	for(int i = 0; i < (int)s.length(); i++)
	{
		if( s[i] == '(' ) f(i);
	}
	
	int k;
	scanf( "%d\n",&n );
	for(int i = 0; i < n; i++)
	{
		cin >> s >> k;
		S.clear();
		for(int j = 0; j < k; j++)
		{
			cin >> tmp;
			S.insert( tmp );
		}
		
		double p = 1.0;
		int id = 1;
		while( id != 0 )
		{
			p *= a[ id ].p;
			if( S.find( a[id].s ) != S.end() )
			{
				id = a[id].left;
			} else
			{
				id = a[id].right;
			}
		}
		
		printf("%0.8lf\n",p);
	}
}

int main()
{
	int n;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	scanf( "%d",&n );
	for(int i=0; i < n; i++)
	{
		cout << "Case #" << i+1 << ":" << endl;
		solve();
	}
	
	return 0;
}
