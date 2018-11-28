#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int L,D,N;
int word[5001][16];
int lim[501][16];

bool fit(int Lm,int Wd)
{
	for(int i=1;i<=L;i++)
		if((word[Wd][i] & lim[Lm][i]) == 0)
			return false;
	return true;
}

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	memset(word,0,sizeof(word));
	memset(lim,0,sizeof(lim));
	cin>>L>>D>>N;
	for(int i=1;i<=D;i++)
	{
		string t;
		cin>>t;
		for(int j=1;j<=L;j++)
			word[i][j] = (1<<(t[j-1] - 'a'));
	}
	for(int i=1;i<=N;i++)
	{
		string t;
		cin>>t;
		int z=0;
		for(int j=1;j<=L;j++)
		{
			if('a' <= t[z] && t[z] <= 'z')
				lim[i][j] += (1<<(t[z] - 'a')) , z++;
			else
			{
				z++;
				while(t[z] != ')')
				{
					lim[i][j] += (1<<(t[z] - 'a'));
					z++;
				}
				z++;
			}
		}
	}
	for(int i=1;i<=N;i++)
	{
		int s=0;
		for(int j=1;j<=D;j++)
			if(fit(i,j))
				s++;
		cout<<"Case #"<<i<<": "<<s<<endl;
	}
	return 0;
}
