#include <iostream>
#include <string>
#include <set>

using namespace std;

int t, a, b;
int adigits[7];
int bdigits[7];
int num[7];
int store[2000005];
set<int> numset;


void main()
{
	freopen("C-large.in","r",stdin);
	freopen("c2.out","w",stdout);

	scanf("%d",&t);
	int c=1;
	while(t--)
	{
		scanf("%d%d",&a,&b);

		int digit=0;
		int ans = 0;

		for(int idd=a;idd<b;idd++)
		{
			int digit=0;
			int i = idd;
			while(i>0)
			{
				num[digit++]=i%10;i=i/10;
			}
			numset.clear();
			for(int k=0;k<digit-1;k++)
			{
				if(num[k]>=num[digit-1])
				{
					int tmp=0;
					for(int ii=k;ii>=0;ii--)
					{
						tmp*=10;tmp+=num[ii];
					}
					for(int ii=digit-1;ii>k;ii--)
					{
						tmp*=10;tmp+=num[ii];
					}
					if(tmp>idd && tmp<=b) numset.insert(tmp);
				}
			}
			ans += numset.size();
		}

		cout << "Case #" << c++ << ": " << ans << endl;
	}
}