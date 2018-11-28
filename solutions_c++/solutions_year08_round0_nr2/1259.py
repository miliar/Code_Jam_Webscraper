// 
// File:   codejam_src1_draft_1.cc
// Author:	G2 (Jit Ray Chowdhury)
//jit.ray.c@gmail.com
// Created on July 16, 2008, 11:21 PM
//

#include <stdlib.h>

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>

#if defined (__GNUC__) && (__GNUC__ <= 2)
#include <hash_map>
#include <hash_set>
#else
#include <ext/hash_map>
#include <ext/hash_set>
using namespace __gnu_cxx;
#endif
using namespace std;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define sz size()
#define FORA(i,c) REP(i,size(c))
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define SORT(x) sort(all(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
//
// 
//
int main(int argc, char** argv) {
        int time_val(string ,int);
        ifstream fin("input.txt");
	ofstream fout("output.txt");
	string A, D;
	long int CN, cn, t,n,N,NA,NB,T,ca,cb,NA_D[100],NA_A[100],NB_D[100],NB_A[100],i,j;

	fin >> CN;

	for (cn = 1; cn <= CN; ++cn) {
            fin>>T;
            
                fin >> NA >> NB ;
                N=NA+NB;
                ca=NA;
                cb=NB;
                cout<<"n="<<N<<"t="<<T<<endl;
               
                
                for (n = 1; n <= NA; ++n) {
                    fin >> D >> A ;
                    NA_D[n-1]=time_val(D,0);
                    NA_A[n-1]=time_val(A,T);
                     cout<<NA_D[n-1]<<"--"<<NA_A[n-1]<<endl;
                    }cout<<endl;
                for (n = 1; n <= NB; ++n) {
                    fin >> D >> A ;
                    NB_D[n-1]=time_val(D,0);
                    NB_A[n-1]=time_val(A,T);
                     cout<<NB_D[n-1]<<"--"<<NB_A[n-1]<<endl;
                    }
        sort(NA_D,NA_D+NA);
        sort(NB_D,NB_D+NB);
        sort(NA_A,NA_A+NA);
        sort(NB_A,NB_A+NB);
         if(cn==9){
                    cout<<endl;
                }
        for(int i=0,j=0;i<NA;i++)
        {
              for(;j<NB;j++)
              {
                  if(NA_A[i]<=NB_D[j])
                  {
                      cb--;
                      j++;
                      break;
                  }
                  
              }
             
        }
        for(int i=0,j=0;i<NB;i++)
        {
              for(;j<NA;j++)
              {
                  if(NB_A[i]<=NA_D[j])
                  {
                      ca--;
                      j++;
                      break;
                  }
                  
              }
             
        }
//g2's_coode
cout << "Case #" << cn << ": " << ca << " " << cb << '\n';
fout << "Case #" << cn << ": " << ca << " " << cb << '\n';
		
        }
  
    return (EXIT_SUCCESS);
}

int time_val(string S,int T){return(T+atoi(S.substr(0,2).c_str())*60+atoi(S.substr(3,4).c_str()));}