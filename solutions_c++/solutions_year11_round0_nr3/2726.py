#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

ifstream fin("C-small-attempt0.in");  //A-small-practice.in  B-small-practice.in input.in
#define cin fin

ofstream fout("output.txt");
#define cout fout

#define FOR(i,n) for(int i=0; i<n; i++)
#define FOR1(i,n) for(int i=1; i<=n; i++)

typedef unsigned long long dword;

const int MAXN=1001;

int t[MAXN];
//int tc[MAXN];
//int ts[MAXN];

int x1,x2,s1,s2,m,xt,st;

void solve(int i, int n){

    //if(m >= st-s1 && m>= st-s2) return; // can't obtain better

    if(i>=n) {
        if(x1==x2 && s1>0 && s2>0 ) {
            if (s1>m) m = s1;
            if (s2>m) m = s2;
        }
        return;
    }

    x1 ^= t[i];
    s2 += t[i];
    solve(i+1,n);
    x1 ^= t[i];
    s2 -= t[i];

    x2 ^= t[i];
    s1 += t[i];
    solve(i+1,n);
    x2 ^= t[i];
    s1 -= t[i];

}

void main () {
	int c;
	cin>>c;
	FOR1(caz,c) //for(int caz=1; caz<=cases; ++caz )
	{
        xt=0;
        st=0;
		int n; //string result;
		cin >> n;
        FOR(i,n){
			cin>>t[i];
            xt ^= t[i];
            st += t[i];
        }
        x1=x2=s1=s2=m=0;
        solve(0,n);
        if(m==0)
            cout << "Case #" << caz <<": " << "NO" <<endl;
        else
            cout << "Case #" << caz <<": " << m <<endl;
	}
	#ifndef cout
	  getchar();
    #endif
}