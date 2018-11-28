#include <fstream>
using namespace std;
void main()
{
	int n,CASE;
	ifstream in ("input.in");
	ofstream out ("output.out");
	in >> n;
	for(CASE=0;CASE<n;CASE++)
	{
		int ans=-1;
		int h,w,r;
		int i,j;
		int p[100][100]={0,};
		in >> h >> w >> r;
		for(i=0;i<r;i++)
		{
			int x,y;
			in >> x >> y;
			p[x-1][y-1]=-1;
		}
		p[0][0]=1;
		for(i=0;i<h;i++)
			for(j=0;j<w;j++)
			{
				if(p[i][j]<=0) continue;
				if(i+1<h && j+2<w && p[i+1][j+2]>=0) p[i+1][j+2]+=p[i][j]%10007;
				if(i+2<h && j+1<w && p[i+2][j+1]>=0) p[i+2][j+1]+=p[i][j]%10007;
			}
		ans=p[h-1][w-1]%10007;
		out << "Case #" << CASE+1 << ": " << ans << endl;
	}
	out.close();
	in.close();
}