
#define MX 2007
#define PI 3.141592653589793238462643383279  
#define INF 100000000
#include<iostream>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<string.h>
#include<queue>
using namespace std;


#define e 2.718281828459 


char a[1000];
int temp[1000];
int O[1000],Y[1000],proo[1000],prob[1000];
int main()
{	
	freopen("V.txt","w",stdout);
	int T;
	int sum,t,i,an,o,b,j,ost,bst;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
		{	
			memset(proo,0,sizeof(proo));
			memset(prob,0,sizeof(prob));
			memset(O,0,sizeof(O));
			memset(Y,0,sizeof(Y));
			memset(temp,0,sizeof(temp));
			memset(a,0,sizeof(a));
			scanf("%d",&an);
			for(o=0,b=0,i=1;i<=an;i++)	
				{
					scanf("%s %d",&a[i],&temp[i]);
					if(a[i]=='O')
						{O[++o]=temp[i];proo[o]=i;}
					else
						{Y[++b]=temp[i];prob[b]=i;}
				}
			for(sum=0,bst=1,ost=1,i=1,j=1;;)
				{
					if(i>o||j>b)
					{
						if(i>o&&j>b)
							break;
						else if(i>o)//onlyb
						{
							sum+=abs(Y[j]-bst)+1;
							bst=Y[j];
							j++;
						}
							
						else 
						{
							sum+=abs(O[i]-ost)+1;
							ost=O[i];
							i++;
						}
					}

					else
					{
					if(proo[i]<prob[j])
						{
							sum+=abs(O[i]-ost)+1;
							
							if(abs(O[i]-ost)+1>=abs(Y[j]-bst))
								bst=Y[j];
							else
								{
									if(Y[j]-bst>0)
										bst+=abs(O[i]-ost)+1;
									else
										bst-=abs(O[i]-ost)+1;
								}
							ost=O[i];
							i++;
						}
					else
						{

							sum+=abs(Y[j]-bst)+1;
							
							if(abs(Y[j]-bst)+1>=abs(O[i]-ost))
								ost=O[i];
							else
								{
									if(O[i]-ost>0)
										ost+=abs(Y[j]-bst)+1;
									else
										ost-=abs(Y[j]-bst)+1;
								}
							bst=Y[j];
							j++;

						}
					}
				
				
				
				
				}
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
			
		printf("Case #%d: %d\n",t,sum);
	
		}
	return 0;
}