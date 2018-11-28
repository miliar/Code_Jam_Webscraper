#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream> 
#include <cmath>
#include <cstring>

using namespace std;

#define pb push_back
#define mp make_pair
#define PII pair<int,int> 
#define B second
#define PIII pair<int,PII> 

#define I(x,y) x <y> :: iterator 
#define set(a,c) memset(a,c,sizeof(a))

#define REP(i,n) for(int i=0;i<n;i++)

typedef unsigned long long LLU;
typedef long long LL;
typedef long double LD;
int Area(){
	int A = 0;
}
int main()
{
	int KASES;
	scanf("%d",&KASES);
	for(int kases=0;kases<KASES;kases++)
	{
		int N,M,A;
		printf("Case #%d: ",kases+1);
		scanf("%d %d %d",&N,&M,&A);
		if(A>N*M)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		N++,M++;
		int x1,y1,x2,y2,x3,y3;
		int i,j,k,found = 0;
		for(i=0;i<N*M && found ==0;i++)
			for(int j=i+1;j<N*M && found==0;j++)
				for(k=j+1;k<N*M && found ==0 ;k++)
				{

					 x1 = i/(M),y1 = i%(M);
					 x2 = j/(M),y2=j%(M);
					 x3 = k/(M),y3=k%(M);
					if(A== (x2-x1) * (y1+y2) + (x3-x2)*(y2+y3) + (x1-x3)*(y3+y1))
						found = 1;
				}
		if(found==1)
			printf("%d %d %d %d %d %d\n",x1,y1,x2,y2,x3,y3);
		else
			printf("IMPOSSIBLE\n");

	}
}

