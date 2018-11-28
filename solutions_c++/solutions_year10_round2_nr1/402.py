#define _GLIBCXX_DEBUG
//Arash Rouhani
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>
#include <fstream>
#include <numeric>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <bitset>

using namespace std;

typedef long long LL;
typedef pair < int, int > II;
typedef pair < int, II > I_II;
typedef vector < int > VI;
typedef vector < II > VII;
typedef vector < VI > VVI;
typedef vector < VII > VVII;
typedef vector < VVI > VVVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef vector < char > VC;
typedef vector < VC > VVC;
typedef stringstream SS;
typedef set < int > SI;

#define sz(c) (int((c).size()))
#define all(c) (c).begin(), (c).end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)
#define sford(type, e, start, stop) for(type e=start; e>=stop; e--)
#define foru(var, stop) sfor(int, var, 0, stop)
#define ford(var, start) sford(int, var, start, 0)
#define mp make_pair

template <class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
template <class T> string vectorToString(vector < T > v, string seperator){
	ostringstream oss;
	tr(v, e)
	oss << *e << seperator;
	oss.flush();
	return oss.str();
}

int currId;

struct Dir{
	map < string, Dir > subDirs;
	bool exist;
	int id;
	Dir(){
		exist = false;
		id = currId++;
	}
};

int main(){
	int nTestCases;
	cin >> nTestCases;
	sfor(int, testCase, 1, nTestCases+1){
		currId = 0;
		Dir root;
		root.exist = true;
		int n, m;
		cin >> n >> m;
		VS existing(n);
		tr(existing, it) cin >> *it;
		VS newDirs(m);
		tr(newDirs, it) cin >> *it;

		//process wanted (new) directories
		tr(newDirs, it){
			string s = *it;
			tr(s, it2) if(*it2 == '/') *it2= ' ';
			SS ss(s);
			VS vs;
			string temp;
			while(ss >> temp) vs.push_back(temp);
			Dir* now = &root;
			tr(vs, it2){
				string p = *it2;
				now = &(now->subDirs[p]);
			}
		}

		set < int > visited;
		visited.insert(0);
		tr(existing, it){
			string s = *it;
			tr(s, it2) if(*it2 == '/') *it2= ' ';
			SS ss(s);
			VS vs;
			string temp;
			while(ss >> temp) vs.push_back(temp);
			Dir* now = &root;
			tr(vs, it2){
				string p = *it2;
				now = &(now->subDirs[p]);
				visited.insert(now->id);
			}
		}

		int ans =currId - sz(visited);
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}











