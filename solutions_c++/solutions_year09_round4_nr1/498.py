#include <iostream>
using namespace std;
#define INF 1000000000
string A[45];
int ret=INF;
int N;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int tt,ttt,i,j,k;
	cin>>tt;
	for(ttt=1;ttt<=tt;ttt++)
	{
		ret=0;
		cin>>N;
		for(i=0;i<N;i++) cin>>A[i];
		for(i=0;i<N;i++)
		{
			for(j=i;j<N;j++)
			{
				for(k=i+1;k<N;k++) if (A[j][k]=='1') break;
				if (k==N) break;
			}
			if (j==N) cout<<"error"<<endl; else
			if (j==i) continue; else
			{
				for(j=j;j>=i+1;j--) {swap(A[j],A[j-1]); ret++;}
			}
		}
		cout<<"Case #"<<ttt<<": "<<ret<<endl;
	}
//	system("pause");
	return 0;
}
