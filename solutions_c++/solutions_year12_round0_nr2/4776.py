#include "iostream"
#include "cstdio"
#include "string.h"
#include "cmath"
using namespace std;
int B[110],Sur[110],both[110],T[110],F[110];
int main()
{
	int test;
	cin>>test;
	int t,a,b,c,N,S,P,i,res;
	for(t=1;t<=test;t++)
	{
		cin>>N>>S>>P;
		for(i=0;i<N;i++)cin>>T[i];
		printf("Case #%d: ",t);
		memset(B,0,sizeof B);
		memset(both,0,sizeof both);
		memset(Sur,0,sizeof Sur);
		for(a=10;a>=0;a--){
			for(b=a;b>=a-2&&b>=0;b--){
				for(c=b;c>=b-2 && c>=a-2 &&c>=0;c--){
					
					for(i=0;i<N;i++){
						if(T[i]==a+b+c){
							if(a>=P){
								if(abs(a-b)==2 || abs(a-c)==2 ||abs(b-c)==2)
									both[i]=true;
								else
									B[i]=true;
							}
							if(abs(a-b)==2 || abs(a-c)==2 ||abs(b-c)==2){
								if(a>=P)
									both[i]=true;
								else
									Sur[i]=true;
							}
							
						}
					}
				}
			}
		}
		memset(F,0,sizeof F);
		res=0;
		
		for(i=0;i<N;i++){
			//cout<<Sur[i]<<" "<<B[i]<<" "<<both[i]<<endl;
			if(both[i] && S && !B[i]){
				S--;
				F[i]=true;
				res++;
			}
		}
		for(i=0;i<N;i++){
			if(!F[i] && both[i] && S && B[i]){
				S--;
				F[i]=true;
				res++;
			}
		}
		for(i=0;i<N;i++){
			if(!F[i] && S && Sur[i]){
				if(!B[i]){
					S--;
					F[i]=1;
				}
			}
		}
		for(i=0;i<N;i++){
			if(!F[i] && S && Sur[i]){
				S--;
				F[i]=1;
			}
		}
		if(!S){
			for(i=0;i<N;i++){
				if(!F[i] && B[i]){
					res++;
				}
			}
			printf("%d\n",res);
		}
		else {
			printf("0\n");
		}	
	}
	return 0;
}
