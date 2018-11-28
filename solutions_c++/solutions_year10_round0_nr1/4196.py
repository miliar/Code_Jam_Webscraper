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
	ifstream cin("A-small-attempt1.in");
        ofstream cout("outputA.txt");
	
	
	int T,T2,N;
    long K;
    int state,power;

	cin>>T;T2=T;
	while(T--)
	{
              cin>>N;
           cin>>K;   
  
   power=1;
   int tempP=0;
   state=0;
   int z=0;
   while(K--)
   {z++;
           //  cout<<"\n"<<K<<" snaps left\tState :"<<oct<<state<<"\nPower :"<<oct<<power<<endl;
           // system("pause");
             state=state^power;
             power=state-(state&(state+1));
             power=1+(power<<1);
             // cout<<"\n"<<z;
            //  cout<<" snaps\tState :"<<oct<<state<<"\nPower :"<<oct<<power<<endl;
             }
   
   cout<<"Case #"<<T2-T<<": ";
   int b=(power>>N)%2;
   
   if(b==1)
   cout<<"ON"<<endl;
   else cout<<"OFF"<<endl;
   
              
  }
	system("pause");


	//return 0;
}

