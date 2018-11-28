#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

bool there(string a, int x, int y) {
	int cx = 0, cy = 0;
	for (int i=x;i<=y;i++) {
		if (a[i] == '(')
			cx++;
		else if (a[i] == ')')
			cy++;
	}
	if (cx == cy)
		return false;
	return true;
}

bool leaf(string a) {
	for (int i=0;i<a.size();i++) {
		if (isalpha(a[i]))
			return false;
	}
	return true;
}

int main() {
	FILE *fo;
    ifstream cin("A-large.in");
    fo = fopen("file.out", "wt");
	int t, l, an;
	cin >> t;
	for (int ts=0;ts<t;ts++) {
		fprintf(fo, "Case #%d:\n", ts+1);
		cin >> l;
		string s;
		int sz = 0;
		for (int i=1;i<=l+1;i++) {
			string k;
			getline(cin, k);
			if (!i)
				continue;
			s += k;
		}
		for (int j=0;j<s.size();j++) {
			if (!isalpha(s[j]) && !(s[j] >= '0' && s[j] <= '9') && s[j] != '.' && s[j] != ')' && s[j] != '(') {
				s.erase(s.begin()+j);
				j--;
			}
		}
		string cr;
		for (int j=0;j<s.size()-1;j++) {
			cr += s[j];
			if (s[j] == '(')
				cr += ' ';
			if (s[j+1] == '(' || s[j+1] == ')')
				cr += ' ';
			if (s[j] >= '0' && s[j] <= '9' && isalpha(s[j+1]))
				cr += ' ';
		}
		cr += s[s.size()-1];
		int cl[1000] = {0};
		for (int i=0;i<cr.size()-1;i++) {
			if (cr[i] == '(') {
				for (int j=i+1;j<cr.size();j++) {
					if (cr[j] == ')' && !there(cr, i+1, j-1)) {
						cl[i] = j;
						break;
					}
				}
			}
		}
		cin >> an;
		for (int i=0;i<an;i++) {
			string name;
			vector< string > h;
			cin >> name;
			int n;
			long double p = 1;
			cin >> n;
			for (int j=0;j<n;j++) {
				cin >> name;
				h.push_back(name);
			}
			sort(h.begin(), h.end());
			int f = 0;
			while (1) {
				string po = cr.substr(f+2, cl[f]-f-2);
				istringstream pfin(po);
				double pod;
				pfin >> pod;
				p *= 1.0000000*pod;
				if (leaf(po))
					break;
				int tp[2], idx;
				for (int j=f+1;j<cr.size();j++) {
					if (cr[j] == '(') {
						idx = j;
						break;
					}
				}
				tp[0] = idx;
				tp[1] = cl[idx]+2;
				string pos;
				pfin >> pos;
				if (binary_search(h.begin(), h.end(), pos))
					f = tp[0];
				else
					f = tp[1];
			}
			fprintf(fo, "%4.7f\n", p);
		}
	}
	return 0;
}