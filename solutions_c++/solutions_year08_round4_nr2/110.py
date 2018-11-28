#include <fstream>
using namespace std;
void main()
{
	int c,CASE;
	ifstream in ("input.in");
	ofstream out ("output.out");
	in >> c;
	for(CASE=0;CASE<c;CASE++)
	{
		int ans[2][2];
		int i,j,k,l,n,m,a;
		in >> n >> m >> a;
		for(i=0;i<=n;i++)
		{
			for(j=0;j<=m;j++)
			{
				for(k=0;k<=n;k++)
				{
					for(l=0;l<=m;l++)
					{
						int maxx=((i>k)?i:k), maxy=((j>l)?j:l);
						int difx=i-k,dify=j-l; if(difx<0) difx*=-1; if(dify<0) dify*=-1;
						int area=maxx*maxy*2;
						area-=(difx*dify+i*j+k*l);
						if(maxx==i && maxy==j)
						{
							if(i*l-j*k>0)
								area-=(j-l)*k*2;
							else
								area-=(i-k)*l*2;
						}
						if(maxx==k && maxy==l)
						{
							if(k*j-l*i>0)
								area-=(l-j)*i*2;
							else
								area-=(k-i)*j*2;
						}
						if(area==a)
							break;
					}
					if(l<=m) break;
				}
				if(k<=n) break;
			}
			if(j<=m) break;
		}
		if(i>n)
			out << "Case #" << CASE+1 << ": IMPOSSIBLE" << endl;
		else
		{
			ans[0][0]=i; ans[0][1]=j; ans[1][0]=k; ans[1][1]=l;
			out << "Case #" << CASE+1 << ": 0 0 " << ans[0][0] << ' ' << ans[0][1] << ' ' << ans[1][0] << ' ' << ans[1][1] << endl;
		}
	}
	out.close();
	in.close();
}