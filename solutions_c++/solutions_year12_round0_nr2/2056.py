#include <iostream>

using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	short int base[100],rem[100],total[100];

	int tc;
	cin >> tc;
	for (int t=0;t<tc;t++)
	{
		int n; cin >> n;
		int s; cin >> s;
		int p; cin >> p;
		int res=0;
		for (int i=0;i<n;i++)
		{
			cin >> total[i];
			base[i]=total[i]/3;
			rem[i]=total[i]-base[i]*3;
		};
		for (int i=0;i<n;i++)
		{
			if ((base[i]>=p) ||
			   ((base[i]==(p-1)) && rem[i] )) {res++;continue;};

			if ((base[i]==(p-2))&&
				(rem[i]==2)		&&
				(s))					{res++;s--;continue;};
			if ((base[i]==(p-1))&&
				(rem[i]==0)		&&
				(s) && base[i])			{res++;s--;continue;};
		};
		printf("Case #%d: %d\n",t+1,res);
	};

	return 0;
};