#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

long long data[1000000];
int n;
int D, C;

int main(void)
{
	int T;
	cin>>T;
	for(int caseN=1;caseN<=T;caseN++)
	{
		cin>>C>>D;
		D*=2;
		n=0;

		for(int i=0;i<C;i++)
		{
			int P, V;
			cin>>P>>V;
			P*=2;
			for(int j=0;j<V;j++) data[n++]=P;
		}

		sort(data, data+n);

		long long s=0, e=1000000LL*1000000LL, mid;
		long long ans=-1;

		while(s<e)
		{
			mid=(s+e)/2;
			long long last=data[0]-mid;
			bool isAble=true;

			for(int i=1;i<n;i++)
			{
				long long cur=data[i];
				long long tar=last+D;
				if(cur>=tar)
				{
					if(cur-tar<=mid) last=tar;
					else last=cur-mid;
				}
				else
				{
					if(tar-cur<=mid) last=tar;
					else
					{
						isAble=false;
						break;
					}
				}
			}

			if(isAble)
			{
				if(ans==-1) ans=mid;
				else ans=min(ans, mid);
				e=mid;
			}
			else s=mid+1;
		}

		printf("Case #%d: %lld.%lld\n", caseN, ans/2, ans%2?5:0);
	}

	return 0;
}
