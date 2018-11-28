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

string problem_name = "C-small-attempt2";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

vector <int> pq;
int mas[10010];
bool u[10100];

int calc(vi a, int p)
{
	memset(u,1,sizeof(u));
	u[0]=u[p+1]=0;
	int res=0;
	for (int i=0;i<sz(a);i++)
	{
		int k=a[i]-1;
		while (u[k])
		{
			res++;
			k--;
		}	
		k=a[i]+1;
		while (u[k])
		{
			res++;
			k++;
		}
		u[a[i]]=0;
	}
	return res;

}

int main()
{

	init();

	int c;
	scanf("%d\n",&c);
	int cas=1;

	for (int cas=0;cas<c;cas++)
	{
		int p,q;
		scanf("%d %d",&p,&q);
		mas[0]=0;
		pq.clear();
		for (int i=1;i<=q;i++) {
			scanf("%d",&mas[i]);
			pq.push_back(mas[i]);
		};

		int res=1<<30;
		do {
			res=min(res,calc(pq,p));

		} while (next_permutation(all(pq)));
		
		printf("Case #%d: %d\n",cas+1,res);
		
	}


  

   return 0; 
}
