#include <iostream>
#include <string>

using namespace std;

int T;
int S, N, P;

int s8, n8;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	cin>>T;
	for(int i=0; i<T; i++)
	{
		printf("Case #%d: ", i+1);
		cin>>N>>S>>P;
		n8=0;
		s8=0;
		for(int j=0; j<N; j++)
		{
			int a;
			cin>>a;
			if (a>=3*P-2) n8++; else
			if (P>1 && a>=3*P-4) s8++;
		}
		cout<<n8+min(s8, S)<<endl;
	}

	fclose(stdout);
}