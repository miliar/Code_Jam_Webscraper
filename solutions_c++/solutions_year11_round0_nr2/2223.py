// google_jam.cpp : Defines the entry point for the console application.
//


#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>

#include <stdio.h>
#include <tchar.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz(v) ((int)v.size())
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
//#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
//#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const double eps = 1e-9;

#define LARGE

int N,nx;

int _tmain(int argc, _TCHAR* argv[])
{
#ifdef SMALL
	freopen("./data/B-small-attempt0.in", "rt", stdin);
	freopen("./data/B-small-attempt0.out", "wt", stdout);
#endif

#ifdef LARGE
	freopen("./data/B-large.in", "rt", stdin);
	freopen("./data/B-large.out", "wt", stdout);
#endif
	int n_combine, n_clear;
	string s;
	cin >> N;
	for (int nn=1; nn<=N; nn++){
		
		vs clear_element, combine_element;
		int element_count;
		string final_element = "", input_element;
		cout << "Case #" << nn << ": ";
		cin >> n_combine;
		for (int n=0; n<n_combine; n++){
			cin >> s;
			string s2 ="";
			s2 += s[1];
			s2 += s[0];
			s2 += s[2];
			combine_element.push_back(s);
			combine_element.push_back(s2);
		}
		cin >> n_clear;
		for (int n=0; n<n_clear; n++){
			cin >> s;
			string s2 ="";
			s2 += s[1];
			s2 += s[0];
			clear_element.push_back(s);
			clear_element.push_back(s2);
		}
		cin >> element_count;
		cin >> input_element;
		// done read
		
		for (int e=0; e<element_count; e++){
			if (final_element.length()<=0){
				final_element += input_element[e];
				continue;
			}
			//combination
			bool combi=false;
			for (int c=0; c<combine_element.size(); c++){
				if ((combine_element[c][1]==input_element[e])&&(combine_element[c][0]==final_element[final_element.length()-1])){
					final_element[final_element.length()-1] = combine_element[c][2];
					combi=true;
					break;
				}
			}
			if (!combi)
				final_element += input_element[e];
			// list clear
			for (int ce=0; ce<clear_element.size();ce++){
				if (final_element.length()<=0)
					break;
				if (final_element[final_element.length()-1]==clear_element[ce][0]){
					for(int ce2=0; ce2<final_element.length()-1;ce2++){
						if (final_element[ce2]==clear_element[ce][1]){
							final_element="";
							break;
						}
					}
				}
			}
		}
		if (final_element.length()<=0){
			cout << "[]"<<endl;
			continue;
		}
		cout << "[";
		for(int ce2=0; ce2<final_element.length()-1;ce2++){
			cout << final_element[ce2] << ", ";
		}
		if (final_element.size()>0)
			cout << final_element[final_element.length()-1];
		cout << "]" << endl;
	}
//		cout << time_counter << endl;
	return 0;
}

