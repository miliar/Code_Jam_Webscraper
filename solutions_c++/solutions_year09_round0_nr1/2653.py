#include <fstream>
#include <vector>
#include <string>
using namespace std;

bool Find(string s, char c)
{
	for(int i=0;i<s.size();++i)
		if(s[i]==c) return true;
	return false;
}

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int l, d, n;
	in >> l >> d >> n;
	vector<string> v(d);
	string s;
	int i, j, k;
	getline(in,s);
	for(i=0;i<d;++i)
	{
		getline(in, s);
		v[i] = s;
	}
	bool ok = false;
	int last, res;
	string substr;
	for(i=0;i<n;++i)
	{
		res = 0;
		getline(in, s);
		for(j=0;j<d;++j)
		{
			last = 0;
			ok = true;
			for(k=0;k<l;++k)
			{
				if(s[last]!='(' && s[last]!=v[j][k])
				{
					ok = false;
					break;
				}
				else
				{
					if(s[last]==v[j][k])
					{
						++last;
						continue;
					}
					else
					{
						substr = "";
						++last;
						while(s[last]!=')') substr += s[last++];
						++last;
						if(!Find(substr, v[j][k]))
						{
							ok = false;
							break;
						}
					}
				}
				if(!ok) break;
			}
			if(ok) ++res;
		}
		out << "Case #" << i+1 << ": " << res << endl; 
	}
	out.close();
	in.close();
}