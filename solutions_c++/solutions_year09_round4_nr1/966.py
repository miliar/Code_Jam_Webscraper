#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

int n,t,num[100];
char tmp[200];

int main(){
	scanf("%d",&t);
	for (int z=1;z<=t;++z){
		memset(num,0,sizeof(num));
		scanf("%d",&n);
		gets(tmp);
		for (int i=1;i<=n;++i){
			for (int j=1;j<=n;++j){
				char c;
				scanf("%c",&c);
				if (c=='1') num[i]=j;
			}
			gets(tmp);
		}
		
		int ans=0;
		for (int i=1;i<=n;++i){
			if (num[i]>i){
	  		   int pos;
	  		   for (int j=i+1;j<=n;++j){
			   	   if (num[j]<=i){pos=j;break;}
			   }
			   for (int j=pos;j>i;--j){
			   	   ++ans;
			   	   num[j]=num[j-1];
			   }
	  		}
		}
		printf("Case #%d: %d\n",z,ans);
	}
	//scanf("\n");
	return 0;
}
