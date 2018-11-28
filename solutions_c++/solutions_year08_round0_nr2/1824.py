#include<stdio.h>
#include<algorithm>
using namespace std;
class Time{
public:
	int hh ;
	int mm ;
	Time operator=( const Time b)
	{
		hh = b.hh;
		mm = b.mm;
		return *this;
	}
	Time operator+(int mini)
	{
		Time tmp ;
		tmp.mm = ( this->mm + mini ) % 60 ;
		tmp.hh = this->hh + (this->mm + mini)/60 ;
		return tmp;
	}
	bool operator<( const Time&b )
	{
		return ( hh * 60 + mm)< (b.hh * 60 + b.mm ) ;
	}
};
const int NMAX = 128 ;
Time Adep[NMAX],Aarr[NMAX],Bdep[NMAX],Barr[NMAX];
int T,NA,NB;
void init()
{
	scanf("%d",&T);
	scanf("%d%d",&NA,&NB);
	int i;
	char buffA[16],buffB[16];
	for( i = 0 ; i < NA ; i ++ )
	{
		scanf("%s%s",buffA,buffB);
		int hh ,mm ;
		sscanf(buffA,"%d:%d",&hh,&mm);
		Adep[i].hh = hh;
		Adep[i].mm = mm;
		sscanf(buffB,"%d:%d",&hh,&mm);
		Aarr[i].hh = hh;
		Aarr[i].mm = mm;
		Aarr[i] = Aarr[i] + T ;
		//printf("%d:%d %d:%d\n",A[i].departure.hh,A[i].departure.mm,A[i].arrivel.hh,A[i].arrivel.mm);
	}
	for( i = 0 ; i < NB ; i ++ )
	{
		scanf("%s%s",buffA,buffB);
		int hh,mm;
		sscanf(buffA,"%d:%d",&hh,&mm);
		Bdep[i].hh = hh;
		Bdep[i].mm = mm;
		sscanf(buffB,"%d:%d",&hh,&mm);
		Barr[i].hh = hh;
		Barr[i].mm = mm;
		Barr[i] = Barr[i] + T ;
		//		printf("%d:%d %d:%d\n",B[i].departure.hh,B[i].departure.mm,B[i].arrivel.hh,B[i].arrivel.mm);
	}
	sort(Adep,Adep+NA);
	sort(Aarr,Aarr+NA);
	sort(Bdep,Bdep+NB);
	sort(Barr,Barr+NB);
	/*
	for( i = 0 ; i < NA ; i ++ )
	{
		printf("%d:%d %d:%d\n",Adep[i].hh,Adep[i].mm,Aarr[i].hh,Aarr[i].mm);
	}
	puts("");
	for( i = 0 ; i < NB ; i ++ )
	{
		printf("%d:%d %d:%d\n",Bdep[i].hh,Bdep[i].mm,Barr[i].hh,Barr[i].mm);
	}
	*/
	return ;
}
void run()
{
	int i,j;
	int cntA = 0 , cntB = 0;
	j = 0;
	for( i = 0 ; i < NA ; i ++ )
	{
		if( j >= NB )
		{
			cntA += NA - i ;
			break;
		}
		if(Adep[i] < Barr[j] )
		{
			cntA ++;
		}
		else
		{
			j ++ ;
		}
	}
	j = 0 ;
	for( i = 0 ; i < NB ; i ++ )
	{
		if( j >= NA )
		{
			cntB += NB - i;
		}
		if( Bdep[i] < Aarr[j] )
		{
			cntB ++ ;
		}
		else
		{
			j ++ ;
		}
	}
	printf("%d %d\n",cntA,cntB);
}
int main()
{
#ifdef _DEBUG
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
#endif
	int nCase;
	scanf("%d",&nCase);
	int cnt = 0;
	while( nCase -- )
	{
		cnt ++ ;
		init();
		printf("Case #%d: ",cnt);
		run();
	}
	return 0 ;
}