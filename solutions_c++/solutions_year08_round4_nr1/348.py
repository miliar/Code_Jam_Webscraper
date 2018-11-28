#include<iostream>
#include<vector>

using namespace std;

typedef unsigned long UL;
typedef signed long SL;
typedef unsigned short US;
typedef signed short SS;

typedef unsigned char UC;

inline UC readuc()
{
	UL a;
	cin>>a;
	return a;
}

const UL inv=numeric_limits<UL>::max();

int main()
{
	UL tests;
	cin>>tests;
	for(UL tt=1; tt<=tests; ++tt)
	{
		UL M;
		UC V;
		cin>>M;
		V=readuc();
		vector<UL> G(M);
		vector<UC> C(M);
		for(UL i=0; i<(M-1)/2; ++i)
		{
			cin>>G[i];
			C[i]=readuc();
		}
		vector<UL> m[2]={vector<UL>(M), vector<UL>(M)};
		for(UL i=(M-1)/2; i<M; ++i)
		{
			UC z=readuc();
			m[z][i]=0;
			m[!z][i]=inv;
		}
		for(UL ii=(M-1)/2; ii>0; --ii)
		{
			const UL cur=ii-1;
			const UL chi1=2*cur+1, chi2=2*cur+2;
			m[0][cur]=m[1][cur]=inv;
			for(UC a1=0; a1<=1; ++a1)
				for(UC a2=0; a2<=1; ++a2)
					if(m[a1][chi1] != inv && m[a2][chi2] != inv)
					{
						UC z=(G[cur]? (a1&&a2) : (a1||a2));
						m[z][cur]=min(m[z][cur], m[a1][chi1]+m[a2][chi2]);
						if(C[cur])
						{
							z=(!G[cur]? (a1&&a2) : (a1||a2));
							m[z][cur]=min(m[z][cur], m[a1][chi1]+m[a2][chi2]+1);
						}
					}
		}
		cout<<"Case #"<<tt<<": ";
		if(m[V][0]!=inv)
			cout<<m[V][0];
		else
			cout<<"IMPOSSIBLE";
		cout<<'\n';
	}
}
