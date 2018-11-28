#include <iostream>
#include <stdio.h>
#include <queue>
#include <vector>
#include <set>
#include <memory.h>

using namespace std;

#define FOR(i,b) for (int i = 0; i < (b); i++)
#define MP(A,B) make_pair(A,B)

typedef vector<int>::iterator VI;

int N;
int M;

vector< vector<int> > v;

int x[10];
int y[10];

int sol[8];

bool FIND(vector<int> v, int el)
{
	for(VI it = v.begin();it!=v.end();it++)
	{
		if(*it==el)
		{
			return true;
		}
	}
	
	return false;
}

bool Solve(int pos, int Col)
{
	if(pos<N)
	{
		for(int n=0;n<Col;n++)
		{
			sol[pos]=n;
			if(Solve(pos+1,Col))
			{
				return true;
			}
		}
		
		return false;
	}
	else
	{
		for(unsigned int n=0;n<v.size();n++)
		{
			bool col[Col];
			
			for(int m=0;m<Col;m++)
			{
				col[m]=false;
			}
			
			for(vector<int>::iterator it = v[n].begin();it!=v[n].end();it++)
			{
				col[sol[*it]]=true;
			}
			
			for(int m=0;m<Col;m++)
			{
				if(!col[m])
				{
					return false;
				}
			}
			
			
		}
		
		return true;
		
	}
}

int main()
{
	int T;
	scanf("%d",&T);
	
	FOR(t,T)
	{
		
		scanf("%d %d",&N,&M);
		
		v.clear();
		vector<int> help;
		
		FOR(n,N)
		{
			help.push_back(n);
		}
		
		v.push_back(help);
		
		FOR(n,M)
		{
			int a;
			scanf("%d",&a);
			a--;
			x[n]=a;
		}
		
		FOR(n,M)
		{
			int a;
			scanf("%d",&a);
			a--;
			y[n]=a;
		}
		
		FOR(n,M)
		{
			if(x[n]>y[n])
			{
				int help = x[n];
				x[n]=y[n];
				y[n]=help;
			}
		}
		
		
		for(int n=0;n<M;n++)
		{
			for(unsigned int k=0;k<v.size();k++)
			{
				if( FIND(v[k],x[n]) && FIND(v[k],y[n])	)
				{
					
					// split elemnts in two halfes
					vector<int> c = v[k];
					
					v.erase(v.begin()+k);
					
					
					vector<int> left;
					vector<int> right;
					
					int pos =0;
					
					while(c[pos]!=x[n])
					{
						pos++;
					}
					
					int counter=pos;
					
					while(c[counter]!=y[n])
					{
						left.push_back(c[counter]);
						
						counter = (counter+1)%c.size();
					}
					
					left.push_back(c[counter]);
					
					
					while(c[counter]!=x[n])
					{
						right.push_back(c[counter]);
						counter = (counter+1)%c.size();
					}
					
					right.push_back(c[counter]);
					
					

					
					v.push_back(left);
					v.push_back(right);
					
					break;
				} 
			}
		}
		
		int limit =N;
		
		for(unsigned int n=0;n<v.size();n++)
		{
			//printf("NUM : %d : ",n);
			limit = min(limit,(int)v[n].size());
		}
		
		while(true)
		{
			for(int n=limit;n>=0;n--)
			{
				if(Solve(0,n))
				{
					printf("Case #%d: %d\n",t+1,n);
					printf("%d",sol[0]+1);
					
					for(int n=1;n<N;n++)
					{
						printf(" %d",sol[n]+1);
					}
					printf("\n");
					goto finish;
				}
			}
		}
		
		finish:
		
		int p =9;
		
		
		
		
	}
}