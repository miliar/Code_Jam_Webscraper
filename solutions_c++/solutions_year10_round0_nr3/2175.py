#include<iostream>
using namespace std;

int num[1000];

int main()
{
	int T, icase;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c.out", "w", stdout);
	cin>>T;
	int r, k, n;
	
	icase = 1;
	while(T--)
	{
		cin>>k>>r>>n;
		for(int i = 0; i < n; i++)
			cin>>num[i];
		int tot = 0;
		int t = 0;
		int i = 0;
		for(; i < n ; i++)
			if(t + num[i] <= r) t += num[i];	
			else break;
		k --;
		tot = t;
		while(k--)
		{
			t = 0;
			int cnt = 0;
			while(cnt < n)
			{
				if(t + num[i%n] <= r) 
				{
					t += num[i%n];
					i++;
					cnt++;
				}else break;
			}
			tot += t;
		}
		cout<<"Case #"<<icase++<<": "<<tot<<endl;
	}
	
	return 0;
}
/*

5
4 6 4
1 4 2 1

*/
