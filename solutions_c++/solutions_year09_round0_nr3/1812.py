#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");
char w[20]={"welcome to code jam"};
char s[500];
class dshu
{
public:
	int a[4];
	dshu()
	{
		int i;
		for(i=0;i<=3;i++)a[i]=0;
	}
	dshu operator+(dshu B)
	{
		dshu C;
		int *b=B.a,*c=C.a;
		c[0]=a[0]+b[0];
		c[1]=a[1]+b[1]+c[0]/10;c[0]%=10;
		c[2]=a[2]+b[2]+c[1]/10;c[1]%=10;
		c[3]=a[3]+b[3]+c[2]/10;c[2]%=10;
		c[3]%=10;
		return C;
	}
};
int main()
{
	int n,i,j,k,slen;
	dshu dp[20][501];
	fin>>n;
	fin.getline(s,500);//消除数字后的换行
	for(i=0;i<=500;i++)dp[0][i].a[0]=1;
	for(k=1;k<=n;k++)
	{
		fin.getline(s,500);
		slen=strlen(s);
		
		for(j=1;j<=19;j++)
		{
			for(i=1;i<=slen;i++)
			{
				if(s[i-1]==w[j-1])dp[j][i]=dp[j][i-1]+dp[j-1][i-1];
				else dp[j][i]=dp[j][i-1];
			}
		}
		fout<<"Case #"<<k<<": ";
		for(i=3;i>=0;i--)fout<<dp[19][slen].a[i];
		fout<<endl;
	}


	return 0;
}