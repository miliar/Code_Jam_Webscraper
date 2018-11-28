#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

string intstr (int n) {
	string str;
	for (;n; n/=10)
		str.push_back (n%10+'0');
	reverse (str.begin(), str.end());
	return str;
}
int strint (string str) {
	return atoi (str.c_str());
}

int main () {
	ifstream in ("csmall.in");
	ofstream out ("csmall.out");
	int n, a , b;
	vector <int> w (2000001);
	in >> n;
	for (int h =1; h <= n; ++h) {
		fill (w.begin(), w.end(), 0);
		in >> a >> b;
		string star = intstr (a);
	//	cout <<a << ' ' << b << endl;
		for (int c= a; c <= b; ++c) {
			string cur  = intstr (c), be = "0", str  = cur;
//			out << c << ' ' << cur << ' ' << be << endl;
			for (int d= 0;d != cur.size (); ++d) {
//				cout << str << endl;
				str = str.substr (1,str.size()-1) + string (1,str[0]);
				if (str < cur && str > be && str[0] != '0')
					be = str;
			}
			if (be >= star)
				w[c] =  w[strint(be)] + 1;
//			cout <<c << ' '<< be << ' ' << w[c] << endl;
		}
//		cout << endl;
		int ret = 0;
//		for (int c = a; c <= b; ++c)
//			cout << c << ' ' <<w[c] << endl;
		for (int c = a; c <= b;++c)
			ret += w[c];
		out << "Case #" << h << ": " <<  ret << endl;
	}
}
