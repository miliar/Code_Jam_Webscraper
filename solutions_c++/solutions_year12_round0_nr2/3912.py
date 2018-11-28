#include <iostream>
using namespace std;

int main()
{
	int N;
	cin >> N;
	int a,b,c,d;
	int val;
	int ans = 0;
	int k = 0;
	for(int i = 0; i < N; i++)
	{
		cin >> a >> b >> c;
		val = 3*(c-1);
		for(int j = 0; j < a; j++)
		{
			cin >> d;
			if(d > val)
			{
				ans++;
			}
			else if(c == 1)
			{
				if( d > 1) ans++;
			}
			else if( d == val  || d == val-1)
			{
				k++;
			} 
		}
		if( k > b)
		{
			k = b;
		}
		ans = ans + k;
		cout <<"Case #"<< i+1<<": "<<ans<<endl;
		ans=k=0;
	}
	return 0;
}
