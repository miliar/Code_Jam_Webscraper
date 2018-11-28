#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}


int f(string a, string b)
{	
	string s;
	int p=0;
	for (int i=0;i<sz(a);i++)
	{
		s="";
		if (b[p]=='(')
		{
			p++;
			while (b[p]!=')')
			{
				s+=b[p];
				p++;
			}
		} else s+=b[p];
		p++;
		if (s.find(string(1,a[i]))==-1) return 0;
	}
	return 1;
}

char w[5010][110],p[511][1010];

int main()
{
 init();


	int l,d,n;
	scanf("%d%d%d\n",&l,&d,&n);
	for (int i=0;i<d;i++) gets(w[i]);
	int cas=0;
	for (int i=0;i<n;i++) 
	{
		gets(p[i]);
		int res=0;
		for (int j=0;j<d;j++)
			if (f(w[j],p[i])) res++;
		cas++;
		printf("Case #%d: %d\n",cas,res);
	}




   return 0; 
}
