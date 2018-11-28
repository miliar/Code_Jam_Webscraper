/*
** Khamitbekov Madi
** Kazakhstan, Almaty
** Kazakh-Turkish High School, 2011
*/
#include <algorithm>
#include <iostream>
#include <string.h>
#include <utility>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cstdio>   
#include <cmath>
#include <queue>
#include <ctime>
#include <list>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef vector <vector <int> >  vvi;
typedef vector <pair <int, int> >  vpi;
typedef queue  <pair <int, int> > qpi;

#define abs(x) ((x) > 0 ? (x) : -(x))
#define all(v) (v).begin(), (v).end()
#define sq(x) ((x)*(x))
#define len length()
#define pb push_back
#define mp make_pair
#define inf 7777777
#define eps (1e-7)
#define sz size()
#define s second
#define f first
 

string get[100];
string kill[100];
int c, d;

bool ok (char a, char b) {
	for (int i = 0; i < c; i++) {
		if (get[i][0] == a && get[i][1] == b) return 1;
		if (get[i][0] == b && get[i][1] == a) return 1;
	}
	return 0;
}

char make (char a, char b) {
	for (int i = 0; i < c; i++) {
		if (get[i][0] == a && get[i][1] == b) return get[i][2];
		if (get[i][0] == b && get[i][1] == a) return get[i][2];
	}
}
bool can_kill (char a, char b) {
	for (int i = 0; i < d; i++){
		if (kill[i][0] == a && kill[i][1] == b) return 1;
		if (kill[i][0] == b && kill[i][1] == a) return 1;
	}
	return 0;
}
char ch, st[10000];
int k = 0;
bool will_kill () {
	for (int i = 1; i < k; i++)
		if (can_kill(st[i], st[k])) return 1;
	return 0;
}
		

int main ()
{
	#ifndef ONLINE_JUDGE
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);
	#endif

	int T;           
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> c;
		cout << "Case #" << t+1 << ": ";
		for (int i = 0; i < c; i++)	cin >> get[i];
		cin >> d;
		int n;
		for (int i = 0; i < d; i++)	cin >> kill[i];
		cin >> n;
		k = 0;
		for (int i = 0; i < n; i++) {
			cin >> ch;
			st[++k] = ch;
			if (k == 1) continue;
			while (ok (st[k-1], st[k])) st[k-1] = make(st[k-1],st[k]), k--;
			if (will_kill()) k = 0;
		}
		cout << "[";
		for (int i = 1; i < k; i++)	cout << st[i] << ", ";
		if (k)	cout << st[k];
		cout << "]\n";
	}

	return 0;
}
    
