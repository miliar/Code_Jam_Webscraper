#include <string.h>
#include <math.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;


void Kevinew(){
#ifndef  ONLINE_JUDGE
	freopen("C:\\TDdownload\\B-large.in","r",stdin);
	freopen("C:\\TDdownload\\B-large.out","w",stdout);
#endif
}


struct _TimeSeg{
	int start, end;
	int flags,flage;
};

_TimeSeg A[110],B[110];

int cmp( const void *a ,const void *b) 
{ 
	return (*(_TimeSeg *)a).start > (*(_TimeSeg *)b).start ? 1 : -1; 
} 

//qsort(s,100,sizeof(s[0]),cmp); 



/*
bool _TimeSeg::operator<( const _TimeSeg &x,const _TimeSeg &y )
{
	if( x.start < y.start) return true;
	else if (x.end<y.end)
	{
		return true;
	}
	return false;
}
*/
int main(){
	int N,T,NA,NB,i,j,icase;
	int ncase,nS,nQ,ans1,ans2;
	int hour,minu,temp[110];

	Kevinew();
	scanf("%d\n",&ncase);
	for(icase=0;icase<ncase;icase++) {
	
		ans1 = ans2 = 0;
		scanf("%d%d%d\n",&T,&NA,&NB);
		for (i=0;i<NA;i++)
		{ 
			scanf("%d:%d",&hour,&minu);
			A[i].start=hour*60+minu;
			scanf("%d:%d",&hour,&minu);
			A[i].end=hour*60+minu;
			A[i].flage = A[i].flags = 0;
		}
		qsort(A,NA,sizeof(A[0]),cmp); 
	//	sort(A,A+NA);

		for ( i=0;i<NB;i++ )
		{
			scanf("%d:%d",&hour,&minu);
			B[i].start=hour*60+minu;
			scanf("%d:%d",&hour,&minu);
			B[i].end=hour*60+minu;
			B[i].flage = B[i].flags = 0;
		}
	//	sort(B,B+NB);
		qsort(B,NB,sizeof(B[0]),cmp); 

		for (i=0;i<NA;i++)
		{
			for (j=0;j<NB;j++)
			{
				if ( (B[j].start-A[i].end)>= T  && A[i].flage==0 && B[j].flags==0)
				{
					A[i].flage = 1; B[j].flags = -1;
				}
			}
		}
		for (i=0;i<NB;i++)
		{
			for (j=0;j<NA;j++)
			{
				if (A[j].start-B[i].end  >=  T && B[i].flage==0 && A[j].flags==0)
				{
					B[i].flage = 1; A[j].flags = -1;
				}
			}
		}

		for (i=0;i<NA;i++) {
			if ( A[i].flags == 0 ) ans1++;
		}
		for (i=0;i<NB;i++) {
			if ( B[i].flags == 0 ) ans2++;
		}



		printf("Case #%d: %d %d\n",icase+1,ans1,ans2);

	}

	return 0;

}


