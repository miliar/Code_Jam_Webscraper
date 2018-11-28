/*
 * Tutorial:
 * Question:
 * Author: Anshul Goel
 * Date:
 *
 */
#include <iostream>
#include <fstream>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <cassert>
#include <sstream>
#include <cmath>

using namespace std;

#define FOR(i, l, u) for(LET(i, l); i < (u); ++i)
#define REP(i, u) FOR(i, 0, u)
#define LET(x, a) __typeof(a) x(a)
#define IFOR(it, b, e) for(LET(it,b); it != e; ++it)
#define SHIFTL(i, n) ((i) << (n))
#define SHIFTR(i, n) ((i) >> (n))
#define POW2(n) (1 << (n))
#define MP(x, y) (make_pair(x, y))
#define SET(x, v) memset(&x, v, sizeof(x))
#define PB(x) push_back(x)
#define IPRINT(s, e) copy(s, e, ostream_iterator<__typeof(*s)>(cout, " "))
#define INRANGE(x, l, u) (x >= l && x < u)

#define DEBUG(x) if(_DEBUG) { x; }
#define PDBG(x) DEBUG(cerr << x << endl)
#define _DEBUG 1

typedef vector<int> v_i;
typedef vector<string> v_s;
typedef set<int> set_i;
typedef set<string> set_s;
typedef map<string,int> map_si;
typedef pair<int,int> p_i;



int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	ifstream cin("C-small-attempt0.in");
        ofstream cout("output.txt");
        int T,R,K,N;
        queue<int> Q,Q2;
        cin>>T;
        FOR(j,1,T+1)
        {
                  int temp;
          cin>>R;
          cin>>K;
          cin>>N;
          FOR(i,0,N)  {cin>>temp;
          Q.push(temp);
          }      
          
          int S=0,rem=K,val=0;
           FOR(i,0,R)
           {
            rem=K;
            while((!Q.empty()) && ((val=Q.front())<=rem)){rem-=val;Q.pop();Q2.push(val);}  
            while(!Q2.empty()){val=Q2.front();Q2.pop();Q.push(val);}
          //  cout<<S<<endl;
            
                    
            S+=K-rem;
                  
           }      
           while(!Q.empty())Q.pop();
           cout<<"Case #"<<j<<": "<<S<<endl; 
           
        }
        
  system("pause");


	//return 0;
}

