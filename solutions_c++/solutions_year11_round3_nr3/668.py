#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

ifstream fin("C-small-attempt0.in");  // input.in, C-small-attempt0.in, C-large.in
#define cin fin

ofstream fout("output.txt");
#define cout fout

#define FOR(i,n) for(int i=0; i<n; i++)
#define FOR1(i,n) for(int i=1; i<=n; i++)

typedef unsigned long long dword;
typedef long long dint;

const int MAXN=10000;
dword F[MAXN];

void main () {
	int c;
	cin>>c;
	FOR1(caz,c)
	{
		int N;
        dword L,H;
		cin >> N >> L >> H;
        FOR(i,N)
            cin >> F[i];        
        bool good;
        dword f;
        for(f=L;f<=H;f++){
            good=true;
            FOR(i,N)
                if(F[i]%f!=0 && f%F[i]!=0) { good=false; break; }
            if(good) break;
        }
        if(good) cout << "Case #" << caz <<": " << f <<endl;
        else cout << "Case #" << caz << ": " << "NO" <<endl;
	}
	#ifndef cout
	  getchar();
    #endif
}