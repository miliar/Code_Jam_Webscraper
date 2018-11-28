#define _USE_MATH_DEFINES
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
/*maded by demidoff*/
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>


using namespace std;
#pragma comment(linker, "/STACK:64000000")


#define p(x) cout<<#x<<":"<<x<<"\n"
#define INF (int)(1e10)
#define INFL (int)(1e18)
#define PB push_back
#define MP make_pair
#define PRIME 31


typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pii64;
typedef vector<int> vi;
typedef vector<ll> vi64;
typedef vector< vi > vii;
typedef vector< vi64 > vii64;
typedef vector< pii > vpii;
typedef vector < pii64 > vpii64;

bool cmpInt(int a, int b)
{
	return a < b;
}

bool cmpPair(pii a, pii b)
{
	return a.second < b.second;
}

int gcd(int a, int b)
{
	if(b == 0)
		return a;
	else 
		gcd(b,a%b);
}

ll getHash(string &str) {
	//cout << str << endl;
	ll sum = 0;
	ll p_pow = 1;
	for(int i = 0; i < str.size(); ++i) {
		sum += (str[i] - 'a' + 1) * p_pow;
		p_pow *= PRIME;
	}
	return sum;
}

void updateTree(vector<int> &mas, int i, int l, int r, int a, int b,int sum)
{
	if(a > b)
		return;
	if(l == a && b == r) {
		mas[i] += sum;
	} else {
		int m = (l + r) / 2;
		updateTree(mas, i * 2, l, m, a, min(b,m), sum);
		updateTree(mas, i * 2 + 1, m + 1, r, max(m + 1, a), b, sum);
		
	}
}


int getTree(vector<int> &mas, int i, int l, int r, int pos)
{
	//p(i);
	if(l == r) {
		//cout << mas[i] << endl;
		return mas[i];
	}
	int m = (l + r) / 2;
	if(pos <= m)
		return mas[i] + getTree(mas, i * 2, l, m,pos);
	else
		return mas[i] + getTree(mas, i * 2 + 1, m + 1, r,pos);
}


int solve(list<int> &orange,list<int> &blue,list<char> &q)
{
	char currentBot;
	int orangePos, bluePos;
	orangePos = bluePos = 1;
	int sum = 0;

	while(!q.empty()) {
		currentBot = q.front();
		q.pop_front();
		//cout << currentBot << endl;
		if(currentBot == 'O') {
			int a1,a2;
			a1 = orange.front();
			orange.pop_front();
			if(blue.empty()) {
				sum += abs(orangePos - a1) + 1;
				orangePos = a1;
			} else {
				a2 = blue.front();
				int st = a2 - bluePos;
				int length = abs(a1 - orangePos);
				sum += length + 1;
				length += 1;
				orangePos = a1;
				if(st > 0) {
					if(length <= st) {
						bluePos += length;
					} else {
						bluePos = a2;
					}
				} else {
					if(length <= -st) {
						bluePos -= length;
					} else {
						bluePos = a2;
					}
				}
			}
		} else if(currentBot == 'B') {
			int a1,a2;
			a1 = blue.front();
			blue.pop_front();
			if(orange.empty()) {
				sum += abs(a1 - bluePos) + 1;
				bluePos = a1;
			} else {
				a2 = orange.front();
				int st = a2 - orangePos;
				int length = abs(a1 - bluePos);
				sum += length + 1;
				length += 1;
				bluePos = a1;
				if(st > 0) {
					if(length <= st) {
						orangePos += length;
					} else {
						orangePos = a2;
					}
				} else {
					if(length <= -st) {
						orangePos -= length;
					} else {
						orangePos = a2;
					}
				}
			}
		}

	}
	return sum;
}



#define INPUT_ON 1
#define INPUT_TXT 1
#define file_name "test"
int main()
{
	if(INPUT_ON) {
		if(INPUT_TXT) {
			freopen("input.txt","r",stdin);
			freopen("output.txt","w",stdout);
		} else {
			freopen(file_name".in","r",stdin);
			freopen(file_name".out","w",stdout);
		}
	}
	int n;
	int t;
	int cnt;
	scanf("%d",&t);
	list<int> orange, blue;
	list<char> q;
	char c;
	int tmp;
	for(int i = 0; i < t; ++i) {
		scanf("%d",&cnt);
		for(int j = 0; j < cnt; ++j) {
			scanf("%*c%c", &c);
			scanf("%d",&tmp);
			q.push_back(c);
			if(c == 'O') {
				orange.push_back(tmp);
			} else if(c == 'B') {
				blue.push_back(tmp);
			}
		}
		printf("Case #%d: %d\n",i+1,solve(orange,blue,q));
		q.clear();
		orange.clear();
		blue.clear();
	}
	
	
	return 0;
}