#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
int count,posA,posB,ordnow,timesum,ordA,ordB;
int oA[105],oB[105],cntA,cntB;
int noA[105],noB[105],cntno,n;
int whos[105];

void ipA()
{
	cin>>oA[cntA];
	noA[cntA++]=cntno++;
}

void ipB()
{
	cin>>oB[cntB];
	noB[cntB++]=cntno++;
}

void tim()
{
	bool actA=false,actB=false;
	timesum++;

	if(whos[ordnow]==0)
	{
		if(posA==oA[ordA]) {ordnow++;ordA++;actA=true;}
	}
	else
	{
		if(posB==oB[ordB]) {ordnow++;ordB++;actB=true;}
	}
	
	if(!actA){
		if( posA<oA[ordA] ) posA++;
		else if( posA>oA[ordA] ) posA--;
	}
	
	if(!actB){
		if( posB<oB[ordB] ) posB++;
		else if( posB>oB[ordB] ) posB--;
	}
}


int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,TT,i;
	cin >> TT;
	string ipt;
	for(T=1;T<=TT;T++)
	{

		count=0;posA=1;posB=1;ordnow=0;timesum=0;ordA=0;ordB=0;
		cntA=0;cntB=0;
		cntno=0;


		cin >> n;
		for(i=0;i<n;i++)
		{
			cin >> ipt;

			if(ipt[0]=='O') {ipA();whos[i]=0;}
			else {ipB();whos[i]=1;}
		}
		while(ordnow<n)
		{
			tim();		
		}
		printf("Case #%d: %d\n",T,timesum);
	}
	return 0;
}