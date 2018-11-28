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
typedef queue<int> qi;
typedef vector<ll> vl;
typedef unsigned long long ull;
typedef vector<ull> vul;
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

/*
have 3 arrays.. if you wish:
12:52 AM group_size[i] :: size of group i
12:52 AM ride_size[i] :: people in the ride when group i is first
12:53 AM next_first[i] :: index of group that will be first in the next ride after group i goes first
*/

int main()
{
	int test;
	ull R, K, N;
	ull group_size[1001];
	ull ride_size[1001];
	ull next_first[1001];
	map<int, bool> store;
	vul people;
	scanf("%d", &test);
	int cases = 0;
	while(test--){
		cases++;
		ull count, sum, earn = 0;
		
		people.clear();
		cin >> R >> K >> N;
		rep(i,N){
			
			ull temp;
			cin >> temp;
			people.pb(temp);
		}
		rep(i,N){
			
			group_size[i] = people[i];
			
		}
		int front = 0;
		int j = 0;
		rep(i,N){
		    int next_front;

		    j = i+1;
		    if (j == N) j = 0;
		    sum = people[i];

		    while (j != i){

		        sum += people[j];

		        if(sum > K){
		            sum -= people[j];
		            break;
		        }

		        j = (j < N) ?  (j+1)%N  : 0;  
		    }

		    ride_size[i] = sum;
		    next_first[i] = j;
		    //cout << "for " << i << " size,ride,next = " << people[i] << "," << sum << "," << j << endl;
		}
		int i = 0;
		while(R--){
			
			earn += ride_size[i];
			i = next_first[i];
		}
		
		printf("Case #%d: ", cases);
		//printf("%d\n" ,earn);
		cout << earn << endl;
		
	}
	return 0;
}