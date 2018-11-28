#include<iostream>
#include<string>
using namespace std;
string ba="welcome to code jam";
string que;
long long n,mem[501][19];

long long solve(int p1, int p2)
{
		if(p2==19)
		return 1;
	if(p1==que.size())
		return 0;
	if(mem[p1][p2]!=-1)
		return mem[p1][p2];

	long long x=0;

	if(que[p1]==ba[p2])
		x+=solve(p1+1,p2+1);
	x+=solve(p1+1,p2);
	mem[p1][p2]=x%10000;
	return mem[p1][p2];
}

int main()
{
	freopen("Cl.in","r",stdin);
	freopen("y.out","w",stdout);
	long long res;
	cin>>n;
	cin.get();
	for(int i=0;i<n;i++)
	{
		getline(cin,que);
		memset(mem,-1,sizeof(mem));
		res=solve(0,0);
		res=res%10000;
		cout<<"Case #"<<i+1<<": ";

		if(res<1000)
			cout<<"0";
		if(res<100)
			cout<<"0";
		if(res<10)
			cout<<"0";
		cout<<res<<endl;
	}
	return 0;
}