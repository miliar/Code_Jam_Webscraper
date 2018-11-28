#include<fstream>
#define dmax 53
using namespace std;
ifstream in("square.in");
ofstream out("square.out");

int t,n,m;
char c,mat[dmax][dmax];

int bune(int ii, int jj)
{	
	return (ii>0 && ii<=n && jj>0 && jj<=m);
}


int merge(int i, int j)
{	
	int ok=1;
	
	if(!bune(i, j+1) || mat[i][j+1]!='#' )
		ok = 0;
	if(!bune(i+1, j) || mat[i+1][j]!='#' )
		ok = 0;
	if(!bune(i+1, j+1) || mat[i+1][j+1]!='#' )
		ok = 0;
	return ok;
}	


void solve()
{	
	int i,j,ok=1;
	
	for(i=1; i<=n; i++)
		for(j=1; j<=m; j++)
			if(mat[i][j] == '#')
			{	
				if(merge(i,j) )
				{	
					mat[i][j] = '/';
					mat[i][j+1]=(char)92;
					mat[i+1][j]=(char)92;
					mat[i+1][j+1]='/';
				}
				else ok = 0;	
			}
			
	if(ok)
		for(i=1; i<=n; i++)
		{	for(j=1; j<=m; j++)
				out<<mat[i][j];
			out<<'\n';
		}
	else out<<"Impossible\n";		
}

int main()
{	
	int i,j,q;
	
	in>>t;
	
	for(q=1; q<=t; q++)
	{	
		in>>n>>m;

		for(i=1; i<=n; i++)
			for(j=1; j<=m; j++)
			{	in>>mat[i][j];
				
			}
		out<<"Case #"<<q<<":\n";	
		solve();

	}

	in.close();
	out.close();
	return 0;
}	