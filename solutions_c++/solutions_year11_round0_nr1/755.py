#include<iostream>
using namespace std;
int main()
{
	int T;
	int N;
	int i;
	int j = 1;
	int temp;
	char robot;
	char last;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	while(j <= T)
	{
		cin>>N;
		int o = 1;
		int b = 1;
		int result = 0;
		int oo = 0;
		int bb = 0;
		for( i = 0; i < N;i++)
		{
			cin>>robot;
			int l = 0;
			if(robot == 'O')
			{
				cin>>temp;
				if(abs(temp - o) > bb)
				{
					result += abs(temp - o) - bb + 1;
					l = abs(temp - o) - bb + 1;
					o = temp;
				}
				else
				{
					result += 1;
					l = 1;
					o = temp;
				}
				oo += l;
				bb = 0;
			}
			else
			{
				cin>>temp;
				if(abs(temp - b) > oo)
				{
					result += abs(temp - b) - oo + 1;
					l = abs(temp - b) - oo + 1;
					b = temp;
				}
				else
				{
					result += 1;
					l = 1;
					b = temp;
				}
				bb += l;
				oo = 0;
			}
			if( i > 0)
			{
				last = robot;
			}
		}
		cout<<"Case #"<<j<<": "<<result<<endl;
		j++;
	}
	return 0;
}