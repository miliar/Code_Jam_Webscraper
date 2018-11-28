#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

ifstream fin("B-large.in");  //A-small-practice.in  B-small-practice.in input.in
#define cin fin

ofstream fout("output.txt");
#define cout fout

#define FOR(i,n) for(int i=0; i<n; i++)
#define FOR1(i,n) for(int i=1; i<=n; i++)

typedef unsigned long long dword;

const int MAX=91;

char ac[MAX][MAX];
bool ad[MAX][MAX];

char a[101],b[101];

//int tc[MAXN];
//int ts[MAXN];


void main () {
	int c;
	cin>>c;
	FOR1(caz,c) //for(int caz=1; caz<=cases; ++caz )
	{
        FOR(i,MAX)
            FOR(j,MAX) { ac[i][j]=0; ad[i][j]=false; }
		int N,C,D;
		cin >> C;
        char c1,c2,c3;
        FOR(i,C){
            cin >> c1 >> c2 >> c3;
            ac[c1][c2] = c3;
            ac[c2][c1] = c3;
        }
        cin >> D;
        FOR(i,D){
            cin >> c1 >> c2;
            ad[c1][c2]=true;
            ad[c2][c1]=true;
        }
        cin >> N;
        FOR(i,N)
			cin>>a[i];
        int p=0;
        FOR(i,N){
            c1 = a[i];
            b[p++] = c1;
            if(p>1){
                c2 = b[p-2];
                if(ac[c1][c2]) { // combine
                    c3 = ac[c1][c2];
                    b[--p-1] = c3;
                    continue;
                } 
            }
            FOR(j,p-1){
               c2=b[j];
               if(ad[c1][c2]) p=0;
            }
        }
        cout << "Case #" << caz <<": " << "[";
        FOR(i,p) {
            if(i>0) cout << ", ";
            cout << b[i];
        }
        cout << "]" <<endl;
	}
	#ifndef cout
	  getchar();
    #endif
}