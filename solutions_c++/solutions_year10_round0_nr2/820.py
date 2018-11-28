#include<iostream>
#include<cstdlib>
using namespace std;

int gcd(int a, int b)
{
	if(a%b == 0) return b;
	return gcd(b, a%b);
}


int main()
{
	int T, icase;
	
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("B-small-attempt2.out", "w", stdout);
	
	cin>>T;
	icase = 1;
	int n;
	int num[10];
	int i;
	while(T--)
	{
		cin>>n;
		int tmp;
		int min = 1E8+1;
		for( i = 0; i < n; i++)
		{
			cin>>num[i];
			if(min > num[i]) min = num[i];
		}
		for( i = 0; i < n; i++)
			num[i] -= min;
		int tg;
		for(i = 0; i < n; i++)
			if(num[i] > 0) 
			{
				tg = num[i];
				break;
			}
		//cout<<tg<<endl;
		for(; i < n; i++)
			if(num[i] > 0)
			{ 
				tg = gcd(num[i], tg);
			}
		
		cout<<"Case #"<<icase++<<": ";
		tmp = num[0] + min;
		if(0 == tmp % tg)cout<<"0"<<endl;	
		else cout<<(tg - tmp%tg)<<endl;
	}
	return 0;
}
