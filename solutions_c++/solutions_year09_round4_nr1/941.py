

#include <iostream>

using namespace std;

char s[42];
int minrow[42];

int main()
{
    FILE* in = freopen("A-large.in", "r", stdin);
    FILE* out = freopen("A-large.out", "w+", stdout);

	int q;
	cin>>q;

	for(int t = 1;t<=q;t++)
	{
		int n;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			int min = 0;
			scanf("%s",s);
			for(int j=0;j<n;j++)
			{
				if(s[j] == '1')
					min = j;
			}
			minrow[i] = min;
		}
		int swaps = 0;
		for(int i=0;i<n;i++)
		{
			if(minrow[i] > i)
			{
				int j=i+1;
				for(;j<n;j++)
				{
					if(minrow[j] <= i)
						break;
				}
				do
				{
					int tmp = minrow[j];
					minrow[j] = minrow[j-1];
					minrow[j-1] = tmp;
					swaps++;
					j--;
				}
				while(j>i);
			}
		}

		cout<<"Case #"<<t<<": "<<swaps<<"\n";
	}


	return 0;
}

