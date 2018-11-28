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
#define repd(i, n) for (int i((n) - 1); i >= 0; --i)
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

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
static int dot(vector<int> a, vector<int> b){
	
	int ret = 0;
	rep(i,a.sz){
		
		ret += a[i] * b[i];
	}
	return ret;
}
struct g_node{
	
	int from, to, w;
	g_node(){}
	g_node(int from, int to, int w){
		
		this -> from = from;
		this -> to = to;
		this -> w = w;
	}
};

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

	scanf("%d", &test);
	int cas = 0;
	
	
	while(test--){
		cas++;
		int ret = 0;
		
		int N;
		cin >> N;
		
		int ai, bi;
		vector<int> A;
		vector<int> B;
		rep(i,N){
			
			
			cin >> ai >> bi;
			A.pb(ai);
			B.pb(bi);
		}
		//sort(A.begin(), A.end());
		//sort(B.begin(), B.end());
		//cout << A.sz << " " << B.sz << endl;
		rep(i,A.sz){
			
			int j = i+1; if(j == A.sz) break;
			//cout << A[i] << " " << A[j] << " " << B[j] << " " << B[i] << endl;
			if(A[i] < A[j] && B[j] < B[i] || A[i] > A[j] && B[j] > B[i]) ret++;
			else continue;
		}
		
		printf("Case #%d: ", cas);
		if(ret == 0) printf("0\n");
		else printf("%d\n", ret);
		
	}
	return 0;
}