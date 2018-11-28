#include <iostream>
#include<cstdio>

using namespace std;


int main()
{
	int test,t,i,j;
	long N,n,K;
	bool ans;
	FILE*fp;
	fp=fopen("outputlarge.txt","a");
	cin >> test;
	for(t=1;t<=test;t++){
		
		cin >> n >> K; 
		
		if(K==0) ans=false;
		else{
			N=1;
			for(i=0;i<n;++i) N*=2;
			++K;
			if(K%N==0) ans=true;
			else ans=false;
		}
		
		if(ans==true) fprintf(fp,"Case #%d: ON\n",t);
		else fprintf(fp,"Case #%d: OFF\n",t);
	}
	fclose(fp);
	return 0;
	
}
		
		
