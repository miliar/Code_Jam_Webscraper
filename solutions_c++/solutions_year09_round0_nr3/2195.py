#include<iostream>
#include<string>
#include<vector>
using namespace std;
string s="welcome to code jam";
string S;
int dp[1000][30];
void print(int a)
{
	if(a<10)
	{
		cout<<"000"<<a<<"\n";
		return;
	}
	if(a<100)
	{
		cout<<"00"<<a<<"\n";
		return;
	}
	if(a<1000)
	{
		cout<<"0"<<a<<"\n";
		return;
	}
	cout<<a<<"\n";
}

int solve(int pos1,int pos2)
{   
	if(pos2==s.size())
		return 1;
	if(pos1==S.size())
		return 0;
	if(dp[pos1][pos2]!=-1)
		return dp[pos1][pos2];
	int res=0;
	if(S[pos1]==s[pos2])
		res=solve(pos1+1,pos2+1)%10000;
	res=(res+solve(pos1+1,pos2))%10000;
	dp[pos1][pos2]=res;
	return res;
}

int main()
{
    int n,i=0;
	cin>>n;
	getline(cin,S);
	while(i<n)
	{
		getline(cin,S);
		memset(dp,-1,sizeof(dp));
		printf("Case #%i: ",++i);
		print(solve(0,0));
	}
}


