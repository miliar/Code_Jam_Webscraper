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

map <string, int> m;
int last;
vector <pair <int, int> > ad[101000];
int getval(string s)
{
	if (m[s]) return m[s];
	last++;
	return m[s]=last;
}

int mas[100010];
int n;
int res=0;
int nextv=1;
void go(int v, int pos, bool st)
{
	if (pos>n) return;
	for (int i=0;i<sz(ad[v]);i++)
		if (ad[v][i].first==mas[pos])
		{
			go(ad[v][i].second,pos+1,st);
			return ;
		}
	if (st) res++;
	nextv++;
	ad[v].push_back(make_pair(mas[pos],nextv));
	go(nextv,pos+1,st);

}
char st[1010];
int main()
{

	init();

	int tst;
	scanf("%d\n",&tst);
	for (int cas=1;cas<=tst;cas++)
	{
		m.clear();
		last=0;
		nextv=1;
		for (int i=0;i<100100;i++)		ad[i].clear();
		int a,b;
		scanf("%d %d\n",&a,&b);
		res=0;
		for (int i=0;i<a+b;i++) {
			gets(st);
			int len=strlen(st);		
			n=0;
			for (int i=0;i<len;i++)
				if (st[i]=='/') st[i]=' ';
			istringstream ss(st);
			string s;
			n=0;
			while (ss >> s)
			{
				n++;
				mas[n]=getval(s);
			}
			if (i<a) go(0,1,0); else
				go(0,1,1);
		}
			
		printf("Case #%d: %d\n",cas,res);
	}
	
	
	

  return 0;
}
