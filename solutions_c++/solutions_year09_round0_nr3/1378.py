#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
using namespace std;


char m[20]="welcome to code jam";
int dp[40][1000];

string int2str(int a)
{
	ostringstream os;
	os<<a;
	string k = os.str();
	while(k.size()<4) k='0'+k;
	return k;
}


int main()
{
	int C;
	cin>>C;
	char c[1000];
	cin.getline(c,1000);
	for(int v=0;v<C;v++)
	{
		
		cin.getline(c,1000);
		memset(dp,0,sizeof(dp));
		int L = strlen(c);
		for(int i=0;i<19;i++)
		{
			//start dp!
			for(int j=0;j<L;j++)
			{
				if(i==0) if(c[j]==m[i]) {dp[i][j]=1; continue;}
				if(c[j]!=m[i]) continue;
				for(int k=0;k<j;k++)
					dp[i][j]+=dp[i-1][k];
				dp[i][j]%=10000;
			}
		}
		int answer = 0;
		for(int i=0;i<L;i++) answer+=dp[18][i];
		answer%=10000;
		cout<<"Case #"<<v+1<<": "<<int2str(answer)<<endl;
	}
}
