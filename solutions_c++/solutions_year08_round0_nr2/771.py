#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;
struct sch{
      int begin,end;
	  int from; 
};
bool com(sch a,sch b)
{
	if(a.begin<b.begin) return true;
	else if(a.begin==b.begin&&a.end<b.end) return true;
	else return false;
}
int main()
{
	int ctest;
	int test;
	sch A[202];

	scanf("%d",&test);
	for(ctest=1;ctest<=test;ctest++)
	{
		int T;
		int flag=0;
		scanf("%d",&T);
		int m,n;
		scanf("%d %d",&m,&n);
		int i,j;
		for(i=0;i<m;i++)
		{
              int a,b,c,d;
			  scanf("%d:%d %d:%d",&a,&b,&c,&d);
			  A[i].begin=a*60+b;
			  A[i].end=c*60+d;
			  A[i].from=1;
		}
		for(i=0;i<n;i++)
		{
			int a,b,c,d;
			scanf("%d:%d %d:%d",&a,&b,&c,&d);
			A[i+m].begin=a*60+b;
			A[i+m].end=c*60+d;
			A[i+m].from=2;
		}
        sort(A,A+m+n,com);
							/*
							for(i=0;i<m+n;i++)
																				printf("%d %d %c\n",A[i].begin,A[i].end+T,A[i].from+'A'-1);	
											*/
							
		int count1=0,count2=0;
		int nowa[105],nowb[105];
		nowa[0]=nowb[0]=0;
		for(i=1;i<105;i++)
		{
			nowa[i]=nowb[i]=1000000;
		}
		for(i=0;i<m+n;i++)
		{
            int begin=A[i].begin;
			
			if(A[i].from==1)
			{
				 flag=0;
                 for(j=1;j<=nowa[0];j++)
				 {
					 if(nowa[j]+T<=begin)
					 {
						 nowa[j]=100000;
						 sort(nowa+1,nowa+nowa[0]+1);
						 nowa[0]--;
						 
						 nowb[0]++;
						 nowb[nowb[0]]=A[i].end;
						 flag=1;
						 break;
					 }                 
					 
				 }
				 if(flag==0)
				 {
					 count1++;
					 nowb[0]++;
					 nowb[nowb[0]]=A[i].end;
				 }				 
			}
			else
			{
				flag=0;
				for(j=1;j<=nowb[0];j++)
				{
					if(nowb[j]+T<=begin)
					{
						
						nowb[j]=100000;
						sort(nowb+1,nowb+nowb[0]+1);
						nowb[0]--;
						nowa[0]++;
						nowa[nowa[0]]=A[i].end;
						flag=1;
						
						break;
					}                 
					
				}
				if(flag==0)
				{
					count2++;
					nowa[0]++;
					nowa[nowa[0]]=A[i].end;
				}			
			}
		}
		printf("Case #%d: %d %d\n",ctest,count1,count2);

	}
}