#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
struct pp{
	int startshi,startfen,endshi,endfen;
};
pp a[100],b[100];
bool aflag[101],bflag[101];
int ache,bche,turntimes;
void dfs( int num , pp aaa )
{
	int startshi,startfen,i;
	startshi=aaa.endshi;
	if(aaa.endfen+turntimes>60)
	{
		startfen=aaa.endfen+turntimes-60;
		startshi++;
	}
	else
		startfen=aaa.endfen+turntimes;
	if ( 2 == num )
	{
		for( i = 0 ; i < bche ; i ++ )
		{
			if( bflag[i] == 0 )
			{
				if( b[i].startshi > startshi )
				{
					bflag[i]=1;
					dfs( 1 , b[i] );
					return ;
				}
				if( b[i].startshi==startshi&&b[i].startfen>=startfen)
				{
					bflag[i]=1;
					dfs( 1 , b[i] );
					return ;
				}
			}
		}
	}
	else if ( 1 == num )
	{
		for( i = 0 ; i < ache ; i ++ )
		{
			if( aflag[i] == 0 )
			{
				if( a[i].startshi > startshi )
				{
					aflag[i]=1;
					dfs( 2 , a[i] );
					return ;
				}
				if( a[i].startshi==startshi&&a[i].startfen>=startfen)
				{
					aflag[i]=1;
					dfs( 2 , a[i] );
					return ;
				}
			}
		}
	}
}
bool cmd( pp aa , pp bb )
{
	if(aa.startshi!=bb.startshi) return aa.startshi<bb.startshi;
	else return aa.startfen<bb.startfen;
}
int cmdd( pp aa , pp bb )
{
	if(aa.startshi<bb.startshi)
		return 1;
	else if( aa.startshi>bb.startshi)
		return 0;
	else if( aa.startfen<bb.startfen)
		return 1;
	else if( aa.startfen>bb.startfen)
		return 0;
	else return 1;
}
int main()
{
	
	char q;
	int cas,cass=1;
	freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	while(cas--)
	{
		memset(aflag,0,sizeof(aflag));
		memset(bflag,0,sizeof(bflag));
		int atimes=0,btimes=0,i,j;
		scanf("%d",&turntimes);
		scanf("%d %d",&ache,&bche);
		for( i = 0 ; i < ache ; i ++ )
		{
			scanf("%d%c%d%c%d%c%d",&a[i].startshi,&q,&a[i].startfen,&q,&a[i].endshi,&q,&a[i].endfen);
		}
		for( i = 0 ; i < bche ; i ++ )
		{
			scanf("%d%c%d%c%d%c%d",&b[i].startshi,&q,&b[i].startfen,&q,&b[i].endshi,&q,&b[i].endfen);
		}
		sort(&a[0],&a[ache],cmd);
		sort(&b[0],&b[bche],cmd);
		while(1)
		{
			int zz=0;
			for( i = 0 ; i < ache ; i ++ )
			{
				if(aflag[i]==0)
					break;
			}
			for( j = 0 ; j < bche ; j ++ )
			{
				if(bflag[j]==0)
					break;
			}
			if(i==ache&&j==bche)
				break;
			if(i==ache&&j<bche)
				zz=0;
			else if(j==bche&&i<ache)
				zz=1;
			else zz=cmdd(a[i],b[j]);
			if(zz==1)
			{
				aflag[i]=1;
				atimes++;
				dfs( 2 , a[i]);
			}
			else if(zz==0)
			{
				bflag[j]=1;
				btimes++;
				dfs( 1 , b[j]);
			}
		}
		printf("Case #%d: ",cass);cass++;
		printf("%d %d\n",atimes,btimes);
	}
	return 0;
}