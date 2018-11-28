/*******************************************************************
*                          CODE JAM 2013
*                    ROUND:                 qualification 
*                       CONTESTER:  yi
*                           Problem: A
*******************************************************************/
 
// headers
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#include <omp.h>
//#include <gmp>


//DEBUGING

#ifdef DEBUG
#define ASSEART(X)     if (!(X)) {printf("\n %s: assertion failed at line %d\n",__FILE__,__LINE__);exit(0);} 
#define PRINT(fmt, args...) printf("%s:%s:%d: "fmt, __FILE__, __FUNCTION__, __LINE__, args); 
#define PVAR(var) cout<<__FILE__<<":"<<__FUNCTION__<<":"<<__LINE__<<":    "<<#var<<" = "<<var<<endl;
#define PLINE(array,n) \
printf("\n%s:%s:line %d : "#array"[0:%d]=\n",__FILE__, __FUNCTION__, __LINE__,n);\
for(register size_t __i__=0;__i__<n;__i__++) \
    cout<<__i__<<" ";\
cout<<endl;\
for(register size_t __i__=0;__i__<n;__i__++) \
        cout<<array[__i__]<<" ";\
        cout<<endl;
#define PMAP(array,n,m,fmt) {\
printf("%s:%s:line %d : "#array"[0:%d][0:%d]=\n",__FILE__, __FUNCTION__, __LINE__,n,m);\
cout<<"  ";\
for(register size_t __j__=0;__j__<m;__j__++) \
cout<<__j__;\
cout<<endl;\
for(register size_t __i__=0;__i__<n;__i__++) {\
    cout<<__i__;\
    for(register size_t __j__=0;__j__<m;__j__++) \
        printf(fmt,array[__i__][__j__]);\
    cout<<endl;\
}\
}
#define PBIN(n) {\
        int i,bit[256];\
        for(i=0;i<sizeof(n)*8;i++) {bit[i]=n%2;n>>=1;}\
        for(;i>0;i--) {cout<<bit[i-1];}\
    }
#define EVAL(cmd) cmd
#else
#define PMAP(array,n,m,fmt) 
#define ASSEART(X)
#define PVAR(var)
#define PRINT(fmt, args...) 
#define PLINE(array,n)
#define PBIN(n)
#define EVAL(cmd)
#endif
//Helpers
#define repeat(n,__i__) for(register size_t __i__=0;__i__<n;__i__++) 
#define all(cnt) cnt.begin(),cnt.end()
#define forall(cnt,it) for(typeof(cnt.begin()) it=cnt.begin();it!=cnt.end();it++)
#define RCMAP(array,n,m) \
    for(register size_t __i__=0;__i__<n;__i__++) {\
        string __l__;\
        getline(cin,__l__);\
        for(register size_t __j__=0;__j__<m;__j__++) {\
            array[__i__][__j__]= __l__[__j__];\
        }\
    }
#define RMAP(array,n,m) \
    for(register size_t __i__=0;__i__<n;__i__++) {\
        string __l__;\
        getline(cin,__l__);\
        for(register size_t __j__=0;__j__<m;__j__++) {\
            istringstream(__l__)>>array[__i__][__j__];\
        }\
    }
typedef long long ll;

//Possible Template classes (Graph, Geometric...).         

//Test Case 
class TestCase {
    //Helpers
    //static const int Limit=1;
    string myresult;
    //variables list
    
    //Implement details
    char board[4][4];
public:
    //Input
    TestCase(istream& input) {
        init(input);
    }
    template<class _stream>
    void init(_stream& input=cin) {
        string line;
        RCMAP(board,4,4);
        getline(input,line);
        PMAP(board,4,4,"%c");
    };
    bool isWinner(char c) {
        bool win;
        for (int i=0; i<4; i++) {
        win=true;
          for (int j=0; j<4; j++) 
            if(board[i][j]!=c && board[i][j] !='T') win&=false;
        if(win) return true;
        }
        for (int i=0; i<4; i++) {
        win=true;
          for (int j=0; j<4; j++) 
            if(board[j][i]!=c && board[j][i] !='T') win&=false;
        if(win) return true;
        }
        win=true;
        for(int i=0;i<4;i++) {
            if(board[i][i]!=c && board[i][i] !='T') win&=false;
        }
        if(win) return true;
        win=true;
        for(int i=0;i<4;i++) {
            if(board[i][3-i]!=c && board[i][3-i] !='T') win&=false;
        }
        if(win) return true;
        return false;
    }
    bool complete() {
        for(int i=0;i<4;i++)
           for(int j=0;j<4;j++)
               if(board[i][j] == '.') return false;
        return true;
    }
    //solve the problem
    void solve() {
        if(isWinner('X')) {myresult="X won"; return;}
        if(isWinner('O')) {myresult="O won"; return;}
        if(complete()) {myresult="Draw";return;}
        myresult="Game has not completed";
        return ;
    };
    //format output
    string result() {
        return myresult;
    };
};
    
// ------------------------ Start @ Fri Apr 12 21:58:46 EDT 2013 ---------------------------------------

int main() {
    int nCase;
    string line;
    getline(cin,line);
    istringstream(line)>>nCase;
    vector<TestCase> testcases;
    for(int i=0;i<nCase;i++) testcases.push_back(TestCase(cin));
#pragma omp parallel for num_threads(4)
    for(int i=0;i<nCase;i++) testcases[i].solve();
    for(int i=0;i<nCase;i++) cout<<"Case #"<<i+1<<": "<<testcases[i].result()<<endl;

}

//Statistics

//------- finished small at Sat Apr 13 13:42:41 EDT 2013--------------
//------- finished large at Sat Apr 13 13:44:28 EDT 2013--------------
