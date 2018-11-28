#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;


int main()
{
	int T,N,L,H;
	int notes[1000],unotes[100];
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int flag=0;
		cin>>N>>L>>H;
		for(int i=0;i<N;i++)
			cin>>notes[i];
		cout<<"Case #"<<t+1<<": ";
		if(L==1)
		{
			cout<<"1"<<endl;
			continue;
		}
		sort(notes,notes+N);
		int k=0;
		unotes[0]=notes[0];
		for(size_t i = 1; i < N; ++i)
		{
			if(notes[i]!=unotes[k])
				unotes[++k]=notes[i];
		}
		k++;
		int j;
		long long prod,gcd,lcm;
		for(size_t i = L; i <= H; ++i)
		{
			for(j = 0; j < k; ++j)
			{
				if((unotes[j]%i) && (i%unotes[j]))
					break;
			}
			if(j==k)
			{
				cout<<i<<endl;
				flag=1;
				break;
			}
		}
		if(!flag)
			cout<<"NO"<<endl;
				
	}
	return 0;
}