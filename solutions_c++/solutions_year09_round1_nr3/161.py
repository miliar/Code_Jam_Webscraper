#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;

int N,C;

double cc[41][41];
double val[41];
bool done[41];

double f(int cur)
{
	if(done[cur])
		return val[cur];
	done[cur]=1;
	double num = 1 , sum = 1;
	for(int i=0;i<=cur;i++)
		if(N-i >= 0)
			if(N-i <= C-cur)
			{
				
				if(i == N)
					num -= cc[cur][i]*cc[C-cur][N-i]/cc[C][N];
				else
				{
					
					sum += cc[cur][i]*cc[C-cur][N-i]/cc[C][N]*f(cur+N-i);
				}
			}
	val[cur]=sum/num;	

	return val[cur];
}

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	cout<<fixed<<setprecision(7);
	for(int i=0;i<=40;i++)
	{
		cc[i][0]=1;
		for(int j=1;j<i;j++)
			cc[i][j]=cc[i-1][j]+cc[i-1][j-1];
		cc[i][i]=1;
	}

	int T;
	cin>>T;
	for(int c=1;c<=T;c++)
	{
		cin>>C>>N;
		memset(done,0,sizeof(done));
		done[C]=1;
		val[C]=0;
		cout<<"Case #"<<c<<": "<<f(0)<<endl;
	}
	return 0;	
}
