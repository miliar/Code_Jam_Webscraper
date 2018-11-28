#include <fstream>
#include <vector>
#include <string>
using namespace std;
ifstream cin("input.txt");
ofstream cout("output.txt");

int a[520][520];

int main()
{
	int T;
	cin>>T;
	for(int tn=1;tn<=T;tn++)
	{
		int n,m,r=0;
		cin>>m>>n;
		memset(a,0,sizeof a);
		for(int i=0;i<m;i++)
		{
			string str;
			cin>>str;
			for(int j=0;j<n/4;j++)
			{
				int t=(str[j]<='F' && str[j]>='A')?str[j]-'A'+10:str[j]-'0';
				for(int k=0;k<4;k++)
				{
					a[i][j*4+3-k]=t&1;
					t>>=1;
				}
			}
		}
		vector<int> v;
		v.assign(min(n,m),0);
		while(1)
		{
			int s=-1, sx=0,sy=0;
			for(int i=0;i<m;i++)
			{
				for(int j=0;j<n;j++)
				{
					if(a[i][j]<2)
					{
						int k=0;
						while(1)
						{
							int cx=i+k, cy=j+k;
							while(cx>=i)
							{
								if((((cx+k-i)&1)^(a[i][j]!=a[cx][j+k])) ||
									((cy+k-j)&1)^(a[i][j]!=a[i+k][cy]) || 
									a[cx][j+k]==2 || a[i+k][cy]==2)
								{
									goto no_chess;
								}
								cx--;
								cy--;
							}
							k++;
						}
no_chess:
						if(k>s)
						{
							s=k;
							sx=i;sy=j;
						}
					}
				}
			}
			if(s==-1)break;
			for(int i=0;i<s;i++)
			{
				for(int j=0;j<s;j++)
				{
					a[sx+i][sy+j]=2;
				}
			}
			if(v[s-1]==0)r++;
			v[s-1]++;
		}
		cout<<"Case #"<<tn<<": "<<r<<endl;
		int sum=0;
		for(int i=min(n,m)-1;i>=0;i--)
		{
			if(v[i]!=0)
			{
				cout<<i+1<<" "<<v[i]<<endl;
			}
			sum+=(i+1)*(i+1)*v[i];
		}
		while(sum!=m*n);
	}
}