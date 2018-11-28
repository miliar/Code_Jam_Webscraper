#include<iostream>
#include<fstream>
#include<cstring>
#include<iomanip>
using namespace std;
int main()
{
	int N;
	int i,j,k;
	ifstream fin("C-small-attempt1.in");
	ofstream fout("C.out");
	fin>>N;
	char str[501];
	char wel[]="welcome to code jam";
	int dp[500][19];
	int len;
	fin.getline(str,2);
	for(i=0;i<N;++i)
	{
		for(j=0;j<500;++j)
			for(k=0;k<19;++k)
				dp[j][k]=0;
		//cin.getline(str,500);
		//cout<<str;
		//cout<<strlen(str);
		fin.getline(str,500);
		cout<<strlen(str)<<endl;
		len=strlen(str);
		j=len-1;
		while(j>=0 && str[j--]!='m');
		if(str[j+1]=='m')
		{
			dp[j+1][18]=1;
		}
		for(;j>=0;--j)
		{
			for(k=0;k<19;++k)
			{
				dp[j][k]=dp[j+1][k];
				if(str[j]=='m' && k==18)
					dp[j][k]++;
				
				else if(str[j]==wel[k])
				{
					dp[j][k]+=dp[j+1][k+1];
					dp[j][k]%=1000;
				}
			}
		}
		fout<<"Case #"<<(i+1)<<": "<<setfill('0')<<setw(4)<<dp[0][0]<<resetiosflags(ios_base::scientific)<<endl;
	}
	return 0;
}
				
			
		
		
