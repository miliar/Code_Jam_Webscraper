#include <iostream>
#include <algorithm>
#include <string>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <utility>
#include <sstream>
#include <map>
#include <queue>
#include <stack>
#include <complex>
#include <cctype>
#include <climits>
#include <fstream>
#include <iomanip>
#include <set>
using namespace std;

typedef complex<double> P;

const int N = 41;
char field[N][N];
int lt[N];
int ans, w;
map<string, int> visit;

void solve(int turn, int lim)
{
	if (turn >= ans) return;
	if (turn >= lim) return;
	
	string s = "";
	for (int i=0; i < w; ++i) s += (char)(lt[i]+'0');
	if (visit.find(s)!=visit.end() && visit[s]<=turn) {
		return;
	}
	visit[s] = turn;

	for (int i=0; i < w; ++i) cout << lt[i] << " ";
	cout << endl;

	int x = 0;
	bool isOk = true;
	for (int i=0; i < w; ++i) {
		if (lt[i] > i) {
			isOk = false;
		}
	}
	if (isOk) {
		ans = turn;
		return;
	}

	for (int i=0; i < w-1; ++i) {
		if (lt[i]<=i && lt[i+1]<=i+1) continue;
		swap(lt[i], lt[i+1]);
		solve(turn+1, lim);
		swap(lt[i], lt[i+1]);
	}
}

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");

	int T;
	for (in>>T; T>0; --T) {
		static int counter = 0;
		out << "Case #" << ++counter << ": ";
		cout << "Case #" << counter << ": ";
		
		in >> w;
		for (int i=0; i < w; ++i) {
			in >> field[i];
		}
		fill(lt, lt+N, 0);
		for (int i=0; i < w; ++i) {
			for (int j=0; j < w; ++j) {
				if (field[i][j]=='1') lt[i] = j;
			}
		}

		ans = 0;
		for (int i=0; i < w; ++i) {
			int x = i;
			if (lt[i]<=i) continue;
			for (int j=i; j < w; ++j) {
				if (lt[j] <= i) {
					x = j;
					break;
				}
			}
			for (int j=x; j > i; --j) {
				swap(lt[j], lt[j-1]);
				++ans;
			}
		}

		visit.clear();
//		ans = w*w+1;
		//for (int i=0 ; i<ans; ++i) {
	//		solve(0, ans);
		//}
		cout << ans << endl;
		out << ans << endl;
	}

	in.close();
	out.close();
	return 0;
}
