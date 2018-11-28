//	ID : pallab81
// 	PROG : B
// 	LANG : C++
// 	2011-05-07-13.46.37 Saturday
//
// 	"I have not failed, I have just found 10000 ways that won't work.
//


#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <bitset>

#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>

using namespace std;

#define  CI( x ) scanf( "%d", &x )

#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VC vector<char>
#define VVC vector<VC >
#define VB vector<bool>
#define VVB vector<VB >
#define PAIR pair<int,int>
#define VP vector<PAIR >
#define fo(i,st,ed) for(int i = st; i < ed ; ++i)
#define foE(i,st,ed) for(int i = st; i <= ed ; ++i)
#define foit(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define bip system("pause")
#define mk make_pair
#define f first
#define s second
#define pb push_back
#define SZ(X) (int)(X).size()
#define LN(X) (int)(X).length()
#define ll long long
#define IO ifstream cin(".in") ; ofstream cout(".out");

map< pair<char,char>, char  > frnd;
map< pair<char,char>, int  > enemy;

int nFrnd,nEnemy;
vector< char > lst;

inline void print(int indi){
    cout<<"Case #"<<indi<<": [";
    string ss="";
    fo(i,0,SZ(lst)){
        cout<<ss<<lst[i];
        ss=", ";
    }
    cout<<"]\n";
return ;
}

inline void read(){
    frnd.clear();
    enemy.clear();
    cin>>nFrnd;
    fo(i,0,nFrnd){
        char f1,f2,f3;
        cin>>f1>>f2>>f3;
        frnd[mk(f1,f2)] = f3;
        frnd[mk(f2,f1)] = f3;
    }
    cin>>nEnemy;
    fo(i,0,nEnemy){
        char f1,f2;
        cin>>f1>>f2;
        enemy[ mk(f1,f2) ]=1;
        enemy[ mk(f2,f1) ]=1;
    }
}
inline bool updateFrnd(){
    if( SZ(lst)<=1 )return false;
    fo(i,1,SZ(lst)){
        char f1 = lst[i-1];
        char f2 = lst[i];
        if( frnd.count( mk(f1,f2) ) ){
//            lst.erase(lst.begin()+ max(0,i-1));
//            lst.erase(lst.begin()+ max(0,i-1));
            lst.erase(lst.begin()+ i-1);
            lst.erase(lst.begin()+ i-1);
            lst.pb( frnd[ mk(f1,f2) ] );
            return true;
        }
    }
return false;
}
inline bool updateEnemy(){
    if( SZ(lst)<=1 )return false;
    fo(i,0,SZ(lst)){
        fo(j,i+1,SZ(lst)){
            char f1 = lst[i];
            char f2 = lst[j];
            if( enemy.count(mk(f1,f2)) ){
                lst.clear();
                return false;
            }
        }
    }
return false;
}
inline void doOperation(){
    while( updateFrnd()==true ){ ;
       // print();
    } //update frnd ok

    while( updateEnemy()==true ){ ;
        //print();
    } //update enemy ok
}
inline void readMain(){
    int nIteam;
    cin>>nIteam;
    lst.clear();
    fo(i,0,nIteam){
        char x; cin>>x;
        lst.pb(x);
        doOperation();
    }
}

int main(){
    int case_;
    cin>>case_;
    foE(i,1,case_){
        read();
        readMain();
        print(i);
    }
return 0;
}

