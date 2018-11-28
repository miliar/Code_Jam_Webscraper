#include <iostream>

using namespace std;

char c;
char num[22];

int main()
{
    FILE* in = freopen("B-large.in", "r", stdin);
    FILE* out = freopen("B-large.out", "w+", stdout);

	int tests = 0;
	cin>>tests;

	for(int t=1; t<=tests;++t)
	{
		scanf("%c",&c);
		while(c<'0' || c>'9') scanf("%c",&c);

		int nc = 0;
		while(c>='0' && c<='9' && !feof(in))
		{
			num[nc++] = c;
			scanf("%c",&c);
		}
		num[nc] = 0;

		int pos = nc-1;
		char max = num[pos];
		while(pos>=0 && max<=num[pos])
		{
			max=num[pos];
			pos--;
		}
		cout<<"Case #"<<t<<": ";
		if(pos==-1)
		{
			int p = nc-1;
			while(num[p] == '0') p--;
			cout<<num[p];
			cout<<'0';
			for(int i = nc-1;i>=0;i--)
			{
				if(i!=p)
					cout<<num[i];
			}
		}
		else
		{
			char min = max;
			int pmin = pos+1;
			for(int i=pos+1;i<nc;i++)
			{
				if(num[pos]<num[i] && num[i]<min)
				{
					min = num[i];
					pmin = i;
				}
			}
			char temp = num[pos];
			num[pos] = num[pmin];
			num[pmin] = temp;

			for(int i=pos+1;i<nc;i++)
			{
				for(int j=i+1;j<nc;j++)
				{
					if(num[i] > num[j])
					{
						temp = num[i];
						num[i] = num[j];
						num[j] = temp;
					}
				}
			}
			for(int i=0;i<nc;i++)
			{
				cout<<num[i];
			}
		}
		cout<<"\n";
	}

	//cout<<"Hello world";
	return 0;
}