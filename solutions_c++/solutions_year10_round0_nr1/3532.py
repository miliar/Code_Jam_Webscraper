#include<stdio.h>
#include<math.h>

using namespace std;

int main()
{
//	freopen("A-small.in","r",stdin);freopen("A-large.out","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.ans","w",stdout);
	int tc;
	
	bool chu[24]={0};
	
	int k,K,N,ff[24],ding=1;
	
	                                                                                    scanf("%d",&tc);
	for(int i=0;i<24;i++)
	
	
	
	ff[i]=(int)pow(2,i);
	//asdasdasssssssssssssssssssssssssssss
	for (int papa=1;papa<=tc;papa++)
	{//asdasdasssssssssssssssssssssssssssss
	                                                                                                    	printf("Case #%d: ",papa);
		scanf("%d%d",&N,&K);//asdasdasssssssssssssssssssssssssssss
		//asdasdasssssssssssssssssssssssssssss
		int lala=23;
	                                                              	int k=K;
		
	        	while(lala>=0 && k>0)
		{//asdasdasssssssssssssssssssssssssssss
                   if(ff[lala]<=k)
                   {chu[lala]=1;
                  //asdasdasssssssssssssssssssssssssssss
                   k=k-ff[lala];//asdasdasssssssssssssssssssssssssssss
                   }
                   lala--;
         }
	     	for(int i=0;i<N;i++)
		
        if(chu[i]==0)//asdasdasssssssssssssssssssssssssssss
		ding=0;
	           	if(ding)
		printf("ON\n");//asdasdasssssssssssssssssssssssssssss
		
        else//asdasdasssssssssssssssssssssssssssss
	    	printf("OFF\n");
		
        for(int i=0;i<24;i++)
	    	chu[i]=0;//asdasdasssssssssssssssssssssssssssss
		ding=1;
		
	}
	return 0;
}
