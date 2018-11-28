#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>


using namespace std;
int A[100][100];
double wp[100], owp[100], oowp[100], rpi[100];

int main(int argc, char** argv)
{
	ifstream f(argv[1]);
	int T;
	f >> T;
	ofstream g(argv[2]);
	g.precision(15);

	for (int t=0; t<T; ++t)
	{
		int N;
		f >> N;
		vector<string> st;
		st.resize(N);
		for (int i=0; i<N; ++i)
		{
			f >> st[i];
		}
		//compute
		vector<int> n_m(N, 0);
		for (int i=0; i<N; ++i)
		{
			int nw = 0;
			int nl = 0;
			for (int j=0; j<N; ++j)
			{
				if (st[i][j]=='1')
				{
					nw++;
				}
				else if (st[i][j]=='0') 
				{
					nl++;
				}
				
			}
			wp[i] = (double)nw / (double)(nw+nl);
			n_m[i] = nw+nl;
		}
		//cout <<"WP = ";
		//for (int i=0; i<N; ++i) cout <<wp[i]<<" ";
		//cout <<endl;


		for (int i=0; i<N; ++i)
		{
			int nn=0;
			double x=0;
			for (int j=0; j<N; ++j)
			{
				if (st[i][j]=='0' || st[i][j]=='1')
				{
					
					nn++;
					if (st[i][j]=='0')	
					{
						double new_wp = (wp[j] * n_m[j]-1.0)/(n_m[j]-1);
						x+= new_wp;
					}
					else
					{
						double new_wp = (wp[j] * n_m[j])/(n_m[j]-1);
						x+= new_wp;
					}
				}				
			}
			owp[i] = x / n_m[i];
		}
		//cout <<"OWP = ";
		//for (int i=0; i<N; ++i) cout <<owp[i]<<" ";
		//cout <<endl;

		for (int i=0; i<N; ++i)
		{
			int nn=0;
			double x=0;
			for (int j=0; j<N; ++j)
			{
				if (st[i][j]=='0' || st[i][j]=='1')
				{
					x+= owp[j];
					nn++;
				}				
			}
			oowp[i] = x / nn;
		}

		//cout <<"OOWP = ";
		//for (int i=0; i<N; ++i) cout <<oowp[i]<<" ";
		//cout <<endl;
		for (int i=0; i<N; ++i)
		{
			rpi[i] = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
		}
		//cout <<"RPI = ";
		//for (int i=0; i<N; ++i) cout <<rpi[i]<<" ";
		//cout <<endl<<endl;

		g <<"Case #"<<(t+1)<<":"<<endl;
		for (int i=0; i<N; ++i) g <<rpi[i]<<endl;
	}
	g.close();


}