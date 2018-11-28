#include <iostream>
#include <vector>
#include <string>
using namespace std;

void doIt()
{
	int N,L,H;
	cin>>N>>L>>H;
	int freqs[N];
	for (int n =0;n<N;n++)
		cin>>freqs[n];
	int occs[H+1];
	for (int j = L;j<H+1;j++)
		occs[j] = 0;
	for (int i = 0; i<N;i++)
		for (int j = L;j<H+1;j++)
			if ((j%freqs[i]==0)or (freqs[i]%j==0))
				occs[j]++;
	for (int j = L;j<H+1;j++)
		if (occs[j]==N)
		{
			cout<<j;
			return;
		}
	cout<<"NO";
	
	return;
}
int main()
{
	int T;
	cin>>T;
	for (int t = 1;t<=T;t++)
	{
		if (t>1) cout<<endl;
		cout<<"Case #"<<t<<": ";
		doIt();
	}
	return 0;
}