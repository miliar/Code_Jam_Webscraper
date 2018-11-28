#include<iostream>
using namespace std;
char ori[1000];
int cnt[1000][30];
const char goal[]="welcome to code jam";
int main()
{
	int t;
	freopen("out.txt","w",stdout);
	cin>>t;
	cin.getline(ori,1000);
	for (int i=1;i<=t;i++)
	{
		cin.getline(ori,1000);
		memset(cnt,0,sizeof(cnt));
		int len=strlen(ori);
		for (int j=len-1;j>=0;j--)
		{
			if (ori[j]=='m') cnt[j][18]++;
			for (int k=len-1;k>j;k--)
			{
				switch(ori[j])
				{
				case 'm':
					if (ori[k]=='e')
						cnt[j][5]+=cnt[k][6];
					break;
				case 'a':
					if (ori[k]=='m')
						cnt[j][17]+=cnt[k][18];
					break;
				case 'j':
					if (ori[k]=='a')
						cnt[j][16]+=cnt[k][17];
					break;
				case ' ':
					if (ori[k]=='j')
						cnt[j][15]+=cnt[k][16];
					if (ori[k]=='c')
						cnt[j][10]+=cnt[k][11];
					if (ori[k]=='t')
						cnt[j][7]+=cnt[k][8];
					break;
				case 'e':
					if (ori[k]==' ')
					{
						cnt[j][14]+=cnt[k][15];
						cnt[j][6]+=cnt[k][7];
					}
					if (ori[k]=='l')
						cnt[j][1]+=cnt[k][2];
					break;
				case 'd':
					if (ori[k]=='e')
						cnt[j][13]+=cnt[k][14];
					break;
				case 'o':
					if (ori[k]=='d')
						cnt[j][12]+=cnt[k][13];
					if (ori[k]==' ')
						cnt[j][9]+=cnt[k][10];
					if (ori[k]=='m')
						cnt[j][4]+=cnt[k][5];
					break;
				case 'c':
					if (ori[k]=='o')
					{
						cnt[j][11]+=cnt[k][12];
						cnt[j][3]+=cnt[k][4];
					}
					break;
				case 't':
					if (ori[k]=='o')
						cnt[j][8]+=cnt[k][9];
					break;
				case 'l':
					if (ori[k]=='c')
						cnt[j][2]+=cnt[k][3];
					break;
				case 'w':
					if (ori[k]=='e')
						cnt[j][0]+=cnt[k][1];
					break;
				default:
					break;
				}
			}
			for (int k=0;k<19;k++)
				if (cnt[j][k]>10000)
					cnt[j][k]%=10000;
		}
		int ans=0;
		for (int j=0;j<len;j++)
			if (ori[j]=='w')
				ans+=cnt[j][0];
		cout<<"Case #"<<i<<": ";
		for (int i=1000;i>1;i/=10)
		{
			int tmp=ans/i;
			cout<<tmp%10;
			ans%=i;
		}
		cout<<ans<<endl;
	}
}