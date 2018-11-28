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

bool cmpPair(pair<string,char> a, pair<string,char> b)
{
	return a.first < b.first;
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

int sdvig(int x,int i) {
	return ((x >> i) & 0x1);
}


int getSum(int x,int y) {
	int out = 0;
	for(int i = 0 ; i < 32; ++i) {
		if((sdvig(x,i) == 0 && sdvig(y,i) == 1) || (sdvig(x,i) == 1 && sdvig(y,i) == 0)) {
			out = (out | (1 << i));
		}
	}
	return out;
}





int solve(vector<int> &mas) {
	int n;
	n = pow(2.0,mas.size() * 1.0);
	queue<int> q, q2;
	while(!q.empty())
		q.pop();
	int sum = 0;
	int sum2 = 0;
	int f = 1;
	int mm = -1;;
	for(int i = 1; i < n - 1; ++i) {
		sum = sum2 = 0;
		for(int j = 0; j < mas.size(); ++j) {
			//cout << sdvig(i,j);
			if(sdvig(i,j) == 1) {
				sum += mas[j];
				q.push(mas[j]);
				if(q.size() == 2) {
					int a = q.front();
					q.pop();
					int b = q.front();
					q.pop();
					int pp = getSum(a,b);
					//cout << pp << endl;
					q.push(pp);
				}
			} else {
				sum2 += mas[j];
				q2.push(mas[j]);
				if(q2.size() == 2) {
					int a = q2.front();
					q2.pop();
					int b = q2.front();
					q2.pop();
					int pp = getSum(a,b); 
					q2.push(pp);
				}
			}
		}
		//cout << endl;
		int a = q.front();
		q.pop();
		int b = q2.front();
		q2.pop();
		if(a == b) {
			mm = max(mm,sum);
		}
		
	}
	return mm;
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
	int t;
	scanf("%d",&t);
	int n;
	//cout << getSum(5,6) << endl;
	for(int i = 0; i < t; ++i) {
		scanf("%d", &n);
		vector<int> mas(n,0);
		
		for(int j = 0; j < n; ++j) {
			scanf("%d",&mas[j]);
		}
		int f = solve(mas);
		printf("Case #%d: ",i + 1);
		if(f == -1) {
			printf("NO\n");
		} else
			printf("%d\n",f);
	}
	return 0;
}

