#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
using namespace std;

typedef long long LL;

int A[1005];
int next[1005];
int cont[1005];
int index[1005];
int cycle[1005];

int main()
{
	ifstream fin;
	fin.open("C:\\data\\C.in");
	ofstream fout;
	fout.open("C:\\data\\C.out");

	int n;
	fin>>n;
	for(int i=1;i<=n;++i)
	{
		memset(next,255,sizeof(next));
		memset(cont,0,sizeof(cont));
		memset(cycle,0,sizeof(cycle));
		memset(index,255,sizeof(index));
		fout<<"Case #"<<i<<": ";
		int N,K,R;
		fin>>R>>K>>N;
		for(int j=0;j<N;++j)fin>>A[j];
		for(int j=0;j<N;++j)
		{
			int sum=0;
			int s=j;
			bool done=false;
			while(s!=j || !done)
			{
				if(A[s]+sum<=K)
				{
					sum+=A[s];
					s=(s+1)%N;
					done=true;
				}
				else
				{
					break;
				}
			}
			if(!done)
			{
				next[j]=-1;
				cont[j]=0;
			}
			else
			{
				next[j]=s;
				cont[j]=sum;
			}
		}
		int turns=0;
		LL ret=0;
		int k=0;
		while(turns<R)
		{
			if(next[k]==-1)break;
			if(index[k]==-1)
			{
				index[k]=turns;
				cycle[k]=ret;
				ret+=cont[k];
				k=next[k];
				turns++;
			}
			else
			{
				int len=turns-index[k];
				LL add=ret-cycle[k];
				int left=R-turns;
				ret+=add*(left/len);
				turns=R-(left%len);
				while(turns<R)
				{
					ret+=cont[k];
					turns++;
					k=next[k];
				}
			}
		}
		fout<<ret<<endl;
	}
	return 0;
}