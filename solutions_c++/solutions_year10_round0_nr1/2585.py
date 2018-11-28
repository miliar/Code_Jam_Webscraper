#include<iostream>
#include<vector>
#include<cmath>
#include<cstdio>
using namespace std;

int main(){
	int t;scanf("%d",&t);
	FILE *pFile;
	pFile = fopen ("E:\\A11\\superscale.txt","w");
	for(int c=1;c<=t;c++){
		int n,k;vector<bool>v(32,0);int count=1;
		scanf("%d%d",&n,&k);
		while(k){
			v[count++]=k%2;
			k/=2;
		}bool f=1;
		for(int i=1;i<=n;i++)if(!v[i])f=0;
		if(f&&count>1)fprintf(pFile,"Case #%d: ON\n",c);
		else fprintf(pFile,"Case #%d: OFF\n",c);
	}
	fclose(pFile);
	return 0;
}