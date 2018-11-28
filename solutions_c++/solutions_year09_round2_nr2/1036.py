#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>
#include<functional>
using namespace std;

void GetNext(const double & lfSour, double & lfDest)
{
	int nList[32];
	int nPos = 0;
	double lfTemp = lfSour;
	while(lfTemp >= 0.99999999999999999999)
	{
	
			nList[nPos ++] = (__int64)(lfTemp) % 10;
			lfTemp /= 10;
	
	}
	int i = 0,j=0;
	bool haschange = false;
	for(i = 1 ; i < nPos ; ++i )
	{
		int ntemp = nList[i];
		for(j = 0 ; j < i ; ++j)
		{
			if(ntemp < nList[j] )
			{
				
				if(nList[j] < nList[i] || haschange == false)
					swap(nList[i],nList[j]);
				haschange = true;
			}
		}
		if(haschange)
		{
			sort(nList , nList + i , greater<int>());
			break;
		}
	}
	if(haschange == false)
	{
		nList[nPos++] = 0;
		sort(nList,nList+nPos,greater<int>());
		if(nList[nPos - 1] == 0)
		{
			i = nPos - 1;
			while(nList[i] == 0) --i;
			swap(nList[nPos-1],nList[i]);
		}
	}
	lfDest = 0;
	for(i = nPos - 1; i >= 0 ; --i)
	{
		lfDest *= 10;
		lfDest += nList[i];
		
	}

}
void GetNext(int * nList,double & lfDest,int & nPos)
{
//	int nPos = 0;
	int i = 0,j=0;
	bool haschange = false;
	for(i = nPos - 1 ; i >= 0 ; --i )
	{
		int ntemp = nList[i];
		for(j = nPos - 1 ; j > i ; --j)
		{
			if(ntemp < nList[j] )
			{
				
				if(nList[j] < nList[i] || haschange == false)
					swap(nList[i],nList[j]);
				haschange = true;
			}
		}
		if(haschange)
		{
			sort(nList + i + 1 , nList + nPos);
			break;
		}
	}
	if(haschange == false)
	{
		nList[nPos++] = 0;
		sort(nList,nList+nPos);
		if(nList[0] == 0)
		{
			i = 0;
			while(nList[i] == 0) ++i;
			swap(nList[0],nList[i]);
		}
	}
	lfDest = 0;
	for(i = 0; i < nPos ; ++i)
	{
		lfDest *= 10;
		lfDest += nList[i];
		
	}

}
int main(int argc , char ** argv)
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	int T ;
	scanf("%d",&T);
	getchar();
	int nt = 0;
	int nPos = 0;
	int nSourList[32],nDestList[32];
	double lfNext;
	for(nt = 1; nt <= T; ++nt)
	{
		memset(nSourList,0,sizeof(nSourList));
		memset(nDestList,0,sizeof(nDestList));
		char ch = 0;
		nPos = 0;
		while(ch = getchar())
		{
			if(ch >= '0' && ch <= '9') nSourList[nPos ++] = ch - '0';
			else break;
		}
		GetNext(nSourList,lfNext,nPos);
		printf("Case #%d: ",nt);
		for(int i = 0 ; i < nPos ; ++i)
		{
			printf("%d",nSourList[i]);
		}
		printf("\n");
	}
	return 0;
}