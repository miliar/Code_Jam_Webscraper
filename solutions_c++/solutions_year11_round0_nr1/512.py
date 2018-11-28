#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int t,n;
vector <string> a;
vector <int> b;
vector <int> c1,c2;
int d1,d2,e1,e2,g,h;
int gt(int p,int q)
{
	if (p==q) return p;
	else return p+abs(q-p)/(q-p);
}
int main()
{
	in >> t;
	for (int x=1;x<=t;x++)
	{
		g=0;
		h=0;
		d1=0;
		d2=0;
		e1=1;
		e2=1;
		c1.resize(0);
		c2.resize(0);
		in >> n;
		a.resize(n);
		b.resize(n);
		for (int i=0;i<n;i++)
		{
			in >> a[i] >> b[i];
			if (a[i]=="B") c1.push_back(b[i]);
			else c2.push_back(b[i]);
		}
		while (h<n)
		{
			if (a[h]=="B")
			{
				if (b[h]==e1)
				{
					h++;
					d1++;
				}
				else e1=gt(e1,c1[d1]);
				if (d2<c2.size()) e2=gt(e2,c2[d2]);
			}
			else
			{
				if (b[h]==e2)
				{
					h++;
					d2++;
				}
				else e2=gt(e2,c2[d2]);
				if (d1<c1.size()) e1=gt(e1,c1[d1]);
			}
			g++;
		}
		out << "Case #" << x << ": " << g << "\n";
	}
	return 0;
}
