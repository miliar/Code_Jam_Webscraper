#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

ifstream fin("A-large.in");  //A-small-practice.in  B-small-practice.in input.in
#define cin fin

ofstream fout("output2.txt");
#define cout fout

#define FOR(i,n) for(int i=0; i<n; i++)
#define FOR1(i,n) for(int i=1; i<=n; i++)

typedef unsigned long long dword;

const int MAXN=101;

int P[MAXN];
char R[MAXN];

void main () {
	int c;
	cin>>c;
	FOR1(caz,c) //for(int caz=1; caz<=cases; ++caz )
	{
		int n; //string result;
		cin>>n;
		FOR(i,n)
			cin  >> R[i] >> P[i];
        int po=1, pb=1;
        int to=0, tb=0, t=0;
        FOR(i,n){
            int p=P[i];
            if(R[i]=='O'){
                to = max(tb, to + abs(po - p)) + 1;
                po = p;

            } else {
                tb = max(to, tb + abs(pb - p)) + 1;
                pb = p;
            }
        }        
        t = max(to,tb);
		cout << "Case #" << caz <<": " << t <<endl;
	}
	#ifndef cout
	  getchar();
    #endif
}