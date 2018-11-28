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
#pragma comment(linker, "/STACK:50000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "C-large";

void init(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
}

int a,b;
int calc(int v)
{
	vi d;
	int x=v;
	while(x) 
	{
		d.push_back(x%10);
		x/=10;
	}
	reverse(all(d));
	vi res;
	for (int i=0;i<sz(d);i++)		
	{
		int v2=0;
		for (int j=0;j<sz(d);j++)
			v2=v2*10 + d[j];
			
		int t= d[0];
		d.erase(d.begin());
		d.push_back(t);

		if (t==0) continue;
		if (v2>v)
		res.push_back(v2);
	
	}
	
	res.push_back(0);
	sort(all(res));
	int r=0;
	for (int i=1;i<sz(res);i++)
		if (res[i]!=res[i-1] && res[i]>=a && res[i]<=b)
			r++;
	return r;
	

}

int main() {

	init();

	

	int tst;
	scanf("%d\n",&tst);

	for (int cas=1;cas<=tst;cas++)
	{		
		scanf("%d %d",&a,&b);
		int res=0;
		for (int i=a;i<=b;i++)
			res+=calc(i);

		printf("Case #%d: %d\n",cas,res);	
	}


	

	

	return 0;
}