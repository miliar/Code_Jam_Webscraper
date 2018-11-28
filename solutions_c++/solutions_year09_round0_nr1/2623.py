#include<iostream>
#include<string>
using namespace std;

string w[5005];
int L,D,N;


int f[20];
string ss;

int work()
{
	cin>>ss;
	int tp = 0;
	for(int i=0;i<L;i++)
	{
		if( ss[tp]!='(' )
		{
			f[i] = 1<<(ss[tp]-'a');
			tp++;
		}else
		{
			f[i] = 0;
			while( ss[++tp]!=')' )
				f[i]|=(1<<(ss[tp]-'a'));
			tp++;
		}
	}

	int ans = D;
	for(int i=0;i<D;i++)
	for(int j=0;j<L;j++) if( (f[j]&(1<<(w[i][j]-'a')))==0 )
	{
		ans--;
		break;
	}
	return ans;
}
int main()
{
	freopen("A1.in","r",stdin);
	freopen("A1.out","w",stdout);

	cin>>L>>D>>N;
	for(int i=0;i<D;i++) cin>>w[i];

	for(int i=1;i<=N;i++) cout<<"Case #"<<i<<": "<<work()<<endl;
	return 0;
}
