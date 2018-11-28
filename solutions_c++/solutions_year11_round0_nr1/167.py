#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int get(int t,int x,int y,int z)
{
	z += abs(x-y);
	return max(t,z)+1;
}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("in.txt","rt",stdin);
	freopen("A_large.txt","wt",stdout);
#endif
	int TC,n;
	scanf("%d",&TC);
	for(int tc=0;tc<TC;tc++)
	{
		scanf("%d",&n);
		int t = 0;
		char lst = '*';
		int lst_o=1;
		int lst_b=1;
		int lto,ltb;
		lto = ltb = 0;
		int x;
		char c;
		for(int i=0;i<n;i++)
		{
			scanf(" %c %d",&c,&x);
			t = get(t,x,c=='O'?lst_o:lst_b,c=='O'?lto:ltb);
			if(c=='O'){
				lst_o = x;
				lto = t;
			}
			else{
				lst_b = x;
				ltb = t;
			}
		}
		printf("Case #%d: %d\n",tc+1,t);
	}
	return 0;
}