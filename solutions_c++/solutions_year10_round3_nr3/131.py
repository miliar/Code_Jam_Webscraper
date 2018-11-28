#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
int mp[600][600];
char ch[1000];
int m,n,tt;
int rec[600];
int judge(int s1,int s2,int size)
{
	int sig;
	if (mp[s1][s2]==1)
	{
		sig=0;
	}
	else
	{
		sig=1;
	}
	if (s1+size>m || s2+size>n)
	{
		return 0;
	}
	for (int i=s1;i<s1+size;++i)
	{
		for (int j=s2;j<s2+size;++j)
		{
			if ((i+j-s1-s2)%2==0)
			{
				if (mp[i][j]!=mp[s1][s2])
				{
					return 0;
				}
			}
			else
			{
				if (mp[i][j]!=sig)
				{
					return 0;
				}
			}
		}
	}
	return 1;
}
void fulfill(int s1,int s2,int size)
{
	for (int i=s1;i<s1+size;++i)
	{
		for (int j=s2;j<s2+size;++j)
		{
			mp[i][j]=-1;
		}
	}
}
int main()
{
	cin>>tt;	
	for (int kk=1;kk<=tt;++kk)
	{
		cin>>m>>n;
		memset(mp,0,sizeof(mp));
		memset(rec,0,sizeof(rec));
		for (int i=0;i<m;++i)
		{
			cin>>ch;
			for (int j=0;j<n/4;++j)
			{
				switch(ch[j])
				{
				case '0':
					mp[i][j*4]=0;
					mp[i][j*4+1]=0;
					mp[i][j*4+2]=0;
					mp[i][j*4+3]=0;
					break;
				case '1':
					mp[i][j*4]=0;
					mp[i][j*4+1]=0;
					mp[i][j*4+2]=0;
					mp[i][j*4+3]=1;
					break;
				case '2':
					mp[i][j*4]=0;
					mp[i][j*4+1]=0;
					mp[i][j*4+2]=1;
					mp[i][j*4+3]=0;
					break;
				case '3':
					mp[i][j*4]=0;
					mp[i][j*4+1]=0;
					mp[i][j*4+2]=1;
					mp[i][j*4+3]=1;
					break;
				case '4':
					mp[i][j*4]=0;
					mp[i][j*4+1]=1;
					mp[i][j*4+2]=0;
					mp[i][j*4+3]=0;
					break;
				case '5':
					mp[i][j*4]=0;
					mp[i][j*4+1]=1;
					mp[i][j*4+2]=0;
					mp[i][j*4+3]=1;
					break;
				case '6':
					mp[i][j*4]=0;
					mp[i][j*4+1]=1;
					mp[i][j*4+2]=1;
					mp[i][j*4+3]=0;
					break;
				case '7':
					mp[i][j*4]=0;
					mp[i][j*4+1]=1;
					mp[i][j*4+2]=1;
					mp[i][j*4+3]=1;
					break;
				case '8':
					mp[i][j*4]=1;
					mp[i][j*4+1]=0;
					mp[i][j*4+2]=0;
					mp[i][j*4+3]=0;
					break;
				case '9':
					mp[i][j*4]=1;
					mp[i][j*4+1]=0;
					mp[i][j*4+2]=0;
					mp[i][j*4+3]=1;
					break;
				case 'A':
					mp[i][j*4]=1;
					mp[i][j*4+1]=0;
					mp[i][j*4+2]=1;
					mp[i][j*4+3]=0;
					break;
				case 'B':
					mp[i][j*4]=1;
					mp[i][j*4+1]=0;
					mp[i][j*4+2]=1;
					mp[i][j*4+3]=1;
					break;
				case 'C':
					mp[i][j*4]=1;
					mp[i][j*4+1]=1;
					mp[i][j*4+2]=0;
					mp[i][j*4+3]=0;
					break;
				case 'D':
					mp[i][j*4]=1;
					mp[i][j*4+1]=1;
					mp[i][j*4+2]=0;
					mp[i][j*4+3]=1;
					break;
				case 'E':
					mp[i][j*4]=1;
					mp[i][j*4+1]=1;
					mp[i][j*4+2]=1;
					mp[i][j*4+3]=0;
					break;
				case 'F':
					mp[i][j*4]=1;
					mp[i][j*4+1]=1;
					mp[i][j*4+2]=1;
					mp[i][j*4+3]=1;
					break;
				default:
					break;
				}
			}
		}
		int num=0;
		while (num<n*m)
		{
			int largest=0;
			int st,ed;
			for (int i=0;i<m;++i)
			{
				for (int j=0;j<n;++j)
				{
					if (mp[i][j]==-1)
					{
						continue;
					}
					while (judge(i,j,largest+1))
					{
						largest++;
						st=i;
						ed=j;					
					}
				}
			}
			fulfill(st,ed,largest);
			num+=largest*largest;
			rec[largest]++;
		}
		int ans=0;
		for (int i=550;i>=1;--i)
		{
			if (rec[i]>0)
			{
				ans++;
			}
		}
		printf("Case #%d: ",kk);
		cout<<ans<<endl;
		for (int i=550;i>=1;--i)
		{
			if (rec[i]>0)
			{
				cout<<i<<" "<<rec[i]<<endl;
			}
		}
	}	
	return 0;	
}