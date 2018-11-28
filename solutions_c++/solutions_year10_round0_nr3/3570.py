#include<fstream>
#include<queue>
#define dmax 1004
using namespace std;
ifstream in("theme.in");
ofstream out("theme.out");

int t,n,r,k,w,s;
queue<int>q;

void solve(int nr)
{	int i,crt=0,x,y=0;
	s=0;
	for(i=1;i<=r;i++)
	{	while(crt+q.front() <= k && y<n)
		{	x=q.front();
			crt+=x;
			y++;
			s+=x;
			q.pop();
			q.push(x);
		}
		crt=0;
		y=0;
	}
	out<<"Case #"<<nr<<": "<<s<<'\n';
}	

int main()
{	int i,j;
	in>>t;
	for(i=1;i<=t;i++)
	{	in>>r>>k>>n;	
		while(!q.empty())
			q.pop();
		for(j=1;j<=n;j++)
		{	in>>w;
			q.push(w);
		}	
		solve(i);
	}
	in.close();
	out.close();
	return 0;
}	