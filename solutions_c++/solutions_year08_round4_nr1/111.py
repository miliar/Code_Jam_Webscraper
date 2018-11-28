#include <fstream>
#define MAX 99999
using namespace std;
int g[5000],c[5000];
int d[10000][2];
void main()
{
	int n,CASE;
	ifstream in ("input.in");
	ofstream out ("output.out");
	in >> n;
	for(CASE=0;CASE<n;CASE++)
	{
		int ans;
		int m,v;
		in >> m >> v;
		int i;
		for(i=0;i<m;i++) d[i][0]=d[i][1]=MAX;
		for(i=0;i<(m-1)/2;i++)
		{
			in >> g[i] >> c[i];
		}
		for(i=0;i<(m+1)/2;i++)
		{
			int tmp;
			in >> tmp;
			d[i+(m-1)/2][tmp]=0;
		}
		for(i=(m-1)/2-1;i>=0;i--)
		{
			if(g[i]==0)	//OR gate
			{
				if(d[i*2+1][0]<MAX && d[i*2+2][0]<MAX)
				{
					d[i][0]=d[i*2+1][0]+d[i*2+2][0];
				}
				int s11=d[i*2+1][1]+d[i*2+2][1];
				int s01=d[i*2+1][0]+d[i*2+2][1];
				int s10=d[i*2+1][1]+d[i*2+2][0];
				if(s11<s01 && s11<s10)
					d[i][1]=s11;
				else if(s01<s10)
					d[i][1]=s01;
				else if(s10<MAX)
					d[i][1]=s10;
				if(c[i]==1 && (d[i*2+1][0]<MAX || d[i*2+2][0]<MAX))
				{
					int min=((d[i*2+1][0]<d[i*2+2][0])?d[i*2+1][0]:d[i*2+2][0]);
					if(d[i][0]>min+1) d[i][0]=min+1;
				}
			}
			else		//AND gate
			{
				if(d[i*2+1][1]<MAX && d[i*2+2][1]<MAX)
					d[i][1]=d[i*2+1][1]+d[i*2+2][1];
				int s00=d[i*2+1][0]+d[i*2+2][0];
				int s01=d[i*2+1][0]+d[i*2+2][1];
				int s10=d[i*2+1][1]+d[i*2+2][0];
				if(s00<s01 && s00<s10)
					d[i][0]=s00;
				else if(s01<s10)
					d[i][0]=s01;
				else if(s10<MAX)
					d[i][0]=s10;
				if(c[i]==1 && (d[i*2+1][1]<MAX || d[i*2+2][1]<MAX))
				{
					int min=((d[i*2+1][1]<d[i*2+2][1])?d[i*2+1][1]:d[i*2+2][1]);
					if(min+1<d[i][1]) d[i][1]=min+1;
				}
			}
		}
		ans=d[0][v];
		if(ans>=MAX)
			out << "Case #" << CASE+1 << ": IMPOSSIBLE" << endl;
		else
			out << "Case #" << CASE+1 << ": " << ans << endl;
	}
	out.close();
	in.close();
}