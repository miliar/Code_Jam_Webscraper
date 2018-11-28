#include <iostream>   
#include <sstream>   
#include <cstdio>   
#include <cstdlib>   
#include <cmath>   
#include <memory>   
#include <cctype>   
#include <string>   
#include <vector>   
#include <list>   
#include <queue>   
#include <deque>   
#include <stack>   
#include <map>   
#include <set>   
#include <algorithm>   
using namespace std;  
   
#define FOR(i,a,b) for(int (i) = (a); (i) < (b); ++(i))  
#define RFOR(i,a,b) for(int (i) = (a)-1; (i) >= (b); --(i))  
#define CLEAR(a) memset((a),0,sizeof(a))  
#define INF 1000000000  
#define PB push_back  
#define ALL(c) (c).begin(), (c).end()  
#define pi 2*acos(0.0)  
#define SQR(a) (a)*(a)  
#define MP make_pair  
#define MAX 75000
#define MOD 1000000007
   
typedef long long Int;  

string a;
string b;
char A[512];

int main()
{
	freopen("C:\\Users\\Віталік\\Desktop\\GCJ 2012\\Qual\\A-small-attempt1.in", "r", stdin);
	freopen("C:\\Users\\Віталік\\Desktop\\GCJ 2012\\Qual\\A-small-attempt1.out", "w", stdout);

	a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	b = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

	FOR (i,0,512)
		A[i] = '-';
	FOR (j,0,a.size())
		A[a[j]] = b[j];
	A['q'] = 'z';
	A['z'] = 'q';

	int T;
	cin >> T;
	getchar();
	FOR (t,0,T)
	{
		string s;
		getline(cin, s);
		FOR (j,0,s.size())
			if (s[j] != ' ')
				s[j] = A[s[j]];
		cout << "Case #" << t+1 << ": " << s << endl;
	}
	
	return 0;
} 