#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define RREPEAT(i,a,b) for(int i=a;i>=b;--i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) RREPEAT(i,n-1,0)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define INF (int)1<<30
#define vi vector<int>
#define vs vector<string>
#define pb push_back
#define mkp make_pair
#define ll unsigned long long int
#define uli unsigned long int
#define MAX (int)1e6

using namespace std;

ifstream fin ("A-large.in");
ofstream fout ("A-large.out");
#define cin fin
#define cout fout
int main() {
    int t=0;
    cin>>t;
    REP(T,t) {
		int n,k;
		cin>>n>>k;
		cout<<"Case #"<<T+1<<": "<<(((k+1)%(1<<n))?"OFF":"ON")<<endl;
    }
    system("pause");
    return 0;
}
