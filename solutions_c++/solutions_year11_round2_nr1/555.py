#include<fstream>
#include<string>
#include<algorithm>
#include<map>
#include<vector>
#include<iomanip>

using namespace std;

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int t;
	cin>>t;
	cout.flags(std::ios::fixed);
	cout<<setprecision(8);
	for(int tt=0; tt<t; tt++)
	{
		int n;
		cin>>n;
		char m[110][110];
		for(int i=0; i<n;i++)
		{
			for(int j=0; j<n; j++)
			{
				cin>>m[i][j];
			}
		}
		double wp[110];
		for(int i=0; i<n; i++)
		{
			int k=0;
					int w=0;
					for(int r = 0; r<n; r++)
					{

						if (m[i][r]!='.') k++;
						if (m[i][r]=='1') w++;
						
					}
					wp[i]=w/double(k);

		}

		double owp[110];
		for(int i=0; i<n;i++)
		{
			double sum = 0;
			int nn = 0;
			for(int j=0; j<n; j++)
			{
				if (m[i][j]!='.')
				{
					int k=0;
					int w=0;
					for(int r = 0; r<n; r++)
					{
						if (r!=i)
						{
						if (m[j][r]!='.') k++;
						if (m[j][r]=='1') w++;
						}
					}
					sum+=w/double(k);
					nn++;
				}
				
			}
			owp[i] = sum/nn;
		}

		cout<<"Case #"<<tt+1<<": "<<endl;
		for(int i=0; i<n; i++)
		{
			double res = 0 ;
			int nn=0;
			for(int j=0; j<n;j++)
			{
				if (m[i][j]!='.') 
				{
					nn++;
					res+=owp[j];
				}
			}

			cout<<0.25*wp[i]+0.5*owp[i]+0.25*(res/nn)<<endl;
		}
		
	}
	return 0;
}