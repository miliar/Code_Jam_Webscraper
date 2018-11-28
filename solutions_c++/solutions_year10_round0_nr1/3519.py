#include<stdio.h>
#include<math.h>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large.ans","w",stdout);
	int testcase;
	bool aa[24]={0};
	int k,K,N,ss[24],flag=1;
	scanf("%d",&testcase);
	for(int i=0;i<24;i++)
	ss[i]=(int)pow(2,i);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d%d",&N,&K);
		int t=23;
		int k=K;
		//printf("hii");
		while(t>=0 && k>0)
		{
                   if(ss[t]<=k)
                   {aa[t]=1;
                   //printf("\n\tt=%d   k=%d\n",t,k);
                   k=k-ss[t];
                   }
                   t--;
         }
		for(int i=0;i<N;i++)
		if(aa[i]==0)
		flag=0;
		if(flag)
		printf("ON\n");
		else
		printf("OFF\n");
		for(int i=0;i<24;i++)
		aa[i]=0;
		flag=1;
		
	}
	return 0;
}
