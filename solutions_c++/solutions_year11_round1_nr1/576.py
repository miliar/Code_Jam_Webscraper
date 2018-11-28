#include<iostream>
#include<fstream>
#include<cstdio>

using namespace std;

#define REP(i,a,b) for(int i=a;i<b;++i)
#define RESET(v,t,s) memset(v,0,s*sizeof(t))

int main()
{
	ifstream fin("A-large.in");
	FILE* fp=fopen("A.o","w+");
	
	long long T,N,P_D,P_G;
	bool ans;
	int div[2]; // 2, 5
	int d_2[3]={1,2,4};
	int d_5[3]={1,5,25};
	
	fin>>T;
	REP(i,0,T)
	{
		fin>>N>>P_D>>P_G;
		
		if((P_D==0 && P_G==0) || (P_D==100 && P_G==100)) ans=1;
		else if(P_G==0 || P_G ==100) ans=0;
		else
		{
			if(P_D%4==0)div[0]=2;
			else if(P_D%2==0)div[0]=1;
			else div[0]=0;
			if(P_D%25==0)div[1]=2;
			else if(P_D%5==0)div[1]=1;
			else div[1]=0;
			
			ans = ( N*d_2[div[0]]*d_5[div[1]]>=100 )?1:0;
			
		}	
		
		printf("Case #%d: %s\n",i+1,ans?"Possible":"Broken");
		fprintf(fp,"Case #%d: %s\n",i+1,ans?"Possible":"Broken");
		
	}
	
	fclose(fp);
	return 0;
}
