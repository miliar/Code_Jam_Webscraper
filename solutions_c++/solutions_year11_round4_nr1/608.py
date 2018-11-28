#include <fstream>
#include <vector>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int tt;
double x,s,r;
int n;
double t,res;
double b,e;
int w;
vector <double> v;
int main()
{
	out.setf(ios::fixed);
	out.precision(7);
	in >> tt;
	for (int nt=1;nt<=tt;nt++)
	{
		in >> x >> s >> r >> t >> n;
		v.assign(101,0);
		v[0]=x;
		for (int i=0;i<n;i++)
		{
			in >> b >> e >> w;
			v[w]+=e-b;
			v[0]-=e-b;
		}
		res=0.0;
		for (int i=0;i<=100;i++) if (v[i]>0)
		{
			if (v[i]<=t*(r+i))
			{
				t-=v[i]/(r+i);
				res+=v[i]/(r+i);
			}
			else
			{
				res+=t+(v[i]-t*(r+i))/(s+i);
				t=0;
			}
		}
		out << "Case #" << nt << ": " << res << "\n";
	}
	return 0;
}
