// joy
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<map>
using namespace std;
const int MAX=1000;

int N,S,P;
int a[MAX];
int main()
{
	int CN=0;
	int T;cin>>T;
	
	while(T--)
	{
		scanf("%d%d%d",&N,&S,&P);
		for(int i=1;i<=N;i++) scanf("%d",&a[i]);
		
		sort(&a[1],&a[N+1]);
		
		int ans=0;
		for(int i=N;i>=1;i--)
		{
			if(a[i]>=3*P-2) ans++;
			else
			{
				if(S)
				{
					if(a[i]>=3*P-4)
					{	
						int x=P,y=P-2,z=P-2;
						if(y<0) y=0;
						if(z<0) z=0;
						if(x+y+z<=a[i])
						{
							ans++;
							S--;
						}
					}
				}
			}
		}
		
		
		cout<<"Case #"<<++CN<<": "<<ans<<endl;
	}
	
	
	return 0;
}


