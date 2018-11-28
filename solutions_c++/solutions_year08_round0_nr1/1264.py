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


long int min_c,CN,cn,S,Q,i,j,eng_c[100],s,q,sw_c,mid;
//VS Que;


int main(int argc, char** argv) {
        ifstream fin("input.txt");
	ofstream fout("output.txt");
try{string eng[1000],qu[10000],tmp;
     void count_rep(long int &min,string a[],string b[],long int c[],long int start);
     long int find_min_pos(long int,string a[],string b[],long int c[],long int start);
     int find_min(string a[],string b[],long int c[],long int &mid);
        getline(fin,tmp);
        CN=atoi(tmp.c_str());
//Que.clear();
       
	for (cn = 1; cn <= CN; ++cn) {
            getline(fin,tmp);
            S=atoi(tmp.c_str());
             
            cout<<"s="<<S<<endl;
            if(cn==10)
            {
            cout<<"a";
            }
            for(s=0;s<S;s++)
            {
            getline(fin,eng[s]);
           // cout<<eng[s]<<",";
            }
            getline(fin,tmp);
            Q=atoi(tmp.c_str());
            cout<<"q="<<Q<<endl;
            for(q=0;q<Q;q++)
            {
            getline(fin,qu[q]);
           // Que.push_back(qu[q]);
            //cout<<q<<"--"<<qu[q]<<",";
            }
             //cout<<endl;   
            
             mid=0;
             min_c=1001;
            sw_c=0;
             while(find_min(eng,qu,eng_c,mid)==1)
             {sw_c++;
              //mid=find_min_pos(min_c,eng,qu,eng_c,mid);
             //count_rep(min_c,eng,qu,eng_c,mid);
            }
//g2's_coode
cout << "Case #" << cn << ": " << sw_c<< '\n';
fout << "Case #" << cn << ": " << sw_c<< '\n';
		
        }
}
catch( char * str ) { cout << "Exception raised: " << str << '\n'; } 
catch(...){ cout << "Caught One!\n";    }
    return (EXIT_SUCCESS);
}
int find_min(string a[],string b[],long int c[],long int &mid)
{
    long int cc=0,i,j;
    for(s=0;s<S;s++){c[s]=0;}
    
    for(q=mid;q<Q;q++)
        {
        for(s=0;s<S;s++)
        {
        if(a[s]==b[q])
            {
            if(c[s]==0) cc++;
            c[s]++;
            
            }
    }
        if(cc==S)
        {
            mid=q;
            return 1;
        }
        }
    return 0;
}
void count_rep(long int &min,string a[],string b[],long int c[],long int start){
   
  for(s=0;s<S;s++){
      //  cout<<"searching for"<<a[s]<<"...[";      
            c[s]=0;
            for(q=start;q<Q;q++)
            {
            //cout<<b[q]<<",";
            if(a[s]==b[q])
                c[s]++;
            }
    //  cout<<c[s]<<"]"<<endl;
      if(c[s]<min)min=c[s];
            }
 cout<<"min is"<<min;
}
long int find_min_pos(long int m,string a[],string b[],long int c[],long int start)
{
    
    for(q=start;q<Q;q++)
            {
            //cout<<b[q]<<",";
            for(s=0;s<S;s++){
                if((a[s]==b[q])&&(c[s]==m)){return q;}
                }
            }
    //return q;
}
