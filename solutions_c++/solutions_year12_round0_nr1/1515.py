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

string read_line() {
	char str[300];
	fgets(str, 300, stdin);
	string cmd(str);
	
	//cmd = cmd.substr(0, sz(cmd)-1);
	return cmd;
}

char convert[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z' ,'t', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() 
{
	int tests;
	string str;
	
	scanf("%d\n", &tests);
	
	int cnt = 1;
	for(int i = 0; i < tests; i++) {
		str = read_line();
		string res = "";
		
		for(int j = 0; j < str.size(); j++) 
			res += str[j] != ' ' ? convert[str[j]-'a'] : ' ';
		
		cout << "Case #" << cnt << ": " << res << endl;
		
		cnt++;
	}
	
	return 0;
}














