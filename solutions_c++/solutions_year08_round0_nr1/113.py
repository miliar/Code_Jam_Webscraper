#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
#define MIN(a,b) ( (a) < (b) ? (a) : (b) )
#define MAX(a,b) ( (a) > (b) ? (a) : (b) )
string arr[101];
string q[1001];
int mem[1001][101];
int main()
{
	int N;
	
	int ind=0;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	cin>>N;
	while(N)
	{
		N--;
		ind++;
		memset(mem,0,sizeof(mem));
		int S;
		cin>>S;
		int i,j,k;
		string ts;
		getline(cin,ts);
		for(i=0;i<S;i++)
		{
			getline(cin,ts);
			arr[i]=ts;
		}
		int Q;
		cin>>Q;
		getline(cin,ts);
		for(i=0;i<Q;i++)
		{
			getline(cin,ts);
			q[i]=ts;
		}
		int res=10000;
		for(i=1;i<=Q;i++)
		{
			for(j=0;j<S;j++)
				if(arr[j]==q[i-1])break;
			for(k=0;k<S;k++)mem[i][k]=mem[i-1][j]+1;
			mem[i][j]=10000;
			for(k=0;k<S;k++)
			{
				if(k==j)continue;
				mem[i][k]=MIN(mem[i][k],mem[i-1][k]);
			}
			
		}
		for(i=0;i<S;i++)res=MIN(res,mem[Q][i]);
		cout<<"Case #"<<ind<<": "<<res<<endl;
	}
	return 0;
}