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

const int MAXN=100;
int A[MAXN][MAXN];
int WS[MAXN];
int WC[MAXN];
double WP[MAXN];
double OWP[MAXN];
double OOWP[MAXN];


void main () {
	int c;
	cin>>c;
	FOR1(caz,c)
	{
		dword N;
		cin >> N;
        FOR(i,N){
            WS[i]=WC[i]=WP[i]=0;
            char c;
            FOR(j,N){
                cin >> c;
                A[i][j] = (c=='.'?-1:(c=='1'?1:0));
                WS[i] += (c=='1'?1:0);
                WC[i] += (c=='.'?0:1);                
            }
            if(WC[i]>0) WP[i] = WS[i]/(double)(WC[i]);
        }
        FOR(i,N){
            double s=0;
            FOR(j,N)
                if(A[i][j]>=0 && WC[j]>1)
                    s += (WS[j]-A[j][i])/(double)(WC[j]-1); // wp
            OWP[i]= s/(double)(WC[i]);
        }
        FOR(i,N){
            double s=0;
            FOR(j,N)
                if(A[i][j]>=0)
                    s+= OWP[j];
            OOWP[i] = s/(double)(WC[i]);
        }
        dword r=0;
        cout << "Case #" << caz <<":" <<endl;
        FOR(i,N){
            double r;
            r = 0.25 * WP[i] + 0.5* OWP[i] + 0.25* OOWP[i];
            char rs[40];
            sprintf(rs,"%.12f",r);
            cout << rs <<endl;
        }
	}
	#ifndef cout
	  getchar();
    #endif
}