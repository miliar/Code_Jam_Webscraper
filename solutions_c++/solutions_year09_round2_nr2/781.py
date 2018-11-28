#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <set>
#include <vector>
#include <map>

#define mn(a,b) ((a<b) ? (a) : (b))
#define mx(a,b) ((a<b) ? (b) : (a))
#define ab(a) ((a<0) ? (-(a)) : (a))
#define fr(a,b) for(int a=0; a<b; ++a)
#define fe(a,b,c) for(int a=b; a<c; ++a)
#define fw(a,b,c) for(int a=b; a<=c; ++a)
#define df(a,b,c) for(int a=b; a>=c; --a)
#define BIG 1000000000
#define SMALL -1000000000

using namespace std;

char buf[40];

void get_string(string &s)
	{
	scanf("%s", &buf);
	s.assign(buf);
	}

int t;
string s;

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d\n", &t);
fr(i,t)
	{
	get_string(s);
	string temp = s;
	next_permutation(s.begin(), s.end());
	if(temp.compare(s)>=0)
		{
		s = '0'+temp;
		next_permutation(s.begin(),s.end());		
		}	
	printf("Case #%d: %s\n", i+1, s.c_str());
	}
return 0;
}
