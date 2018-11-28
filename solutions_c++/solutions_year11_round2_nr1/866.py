#include<iostream>
using namespace std;

int work(int test_now)
{
	cout<<"Case #"<<test_now+1<<":"<<endl;
	int n;
	cin>>n;
	char ch;
	int f[n][n];
	memset(f,0,sizeof(f));
	for (int i=0; i<n; i++)
	{
		for (int j=0; j<n; j++)
			{
				cin>>ch;
				if (ch=='0')
					f[i][j]=-1;
				if (ch=='1')
					f[i][j]=1;	
          }
	};
	double wp[n];
	double owp[n];
	double oowp[n];
	for (int i=0; i<n; i++)
		{
			int count=0;
			int won=0;
			for (int j=0; j<n; j++)
			{
				if (f[i][j]!=0)
					count++;
				if (f[i][j]==1)
					won++;
				
          }
			wp[i]=double(won)/count;
		}
	for (int i=0; i<n; i++)
		{
			double res=0;
			int ttt=0;
			for (int j=0; j<n; j++)
				if (f[i][j]!=0)
					{
						int count=0;
						int won=0;
						for (int k=0; k<n; k++)
						if (k!=i)
						{
							if (f[j][k]!=0)
								count++;
							if (f[j][k]==1)
								won++;
						}
						res=res+double(won)/count;
						ttt++;
					}
			owp[i]=res/ttt;
			
		}
	for (int i=0; i<n; i++)
		{
			double res=0;
			int ttt=0;
			for (int j=0; j<n; j++)
				if (f[i][j]!=0)
				{
                    ttt++;
					res=res+owp[j];
            }
			oowp[i]=res/ttt;
		}
	for (int i=0; i<n; i++)
		cout<<0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]<<endl;
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
