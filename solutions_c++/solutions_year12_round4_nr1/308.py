#include<iostream>
#include<algorithm>

using namespace std;

int d[10000];
int l[10000];
int D,n;

int lowest[10000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>d[i]>>l[i];
			lowest[i]=-1;
		}
		cin>>D;

		bool found = false;

		lowest[0] = d[0];

		for(int i=0;i<n;i++)
		{
			if (D-d[i]<=lowest[i]) { found = true; break; }
			for(int j=i+1;j<n;j++)
			{
				if (d[j]-d[i]>lowest[i]) break;

				int best = lowest[i];
				if (best>l[j]) best = l[j];
				if (best>d[j]-d[i]) best = d[j]-d[i];

				if (lowest[j]==-1) lowest[j] = best;
				else lowest[j] = max(lowest[j], best);
			}
		}

		printf("Case #%d: %s\n", tt, found?"YES":"NO");
	}
	return 0;
}
