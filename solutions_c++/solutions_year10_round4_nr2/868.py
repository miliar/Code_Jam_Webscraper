#include<iostream>
using namespace std;

#define MAXN 1100

int n,p,te,ans;
int M[MAXN];

bool Check(int l,int r)
{
	for(int i=l;i<=r;++i)
	{
       if(M[i]<p)
	   {
		   return false;
	   }
    }
	return true;
}

int Find(int l,int r)
{
    int ret=0;
    int mid=(l+r)>>1;
    if(!Check(l,r))
	{          
         ret++;
         for(int i=l;i<=r;++i)
		 {
            M[i]++;
         }
         ret=ret+Find(l,mid)+Find(mid+1,r);
    }
    return ret;
}

int main()
{
	freopen("Bs.in","r",stdin);
	freopen("Bs.txt","w",stdout);
	cin>>te;
	for(int ca=1;ca<=te;++ca)
	{
		cin>>p;
		n=(1<<p);
		for(int i=0;i<n;++i)
		{
			cin>>M[i];
		}
		for(int i=0;i<p;++i)
		{
			for(int j=0;j<(1<<(p-i-1));++j)
			{
				int tt;
				cin>>tt;
			}
		}
		ans=Find(0,n-1);

		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
