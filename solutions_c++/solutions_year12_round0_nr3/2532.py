#include <iostream>
#include <vector>
#include <cstdio>
#include <sstream>
#include <set>

using namespace std;

bool is_g(string a, string b)
{
	if (a.size() > b.size()) {
		return true;
	}
	for (int i=0; i<a.size(); i++) {
		if (a[i] < b[i]) {
			return false;
		} else if (a[i] > b[i]) {
			return true;
		}
	}
	return true;
}

int main()
{
	int t;
	scanf("%d",&t);
	for (int j=1; j<=t; j++) {
		int A,B,res=0;
		string As,Bs;
		scanf("%d %d",&A,&B);
		stringstream sa;
		sa << A;
		sa >> As;
		stringstream sb;
		sb << B;
		sb >> Bs;
		for (int i=A; i<B; i++) {
			stringstream ss;
			string s;
			ss << i;
			ss >> s;
			string Cs = s;
			set<string> sset;
			for (int k=1; k<s.size(); k++) {
				s.push_back(s[0]);
				s.erase(s.begin());
				if (s!=Cs) {
					if (is_g(s,Cs) && is_g(Bs,s)) {
						sset.insert(s);
					}
				}
			}
			res += sset.size();
		}
		printf("Case #%d: %d\n",j,res);
	}
	return 0;
}
