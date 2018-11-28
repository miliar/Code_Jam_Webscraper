#include<fstream>
#define dmax 20
using namespace std;
ifstream in("candy.in");
ofstream out("candy.out");

long long n,x[dmax],st[dmax],s,tst,sm,sx,ok,sol;
bool t[dmax];

void bkt(int k)
{	
	int i;
	
	if(k <= n+1)
	{	
		sm = 0;
		sx = 0;
		for(i=1; i<k;i++)
		{	sm += x[st[i]];
			sx = sx xor x[st[i]];
		}

		if(s-sm == sx && sm!= 0 && s-sm != 0)
		{	sol = max(sol, s-sm);
			sol = max(sol, sm);
			ok = 1;
		}	
	
		for(i=st[k-1]+1; i<=n; i++)
			if(!t[i])
			{	st[k] = i;
				t[i] = 0;
				bkt(k+1);
			}			
	}
}



int main()
{	
	int i,j;
	
	in>>tst;
	
	for(j=1;j<=tst;j++)
	{	
		in>>n;
		s = 0;
		sol = 0;
		ok = 0;
		
		for(i=1; i<=n; i++)
		{	in>>x[i];
			s += x[i];
		}	
		
		bkt(1);
		
		out<<"Case #"<<j<<": ";
		
		if(ok)
			out<<sol<<'\n';
		else out<<"NO\n";
	}

	in.close();
	out.close();
	return 0;
}	