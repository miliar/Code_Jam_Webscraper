#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

template<class TT> 
inline TT gcd(TT a,TT b)  
{
	if(a<0)return gcd(-a,b);
	if(b<0)return gcd(a,-b);
	return (b==0)?a:gcd(b,a%b);
}

long long N, L, H;
long long a[10001];

int main()
{//
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small1.out", "w", stdout);
/*	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);*/

	int T;
	cin>>T;
	for(int t=1; t<=T; t++)
	{
		memset(a, 0, sizeof(a));
		cin>>N>>L>>H;
		cout<<"Case #"<<t<<": ";
		for(int i=0; i<N; i++)
			cin>>a[i];
		sort(a, a+N);
		long long k;
		bool flag=1;
		for(k=L; k<=H; k++)
		{	
			flag = 1;
			for(int i=0; i<N; i++)
			{
				if(k>=a[i])
				{
					if(k % a[i] != 0)
					{
						flag = 0;
						break;
					}
				}
				else 
				{
					if(a[i] %k != 0)
					{
						flag = 0;
						break;
					}
				}
			}
			if(flag)
				break;
		}
		if(!flag)
			cout<<"NO"<<endl;
		else cout<<k<<endl;
	}
//	while(1);
	return 0;
}