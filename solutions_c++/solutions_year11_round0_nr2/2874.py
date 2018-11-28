#include<fstream>
#include<list>
#include<vector>
#define dmax 30
using namespace std;
ifstream in("magicka.in");
ofstream out("magicka.out");

vector<int>x[dmax];
vector<int>::iterator it;

vector<char>lst;
vector<char>::iterator ir;

int tst,n,m,k,l;
char p[4],z[10][10],cd;
int t[10];

int cod(char c)
{	
	if(c == 'Q')return 1;
	if(c == 'W')return 2;
	if(c == 'E')return 3;
	if(c == 'R')return 4;
	if(c == 'A')return 5;
	if(c == 'S')return 6;
	if(c == 'D')return 7;
	if(c == 'F')return 8;
	return 0;
}
	

int main()
{	
	int i,j,a,b,r;
	
	
	for(j=0; j<10; j++)
		for(r=0; r<10; r++)
			z[j][r] = '0';
	
	in>>tst;
	
	for(i=1;i<=tst; i++)
	{	
		in>>n;

		for(j=1; j<=n; j++)	
		{	in>>p;	
			a = cod(p[0]);
			b = cod(p[1]);
			z[a][b] = p[2];
			z[b][a] = p[2];	
		}

		in>>m;
		
		for(j=1; j<=m; j++)	
		{	in>>p;	
			a = cod(p[0]);
			b = cod(p[1]);
			x[a].push_back(b);
			x[b].push_back(a);
		}
		
		in>>l;
		
		if(l)
		{	in>>cd;
			lst.push_back(cd);
			t[cod(cd)] = 1;
		
			for(j=2;j<=l;j++)
			{	
				in>>cd;

				a = cod(cd);
				if(!lst.empty())
					b = cod(lst.back() );
				else b = 0;
				
				if(z[a][b] != '0')
				{	t[b] --;
					lst.pop_back();
					lst.push_back(z[a][b]);
				}	
				else
				{	lst.push_back(cd);
					t[a] ++;
				
					for(it = x[a].begin(); it<x[a].end(); it++)
						if(t[*it] )
							while(!lst.empty() )
							{	b = cod(lst.back() );
								t[b] = 0;
								lst.pop_back();
							}	
							
							
				}
				
			}
		}
		out<<"Case #"<<i<<": [";
		
		if(!lst.empty() )
			out<<lst.front();
		if(lst.size() > 1)
			for(ir = lst.begin()+1; ir != lst.end(); ir++)
				out<<", "<<*ir;
		
		out<<"]\n";
		
		
		for(j=0; j<10; j++)
			t[j] = 0;
		for(j=0; j<10; j++)
			for(r=0; r<10; r++)
				z[j][r] = '0';
		for(j=0; j<10; j++)
			x[j].clear();
		lst.clear();
		
	}
	
	
	
	in.close();
	out.close();
	return 0;
}	