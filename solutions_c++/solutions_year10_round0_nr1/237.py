#include<iostream>
using namespace std;
typedef long long ll;

ll g[1005];
int start[1005];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t;
	cin>>t;
	int cas=1;
	while(t--)
	{
		int n,k;
		cin>>n>>k;
		k++;
		if(k%(1<<n)==0) cout<<"Case #"<<cas++<<": ON\n";
		else cout<<"Case #"<<cas++<<": OFF\n";
	}
	return 0;
}