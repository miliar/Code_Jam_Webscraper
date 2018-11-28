#include<stdio.h>
#include <iostream>
#include <queue>

using namespace std;
FILE *fin=fopen("large.in","r");
FILE *fout=freopen("outputlarge.out","w",stdout);
int main ()
{
	long long int R,N,k,i,j,h,temp,no,sum,ans,K,B,T;
	long long int x[50];
	long long int v[50];
	long long int dist[50];
	long long int swap[50];
	
	fscanf(fin,"%lld",&no);
//	prlong long intf("%lld" ,no);
	for(h=0;h<no;h++)
	{
                    // prlong long intf("%lld\n", h); 
                     fscanf(fin,"%lld %lld %lld %lld",&N,&K,&B,&T);
                     for(i=0;i<50;i++)
                     {
                                     x[i]=v[i]=dist[i]=swap[i]=0;
                     }
                     for(i=0;i<N;i++)
                     {
                                     fscanf(fin,"%lld",&x[i]);
                     }
                     for(i=0;i<N;i++)
                     {
                                     fscanf(fin,"%lld",&v[i]);
                     }
                     for(i=0;i<N;i++)
                     {
                                     dist[i]=x[i]+(v[i]*T);
                     }
                     long long int count=0;
                     long long int count1=0;
                     for(i=N-1;i>=0;i--)
                     {
                                        if(dist[i]>=B)
                                        count++;
                                        else
                                        count1++;
                                        if(dist[i]>=B)
                                        swap[i]=count1;
                     }                  
                     if(count<K)
                     {
                     printf("Case #%lld: IMPOSSIBLE\n",h+1);   
                     continue;
                     }
                     long long int count2=0;
                     long long int sum=0;
                     for(i=N-1;i>=0;i--)
                     {
                                        if(count2<K)
                                        {
                                                       if(dist[i]>=B)
                                                       {
                                                                     count2++;
                                                                     sum=sum+swap[i];
                                                                     //printf("%lld %lld %lld\n",sum,count2,dist[i]);      
                                                       }
                                        }
                     }                             
                     printf("Case #%lld: %lld\n",h+1,sum);                                                
                                                       
                                        
                                        
                                        
                                   /*     
                                        
                     for(i=0;i<N;i++)
                     {
                                    printf("%lld ",dist[i]);
                     }
                      for(i=0;i<N;i++)
                     {
                                    printf("\n\n%lld %d",swap[i]);
                     }
                     
		
		*/
		
		
		
		
	}	
	
	
	/*
		long long int jj;
	scanf("%lld",&jj);*/
	return 0;
}
		
	
	
	
