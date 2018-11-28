#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

ifstream fin("B-small-attempt2.in");  // input.in, B-small-attempt0.in, B-large.in
#define cin fin

ofstream fout("output.txt");
#define cout fout

#define FOR(i,n) for(int i=0; i<n; i++)
#define FOR1(i,n) for(int i=1; i<=n; i++)

typedef unsigned long long dword;
typedef long long dint;

const int MAXN=1000001;
int A[MAXN];
bool B[MAXN];
int L,N;
double t,best;

void simulate(){
    double time=0;
    for(int i=0; i<N; i++){
        int d = A[i];
        double bt=0;
        if(B[i]) { bt = time+2*d-t; if(bt<0) bt=0; if(bt>2*d) bt=2*d; }
        time += 2*d - bt/2.0;
        if(time>=best) break;
    }
    if(time<best) best = time;
}

void solve(int b,int s){
    if(b==0 || s>=N) {
        simulate(); 
        return;
    }
    for(int i=s; i<=N-1; i++){ // not needed for last one
        B[i]=true; // add booster
        solve(b-1,i+1);
        B[i]=false; // remove
    }
}



void main () {
	int cz;
	cin>>cz;
	FOR1(caz,cz)
	{
		int C;
        cin >> L >> t >> N >>C;
        FOR(i,C)
            cin >> A[i];
        for(int i=C; i<N; i++)
            A[i] = A[i%C];
        best = 0;
        for(int i=0; i<N; i++) { B[i]=false; best+= 2*A[i]; }
        solve(L,0);
        char bests[100];
        sprintf(bests,"%.0f",best);
        cout << "Case #" << caz <<": " << bests <<endl;
	}
	#ifndef cout
	  getchar();
    #endif
}