#include<iostream>
#include<map>
#include<vector>
#include<string>
using namespace std;

long long a[100000];
long long b[100000];
int c[23423];
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	cin>>zu;
	for(int Cas =1 ; Cas<=zu;Cas++)
	{
		printf("Case #%d: ",Cas);
		int m,n,d,t;
		cin>>m>>n>>d>>t;
		for(int i=0;i<m;i++)
		{
			cin>>a[i];
		}
		int ge =0;
		for(int i=0;i<m;i++)
		{
			cin>>b[i];
			if(b[i]*t>=d-a[i])
				c[i]=1,ge++;
			else
				c[i]=0;
		}
		if(ge<n)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			int bu=0;
			int index=-1;
			int rr =0;
			for(int i=m-1;i>=0;i--)
			{
				if(c[i]==0)
				{
					index=i;
					break;
				}

				rr++;
			}
			if(rr>=n)
			{
				cout<<0<<endl;
				continue;
			}
			int zero = 1;
			int head= index,tail = index;
			for(;rr<n;)
			{
				if(c[head-1]==0)
				{
					head--;
				}
				else
				{
					bu+=tail-head+1;
					head--;
					tail--;
					rr++;
				}
			}
			cout<<bu<<endl;
		}
	}
}