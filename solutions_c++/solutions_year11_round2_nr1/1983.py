#include<fstream>
#define dmax 104
using namespace std;
ifstream in("rpi.in");
ofstream out("rpi.out");

int n,t,mat[dmax][dmax],m[dmax],w[dmax];
char c;
double wp[dmax], owp[dmax], oowp[dmax], rpi, towp; 


void solve()
{	
	int i,j;
	
	for(i=1; i<=n; i++)
	{	wp[i] = 0;
		oowp[i] = 0;
		owp[i] = 0;
	}	
	towp = 0;
	
	for(i=1; i<=n; i++)
	{	
		wp[i] = (double)w[i] / (double)m[i];
	}
	
	for(i=1; i<=n; i++)
	{	owp[i]=0;
		
		for(j=1; j<=n; j++)
			if(j != i)
				if(mat[i][j] != 0)
				{	
					if(mat[i][j] == -1)
						owp[i] += ( (double)(w[j]-1) / (double)(m[j]-1) );
					
					else if(mat[i][j] == 1)
						owp[i] += ( (double)w[j] / (double)(m[j]-1) );
						
					//else owp[i] += wp[i];
				}	
				
		owp[i] /= m[i];
		
		towp += owp[i];
	}	
	
	for(i=1; i<=n; i++)
	{	for(j=1; j<=n; j++)
			if(j!=i)
				if(mat[i][j] != 0)
				{
					oowp[i] += owp[j];
				}	
		oowp[i] /= m[i];
	}	
	
	
	for(i=1; i<=n; i++)
	{	//out<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<'\n';
		rpi = 0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
		out<<fixed<<rpi<<'\n';
		
		w[i] = m[i] = 0;
	}	
	
}	



int main()
{	
	int i,j,q;
	
	in>>t;
	
	for(q=1; q<=t; q++)
	{	
		in>>n;

		for(i=1; i<=n; i++)
			for(j=1; j<=n; j++)
			{	in>>c;
				if(c=='1')
				{	mat[i][j]=1;
					m[i]++;
					w[i]++;
				}	
				else if(c=='0')
				{	mat[i][j]=-1;
					m[i]++;
				}	
				else if(c=='.')
					mat[i][j]=0;
			}
		
		out<<"Case #"<<q<<":\n";
		solve();
	}

	in.close();
	out.close();
	return 0;
}	