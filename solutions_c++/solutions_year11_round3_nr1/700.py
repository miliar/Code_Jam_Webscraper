#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

ifstream fin("A-large.in");  // input.in, A-small-attempt0.in, A-large.in
#define cin fin

ofstream fout("output.txt");
#define cout fout

#define FOR(i,n) for(int i=0; i<n; i++)
#define FOR1(i,n) for(int i=1; i<=n; i++)

typedef unsigned long long dword;
typedef unsigned long long dint;

const int MAX=50;
char A[MAX][MAX];
//int B[MAX][MAX];
//int W;

void main () {
	int c;
	cin>>c;
	FOR1(caz,c)
	{
		int R,C;
		cin >> R >> C;
        //W=0;
        FOR(i,R){
            FOR(j,C){
                char c;
                cin >>c;
                A[i][j]=c; //(c=='#'?:1:0);
                //if(c=='#') W++;
            }
        }
        bool good = true;
        FOR(i,R)
            FOR(j,C)
                if(A[i][j]=='#')
                    if(i<R-1 && j<C-1) 
                        if(A[i+1][j]=='#' && A[i][j+1]=='#' &&  A[i+1][j+1]=='#'){
                            A[i+1][j] = A[i][j+1]='\\';
                            A[i][j] = A[i+1][j+1] ='/';
                        } else good=false;
                    else good=false;
        dword r=0;
        cout << "Case #" << caz <<":" <<endl;
        if(!good) cout <<"Impossible" <<endl;
        else FOR(i,R){
               FOR(j,C) cout <<A[i][j];
                 cout <<endl;
               }
	}
	#ifndef cout
	  getchar();
    #endif
}