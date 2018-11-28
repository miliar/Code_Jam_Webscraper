#ifndef __MYLIB_H
#define __MYLIB_H

#include<iostream>
#include<algorithm>
#include<sstream>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<utility>	// pair, make_pair
using namespace std;

#include<stdio.h>
#include<math.h>
#include<string.h>
#include<limits.h>

#define all(vec)		vec.begin(),vec.end()
#define rall(vec)		vec.rbegin(),vec.rend()
#define sz(r)			r.size()
#define digits(i)		(int)((log(i)/log(10))+1)
#define dround(num)		(int)floor(num+0.5)	// Rounds num to int (int)num+(<.5 to 0, > .5 to 1)
#define strtoint(str)		(extract_int(str)[0])

#define REP(i,n) 		for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) 		for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

#define first_bit_index(num) __builtin_ctz(num) // count trailing zeros
#define last_bit_index(num)  __builtin_clz(num) // count leading zeros
#define UNDEFINED_BIT	     32
#define test_bit(num, bit)   ((num & 1 << bit) != 0)
#define num_bits(num)	     __builtin_popcount(num)

#define inf 	INT_MAX
#define mn_inf  INT_MIN

typedef stringstream sstream;
typedef struct point{
	int x, y;
	point(){};
	point(int a, int b){x=a;y=b;}
}point;

int X[] = {0, 1, -1, 0, -1, 1, -1, 1};
int Y[] = {1, 0, 0, -1, -1, 1, 1, -1};


/**
 * Convert int to string
*/
string inttostr(int num)
{
	string res;
	sstream s;

	s << num; s >> res;
	return res;
}

/**
 * Extract int from string
*/
vector<int> extract_int(string str)
{
	sstream s;
	s << str;

	vector<int> res;
	int num = -1;

	while((s >> num))
		res.push_back(num);

	return res;
}

#endif 

/* End of my lib */

int digits = 0;
map<int, bool> mp;

long long count_it(int n, int a, int b) {
	//string str = inttostr(n);
	
	if(n <= 10) return 0;
	
	long long cnt = 0;
	int tt = n, rem;
	for(int i = 0; i < digits-1; i++) {
//		cnt++;
		rem = tt%10;
		tt = tt/10 + rem*(int)pow(10, digits-1);
		
		if(tt > b) continue;

		if((rem != 0) && (tt > n) && (tt <= b) && mp[tt] != true) {
			mp[tt] = true;
			cnt++;
		}
	}
	
	//cout << n << " " << cnt << endl;
	
	return cnt;
}

void cnt_digits(int a) {
	digits = 0;
	
	while(a) {
		a /= 10;
		digits++;
	}
	
	//cout <<  digits << endl;
}

int main() 
{
	int tests;
	cin >> tests;
	
	for(int i = 1; i <= tests; i++) {
		int a, b;
		cin >> a >> b;
		
		cnt_digits(a);
		
		long long cnt = 0;
		for(int j = a; j < b; j++) {
			cnt += count_it(j, a, b);
			mp.clear();
		}
			
		cout << "Case #" << i << ": " << cnt << endl;
	}
	
	return 0;
}














