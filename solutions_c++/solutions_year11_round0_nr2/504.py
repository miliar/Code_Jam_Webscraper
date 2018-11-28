#include <fstream>
#include <vector>
#include <string>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int t,c,d,n;
vector <string> a,b;
string e;
vector <char> s;
int main()
{
	in >> t;
	for (int x=1;x<=t;x++)
	{
		in >> c;
		a.resize(c);
		for (int i=0;i<c;i++) in >> a[i];
		in >> d;
		b.resize(d);
		for (int i=0;i<d;i++) in >> b[i];
		in >> n >> e;
		s.resize(0);
		for (int i=0;i<n;i++)
		{
			s.push_back(e[i]);
			if (s.size()>1) for (int j=0;j<c;j++) if (s[s.size()-1]==a[j][0] && s[s.size()-2]==a[j][1] || s[s.size()-1]==a[j][1] && s[s.size()-2]==a[j][0])
			{
				s.pop_back();
				s.pop_back();
				s.push_back(a[j][2]);
				j=c;
			}
			if (s.size()>1) for (int j=0;j<d;j++) for (int k=0;j<d && k<s.size()-1;k++) if (s[s.size()-1]==b[j][0] && s[k]==b[j][1] || s[s.size()-1]==b[j][1] && s[k]==b[j][0])
			{
				s.resize(0);
				j=d;
			}
		}
		out << "Case #" << x << ": [";
		if (s.size()>0)
		{
			out << s[0];
			for (int i=1;i<s.size();i++) out << ", " << s[i];
		}
		out << "]\n";
	}
	return 0;
}
