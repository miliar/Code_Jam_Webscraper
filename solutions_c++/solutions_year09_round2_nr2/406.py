#include <iostream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int tt,ttt,i,N,j;
	string S;
	scanf("%d",&tt);
	for(ttt=1;ttt<=tt;ttt++)
	{
		cout<<"Case #"<<ttt<<": ";
		cin>>S; S="0"+S;
		int N=S.size();
		for(i=N-2;i>=0;i--)
		if (S[i]<S[i+1]) break;
		for(j=N-1;j>i;j--) if (S[j]>S[i]) break;
		swap(S[i],S[j]);
		sort(S.begin()+i+1,S.end());
		if (S[0]=='0') cout<<S.substr(1)<<endl; else cout<<S<<endl;
	}
//	system("pause");
}
