#include <iostream>
#include <vector>
using namespace std;
bool on[32];
 
int T,N,K;
int main()
{
    scanf("%d",&T);
    
    for(int t=1;t<=T;t++)
    {
		scanf("%d %d",&N,&K);
		memset(on,0,32);
		for(int i=1;i<=K;i++)
		{
				int tl = 1;
				while(on[tl] && tl<=N)  tl++;
				tl = min(tl,N);
				while(tl>0) on[tl--]^=1;
				
				//			cout<<i<<":";
					//for(int dae = 1 ;dae<=N;dae++)cout<<(int)on[dae];
					//	cout<<endl;
		}
		
		char ans=0;
			for(int d=1;d<=N;d++)
					if(!on[d]) ans ='n';
				if(ans==0) ans ='y';
				
			printf("Case #%d: %s\n",t,(ans =='y')? "ON" : "OFF"); 
	}
}
