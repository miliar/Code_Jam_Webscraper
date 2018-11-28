#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<map>
#include<set>
#include<string>
#include<vector>
#include<utility>
#include<queue>
#include<iostream>
#include<list>
#include<sstream>
#include<cmath>
#define N 309

using namespace std;

int O[N],B[N],os[N],bs[N],lod[N],pos[N];


int main()
{
	int test,i,j,k,l,m,n,cas=1,oc,bc,pos1,pos2,id1,id2,cnt,sum;
	char ch;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&test);
	while( test-- )
	{
		scanf("%d",&n);
		oc=bc=0;
		for(i=0;i<n;i++)
		{
			scanf(" %c %d",&ch,&m);
			if( ch=='O' ) O[oc++] = m;
			else B[bc++] = m;
			os[i]=bs[i]=0,lod[i]=ch,pos[i]=m;
		}
		sum =id1=id2=cnt=0,pos1=pos2=1;
		bool F = false;
		while(true)
		{
			if( n-cnt==0 ) break; 
			F = false;
			if(lod[cnt]=='O' && pos1==pos[cnt])              {F=true;cnt++;id1++;}
			else if(id1<oc && pos1>O[id1])                   pos1--;
			else if(id1<oc && pos1<O[id1])	                 pos1++;
			if(lod[cnt]=='B' && pos2==pos[cnt] && F==false ) {cnt++;id2++;}
			else if(id2<bc && pos2>B[id2])                   pos2--;
			else if(id2<bc && pos2<B[id2])                   pos2++;
			                                                 os[i]=bs[i]=sum++;
		}
		printf("Case #%d: %d\n",cas++,sum);
	}
	return 0;
}