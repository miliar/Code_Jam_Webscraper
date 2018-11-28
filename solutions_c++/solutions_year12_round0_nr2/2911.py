#include <fstream>
using namespace std;
ifstream f("input");
ofstream g("output");
unsigned t,s,p,i,di,j,n,y;
int main()
{
	f>>t;
	for(j=1;j<=t;j++)
	{
		y=0;
		f>>n;
		f>>s;
		f>>p;
		if(p==0)
			{
				y=n;
				for(i=1;i<=n;i++)f>>di;
}
		else
		for(i=1;i<=n;i++)
		{
			f>>di;
			if(di!=0)
			{
				if(3*p-2<=di)
					y++;
				else
					if((p+2*(p-2)<=di)&&s>0)
						s--,y++;
			}
					
		}
		g<<"Case #"<<j<<": "<<y<<"\n";
	}
	f.close();
	g.close();
	return 0;
}