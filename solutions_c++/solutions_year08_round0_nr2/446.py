#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int maxn = 300;

vector< vector<bool> > mp;
vector <bool> cover(maxn);
vector <int> link(maxn);
int n;

bool find(int i)
{
  for (int k = 0; k < n; k ++)
    if (mp[i][k] && !cover[k])
    {
      int q = link[k];
      link[k] = i;
      cover[k] = true;
      if (q == - 1 || find(q)) return true;
      link[k] = q;
    }
  return false;
}

void maxbmatch()
{
  fill(link.begin(), link.end(), - 1);
  for (int i = 0; i < n; i ++)
  {
    fill(cover.begin(), cover.end(), false);
    find(i);
  }
}

int readtm(ifstream& inp) {
	string t;
	inp >> t;
	return ((t[0]-'0')*10+t[1]-'0')*60+((t[3]-'0')*10+t[4]-'0');
}

void readlist(ifstream &inp, vector< pair<int, int> >& a, int n) {
	for (int i = 0; i < n; i++)
	{
		int s = readtm(inp);
		int t = readtm(inp);
		a.push_back(make_pair(s, t));
	}
}

void main() {
	ifstream inp("b.in");
	ofstream out("b.out");
	int cases;
	inp >> cases;
	for (int id=1; id<=cases; id++) {
		int na, nb, t;
		inp >> t >> na >> nb;
		n = na+nb;
		mp = vector< vector<bool> >(n, vector <bool> (n, false));
		vector< pair<int, int> > a, b;
		readlist(inp, a, na);
		readlist(inp, b, nb);
		for (int i=0; i<na; i++) {
			for (int j=0; j<nb; j++) {
				if (a[i].second+t <= b[j].first) {
					cout << i << "->" << j << endl;
					mp[i][j+na] = true;
				}
				if (b[j].second+t <= a[i].first) {
					cout << i << "<-" << j << endl;
					mp[j+na][i] = true;
				}
			}
		}
		maxbmatch();
		int oa = na, ob = nb;
		for (int i=0; i<na; i++) if (link[i] != -1) oa--;
		for (int i=na; i<n; i++) if (link[i] != -1) ob--;
		out << "Case #" << id << ": " << oa << " " << ob << endl;
	}
}
