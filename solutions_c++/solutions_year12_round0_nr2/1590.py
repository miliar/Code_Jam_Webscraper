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

int find_sol(int sum, int p) {

	int surp = 0, not_surp = 0, both = 0;
	
	for(int a = 0; a <= 10; a++) {
		for(int b = 0; b <= 10; b++) {
			for(int c = 0; c <= 10; c++) {
				if(a+b+c != sum) continue;
				else if(abs(a-b) > 2 || abs(a-c) > 2 || abs(b-c) > 2) continue;
				
				if(a >= p || b >= p || c >= p) {
					if(abs(a-b) == 2 || abs(a-c) == 2 || abs(b-c) == 2) surp = 1;
					else if(abs(a-b) < 2 && abs(a-c) < 2 && abs(b-c) < 2) not_surp = 1;
				}
			}
		}
	}
	
	if(surp == 1 && not_surp == 1) return 1;
	else if(not_surp == 1) return 2;
	else if(surp == 1) return 3;
	
	return 0;
}

int main() 
{
	int tests;
	cin >> tests;
	
	for(int i = 1; i <= tests; i++) {
		int n, s, p;
		cin >> n >> s >> p;
		
		vector<int> sums(n);
		
		int not_surp = 0, both = 0, surp = 0, ret = 0;

		for(int j = 0; j < n; j++) {
			cin >> sums[j];
			
			int res = find_sol(sums[j], p);			

			if(res == 1) both++;
			else if(res == 2) not_surp ++;
			else if(res == 3) surp++;
		}

		ret += not_surp+both;
			
		if(surp >= s) ret += s;
		else ret += surp;
		
		cout << "Case #" << i << ": " << ret << endl;
	}
	
	return 0;
}














