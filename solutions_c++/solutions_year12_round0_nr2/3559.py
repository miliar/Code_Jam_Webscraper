#include<algorithm>
#include<cstdio>
#include<iostream>
#include<vector>
#include<cmath>
#include<map>

using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("outf.txt","w",stdout);
	int test;
	scanf("%d",&test);
	for(int x=0;x<test;x++)
	{
		int n,s,p,t,r,res=0;
		scanf("%d%d%d",&n,&s,&p);
		for(int i=0;i<n;i++){
			scanf("%d",&t);
			r=t/3;if(t%3!=0)r++;
			if(r>=p)res++;
			else if(r==(p-1) and s>0 and r!=0 and (t%3==2 || t%3==0)){s--;res++;}
		}
		printf("Case #%d: %d\n",x+1,res);
	}
		
	return 0;
}