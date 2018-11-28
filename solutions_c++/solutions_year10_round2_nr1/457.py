#include <iostream>
#include <cstdio>
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
#define MAX_STRING 100000
#define PB push_back
#define MP make_pair

using namespace std;

char buf[MAX_STRING];	

void get_string(string &s)
	{
	scanf("%s", &buf);
	s.assign(buf);
	}

bool get_line(string &s)
	{
	if(!gets(buf)) return false;
	s.assign(buf);
	return true;
	}


int t,n,m,a,b;
string s;
set<string> folders;

void add_path(string path)
{
string cur = "";
fr(i,path.length())
	if(path[i]=='/'&&cur.length()>0) 
	{
		folders.insert(cur);
		cur+="-";
	}
	else if(path[i]!='/')
		cur+=path[i];
folders.insert(cur);
cur+="-";
}

int main()
{
freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
scanf("%d", &t);
fr(x,t)
	{
	folders.clear();
	scanf("%d %d\n", &n, &m);
	fr(i,n)
		{
		get_line(s);
		add_path(s);
		}
	a = folders.size();
	fr(i,m)
		{
		get_line(s);
		add_path(s);
		}
	b = folders.size();
	b-=a;
	printf("Case #%d: %d\n", x+1, b);		
	}
return 0;
}
