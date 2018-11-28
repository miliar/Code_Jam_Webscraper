#include<iostream>
using namespace std;

int main()
{
	int T, icase;
	
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	int N, K, ans;
	cin>>T;
	icase = 1;
	while(T--)
	{
		cin>>N>>K;
		int  t = 1<<N;
		
		cout<<"Case #"<<icase++<<": ";
		if(K % t == t-1)cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}
	
	return 0;
}
