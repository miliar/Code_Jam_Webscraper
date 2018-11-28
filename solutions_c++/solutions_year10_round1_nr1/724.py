#include <iostream>
#include <algorithm>
using namespace std;
int tt,n,k;
char ch[101][101];
char ne[101][101];
int now[101];
void rot()
{
	for (int i=0;i<n;++i)
	{
		for (int j=0;j<n;++j)
		{
			ne[j][n-1-i]=ch[i][j];
		}
	}
}
int main()
{	
	cin>>tt;
	for (int kk=1;kk<=tt;++kk)
	{
		cin>>n>>k;
		memset(ch,0,sizeof(ch));
		memset(ne,0,sizeof(ne));
		for (int i=0;i<n;++i)
		{
			cin>>ch[i];
		}
		rot();
		//for (int i=0;i<n;++i)
		//{
		//	for (int j=0;j<n;++j)
		//	{
		//		cout<<ne[i][j];
		//	}
		//	cout<<endl;
		//}
		memset(ch,'.',sizeof(ch));
		for (int i=0;i<n;++i)
		{
			now[i]=n-1;
		}
		for (int i=0;i<n;++i)
		{			
			for (int j=n-1;j>=0;--j)
			{
				if (ne[j][i]!='.')
				{
					ch[now[i]][i]=ne[j][i];
					now[i]--;					
				}
			}			
		}
		//for (int i=0;i<n;++i)
		//{
		//	for (int j=0;j<n;++j)
		//	{
		//		cout<<ch[i][j];
		//	}
		//	cout<<endl;
		//}
		int flagr=0;
		int flagb=0;
		for (int i=n-1;i>=0;--i)
		{
			for (int j=0;j<n;++j)
			{
				if (ch[i][j]=='.')
				{
					continue;
				}
				if (ch[i][j]=='R' && flagr==1)
				{
					continue;
				}
				if (ch[i][j]=='B' && flagb==1)
				{
					continue;
				}
				int cot=1;
				for (int l=i-1;l>=0;--l)
				{
					if (ch[l][j]==ch[i][j])
					{
						cot++;
					}
					else
					{
						break;
					}
				}
				if (cot>=k)
				{
					if (ch[i][j]=='R')
					{
						flagr=1;
					}
					if (ch[i][j]=='B')
					{
						flagb=1;
					}
					continue;
				}
				cot=1;
				for (int l=j+1;l<n;++l)
				{
					if (ch[i][l]==ch[i][j])
					{
						cot++;
					}
					else
					{
						break;
					}
				}
				if (cot>=k)
				{
					if (ch[i][j]=='R')
					{
						flagr=1;
					}
					if (ch[i][j]=='B')
					{
						flagb=1;
					}
					continue;
				}
				cot=1;
				for (int l=i+1,p=j-1;l<n && p>=0;++l,--p)
				{
					if (ch[l][p]==ch[i][j])
					{
						cot++;
					}
					else
					{
						break;
					}
				}
				if (cot>=k)
				{
					if (ch[i][j]=='R')
					{
						flagr=1;
					}
					if (ch[i][j]=='B')
					{
						flagb=1;
					}
					continue;
				}
				cot=1;
				for (int l=i+1,p=j+1;l<n && p<n;++l,++p)
				{
					if (ch[l][p]==ch[i][j])
					{
						cot++;
					}
					else
					{
						break;
					}
				}
				if (cot>=k)
				{
					if (ch[i][j]=='R')
					{
						flagr=1;
					}
					if (ch[i][j]=='B')
					{
						flagb=1;
					}
					continue;
				}
				cot=1;
				for (int l=i-1,p=j-1;l>=0 && p>=0;--l,--p)
				{
					if (ch[l][p]==ch[i][j])
					{
						cot++;
					}
					else
					{
						break;
					}
				}
				if (cot>=k)
				{
					if (ch[i][j]=='R')
					{
						flagr=1;
					}
					if (ch[i][j]=='B')
					{
						flagb=1;
					}
					continue;
				}
			}
		}
		printf("Case #%d: ",kk);
		if (flagb==1 && flagr==1)
		{
			cout<<"Both"<<endl;
		}
		else if (flagb==0 && flagr==1)
		{
			cout<<"Red"<<endl;
		}
		else if (flagb==1 && flagr==0)
		{
			cout<<"Blue"<<endl;
		}
		else
		{
			cout<<"Neither"<<endl;
		}
	}
	return 0;	
}