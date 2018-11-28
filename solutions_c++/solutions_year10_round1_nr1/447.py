#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
#include <cassert>
using namespace std;

const int MAX_N=100;

int N,K;
char field[MAX_N][MAX_N]={0};

int memo[MAX_N][MAX_N][4]={0};

void print()
{
	for(int j=0;j<N;j++)
	{
		for(int i=0;i<N;i++)
			cerr<<field[j][i];
		cerr<<endl;
	}
	for(int j=0;j<N;j++)
	{
		for(int i=0;i<N;i++)
			fprintf(stderr,"%2d",memo[j][i][0]);
		fprintf(stderr,"\n");
	}
	fprintf(stderr,"\n");
	for(int j=0;j<N;j++)
	{
		for(int i=0;i<N;i++)
			fprintf(stderr,"%2d",memo[j][i][1]);
		fprintf(stderr,"\n");
	}
	fprintf(stderr,"\n");
	for(int j=0;j<N;j++)
	{
		for(int i=0;i<N;i++)
			fprintf(stderr,"%2d",memo[j][i][2]);
		fprintf(stderr,"\n");
	}
	fprintf(stderr,"\n");
	for(int j=0;j<N;j++)
	{
		for(int i=0;i<N;i++)
			fprintf(stderr,"%2d",memo[j][i][3]);
		fprintf(stderr,"\n");
	}
	fprintf(stderr,"\n");
}

void gravityR()
{
	for(int j=0;j<N;j++)
	{
		int k=0;
		for(int i=0;i<N;i++)
		{
			if(field[j][i]=='.')
				continue;
			
			field[j][k]=field[j][i];
			k++;
		}
		for(int i=k;i<N;i++)
			field[j][i]='.';
	}
}

bool isIn(int x,int y)
{
	return 0<=x && x<N && 0<=y && y<N;
}

int check()
{
	for(int j=0;j<N;j++)
	for(int i=0;i<N;i++)
	{
		char c=field[j][i];
		if(c=='.')
		{
			memo[j][i][0]=0;
			memo[j][i][1]=0;
			memo[j][i][2]=0;
			memo[j][i][3]=0;
			continue;
		}
		
		int p=(c=='B')?+1:-1;
		memo[j][i][0]=p;
		memo[j][i][1]=p;
		memo[j][i][2]=p;
		memo[j][i][3]=p;
		
		if(isIn(j-1,i  )) if(field[j-1][i  ]==c) memo[j][i][0]=memo[j-1][i  ][0]+p;
		if(isIn(j  ,i-1)) if(field[j  ][i-1]==c) memo[j][i][1]=memo[j  ][i-1][1]+p;
		if(isIn(j-1,i-1)) if(field[j-1][i-1]==c) memo[j][i][2]=memo[j-1][i-1][2]+p;
		if(isIn(j-1,i+1)) if(field[j-1][i+1]==c) memo[j][i][3]=memo[j-1][i+1][3]+p;
	}
	
	int winB=0;
	int winR=0;
	for(int j=0;j<N;j++)
	for(int i=0;i<N;i++)
	{
		for(int d=0;d<4;d++)
		{
			if(memo[j][i][d]>=+K)
				winB=1;
			if(memo[j][i][d]<=-K)
				winR=2;
		}
	}
	return winB|winR;
}

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		for(int j=0;j<MAX_N;j++)
		for(int i=0;i<MAX_N;i++)
			field[j][i]='.';
		
		cin>>N>>K;
		for(int j=0;j<N;j++)
		for(int i=0;i<N;i++)
			cin>>field[N-1-j][N-1-i];
		
		int result1=check();
		cerr<<"[Field]"<<endl;
//		fprintf(stderr,"#%d\n",result1);
//		print();
		
		gravityR();
		int result2=check();
		cerr<<"[Field]"<<endl;
//		fprintf(stderr,"#%d\n",result2);
//		print();
		
		int ans=(result1|result2);
		printf("Case #%d: ",ds);
		switch(ans)
		{
		case 0: printf("Neither\n"); break;
		case 1: printf("Blue\n"); break;
		case 2: printf("Red\n"); break;
		case 3: printf("Both\n"); break;
		default: assert(false);
		}
		cerr<<"-----------------------------"<<endl;
	}
	return 0;
}
