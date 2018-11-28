#include<iostream>
#include<string>
#include<fstream>
using namespace std;

char t[201];
int lis[11],z;

int f(int n,int bas)
{
	int r=0;
	while(n)
	{
		r+=(n%bas)*(n%bas);
		n/=bas;
	}
	return r;
}

bool able[1000001][11];
bool done[1000001][11];

void inputit(string s)
{
	z=0;
	for(int i=0;i<s.length();i++)
		if(s[i]!=' ')
		{
			if(i<s.length()-1  &&  s[i+1]!=' ')
			{
				lis[++z]=(s[i]-'0')*10+s[i+1]-'0';
				++i;
			}
			else
				lis[++z]=s[i]-'0';
		}
	
}

bool check(int n,int bas,int bad)
{
	if(done[n][bas])
		return able[n][bas];
	done[n][bas]=1;
	int t=f(n,bas);
	if(t == bad)
		able[n][bas]=0;
	else
		able[n][bas]=check(t,bas,bad);
	return able[n][bas];
}


bool AC(int u)
{
	for(int i=1;i<=z;i++)
		if(!check(u,lis[i],u))
			return false;
	return true;
}

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	memset(done,0,sizeof(done));
	for(int i=2;i<=10;i++)
		done[1][i]=1,able[1][i]=1;
	int T;
	cin>>T;
	cin.getline(t,200);
	for(int c=1;c<=T;c++)
	{
		cin.getline(t,200);
		string s = t;
		inputit(s);
		for(int i=2;;i++)
			if(AC(i))
			{
				cout<<"Case #"<<c<<": "<<i<<endl;
				break;
			}
	}
	return 0;
}
