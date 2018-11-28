#include <iostream>
#include <string>
using namespace std;

int n,s,p;
int t,t1;

int ans;

int i,j,k;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin >> t;

	for(t1=1;t1<=t;t1++)
	{
		cin >> n >> s >> p;
		ans=0;
		for(i=0;i<n;i++)
		{
			cin >> k;
			if(k%3==0)
			{
				//k/3 k/3 k/3
				//k/3-1 k/3 k/3+1
				if(k/3>=p)
				{
					ans++;
				} else
				{
					if(k/3-1>=0 && k/3+1>=p && s>0)
					{
						ans++;
						s--;
					}
				}
			} else
			{
				if(k/3+1>=p)
				{
					ans++;
					continue;
				}

				if(k%3==2 && k/3>=0 && s>0 && k/3+2>=p)
				{
					ans++;
					s--;
				}
			}
		}
		cout << "Case #" << t1 << ": " << ans << "\n";
	}

	return 0;
}