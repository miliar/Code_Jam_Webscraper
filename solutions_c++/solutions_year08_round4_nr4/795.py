#include <stdio.h>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <stack>
#include <queue>

#define S(t,z) scanf("%"#t,&z)
#define P(t,z) printf("%"#t,z)
#define PLN(t,z) printf("%"#t"\n",z)
#define PS(t,z) printf("%"#t" ",z)

#define Z(t,n) memset((t),(0),sizeof((t)[0])*(n))
#define MCP(d,s,n) memcpy((d),(s),sizeof((s)[0])*(n))

#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)

#define LL long long

using namespace std;

int i,j,x,w,v,k,m,n;
int CC;
LL res;
//vector <int> v1;
//vector <int> v2;
//priority_queue<int> PQ;
//queue<int>Q;
//stack<int>S;
using namespace std;

long long int power(LL i) {
    if (i<=1 )
	return 1;
    else 		
	return power(i-1)*i;
}

long long int size(string S, vector<int> v) {
    LL tmp(0);
    string copy(S);
    char prev(0);
    int start = 0;	
    for (int i=0;i<S.length();i++) {
    
        if ( i && (i%k == 0) )
	    start += k;
	    
	S[i] = copy[ v[i%k] + start ];
	
    }
    
    for (int i=0;i<S.length();i++) {
	if ( S[i]!=prev || i ==0) {
	    tmp++;
	    prev = S[i];
	}
    }
    
//    cout <<" tmp "<<tmp<< " "<<S<<endl;
    return tmp;
}

int main(){
   int C;
   S(d,C);
   CC=0;
   while (CC++,C--) {
     string s;
     cin >> k;
     cin >> s;
     vector <int> v;
     
     REP(i,k) {
        v.push_back(i);
     }
     
     LL pow = power(k);
     
     res = -1;
//     cout <<"pow "<<pow<<endl;
     REP(i,pow) {
        LL tmp = size (s,v);
	if (tmp < res || res < 0) {
	    res = tmp;
	}
        next_permutation(v.begin(),v.end());
     }
     		
	
     cout <<"Case #"<<CC<<": "<<res<<endl;
   }
    return 0;
}

