#include <cstring>
#include <string.h>
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
#include <sstream>
#include <fstream>


using namespace std;

#define max(a,b) (a > b ? a : b)
#define min(a,b) (a < b ? a : b)
#define rep(i,n) for(int i=0; i < (int)n; i++)
#define rep1(i,a,b) for(int i = (int)a; i < (int)b; i++)
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(), v.rend()
#define pb push_back
#define sz size()
#define em empty()
#define mp make_pair

typedef vector<string> vs;
typedef vector<int> vi;
typedef vector< vector<int> > vii;
typedef long long int ll;
typedef vector<double> vd;
typedef vector<pair<int, int> > pii;
typedef stringstream ss;
typedef complex<double> point;
typedef vector<point> poly;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

int newsx[] = {0, 1, -1, 0};
int newsy[] = {1, 0, 0, -1};
int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

bool point_in_poly(poly p, point new_p){
	
	int i, j = p.sz - 1;
	bool odd_nodes = false;
	rep(i,p.sz){
		
		if(p[i].imag() < new_p.imag() && p[j].imag() >= new_p.imag() || p[j].imag() < new_p.imag() && p[i].imag() >= new_p.imag() )
		{
			
			if( (p[i].real() + (new_p.imag() - p[i].imag())) / ( (p[j].imag() - p[i].imag()) * (p[j].real() - p[i].real()) < new_p.real() ))
			{
				
				odd_nodes = !odd_nodes;
			}
		}
		j = i;
	}
	return odd_nodes;
}

int main()
{
	int test;
	ll N, K;
	scanf("%d", &test);
	int i = 0;
	while(test--){
		i++;
		
		cin >> N >> K;
		
		printf("Case #%d:", i);

		string s = (K % (2 << N-1)) == (2 << N-1) - 1 ? " ON" : " OFF";
	    cout << s << endl;
		
		
	}
	return 0;
}