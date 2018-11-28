#include<iostream>
using namespace std;

int work(int test_now)
{
	cout<<"Case #"<<test_now+1<<": "<<endl;
	int n,m;
	cin>>n>>m;
	char ch;
	int f[n][m];
	memset(f,0,sizeof(f));
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<m; j++)
			{
				cin>>ch;
				if (ch=='#')
					f[i][j]=1;
			//	cout<<f[i][j];
          }
         // cout<<endl;
}
	int l[4],r[4];
	l[0]=0;
	l[1]=0;
	l[2]=1;
	l[3]=1;
	r[0]=0;
	r[1]=1;
	r[2]=0;
	r[3]=1;
	int flag=1;
	int g[n][m];
	memset(g,0,sizeof(g));
	for (int i=0; i<n; i++)
		for (int j=0; j<m; j++)
			if (f[i][j])
				{
					for (int k=0; k<4; k++)
						{
							int x=i+l[k];
							int y=j+r[k];
							if (x>=n||y>=m||f[x][y]==0)
								flag=0;
							if (flag==0)
								break;
							g[x][y]=k+1;
							f[x][y]=0;
						}
				}
	if (flag==0)
		cout<<"Impossible"<<endl;
	else
	{
		for (int i=0; i<n; i++)
		{
			for (int j=0; j<m; j++)
				{
					int x=g[i][j];
					if (x==0) cout<<'.';
					if (x==1||x==4) cout<<'/';
					if (x==2||x==3) cout<<'\\';
				}
			cout<<endl;
		}
	}
}

int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
	int test_num;
	cin>>test_num;
	for (int i=0; i<test_num; i++)
		work(i);
	return 0;
}
