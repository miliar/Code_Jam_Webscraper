#include<iostream>
#include<cstdio>
#include<vector>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<cmath>
#include<queue>
#include<cstring>
#include<string>
#include<algorithm>
//#include<nevertimelimited.h>
//#include<neverwronganswer.h>
//#include<accepted forever.h>
using namespace std;
int v[1000+20];
int main(void){
	FILE * fp1=fopen("in.in","r");
	FILE * fp2=fopen("out.in","w");
	int t,k,n,sum,minv;
	fscanf(fp1,"%d",&t);
	for(k=1;k<=t;k++){
		fscanf(fp1,"%d",&n);
		for(int i=0;i<n;i++)
			fscanf(fp1,"%d",&v[i]);
		sum=0;
		for(int i=0;i<n;i++)
			sum^=v[i];
		if(sum!=0){
			fprintf(fp2,"Case #%d: NO\n",k);
			continue;
		}
		minv=sum=v[0];
		for(int i=1;i<n;i++){
			if(v[i]<minv) minv=v[i];
			sum+=v[i];
		}
		fprintf(fp2,"Case #%d: %d\n",k,sum-minv);
	}
	system("pause");
	return 0;
}