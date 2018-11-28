//	ID : pallab81
// 	PROG : A
// 	LANG : C++
// 	2011-05-07-05.33.49 Saturday
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

int n,d;
int res;
VVI vt;
VC ST;
// blue have to wait

inline void read(){
        char ch;
        int x;
        cin>>d;
        vt.assign(2,VI());
        ST.clear();
        fo(i,0,d){
            cin>>ch>>x;
            if(ch=='O')vt[0].pb(x);
            else vt[1].pb(x);
            ST.pb(ch);
        }
}
inline bool C1(int &nw, int indx, int I){
    if( indx >= SZ(vt[I]) )return false;


    int tobe = vt[I][indx];
    bool flag = false;
    if(tobe==nw){
        flag=true;
    }
    else if(tobe>nw){
        nw++;
    }
    else{
        nw--;
    }
return flag;
}

inline void proc(){

    res=0;
    int oNow = 1;
    int bNow = 1;
    int indx1=0; //for orange
    int indx2=0; //for blue

    while( true ){
        if( ST.empty() )break;
        char TOP = (*ST.begin());
        //cout<<TOP<<"\n";bip;
        if( TOP=='O' ){
                if( C1(oNow,indx1, 0) ){
                    ST.erase(ST.begin());
                    indx1++;
                }
                C1(bNow,indx2, 1);
        }
        else{
                if( C1(bNow, indx2, 1)){
                    ST.erase(ST.begin());
                    indx2++;

                }
                C1(oNow,indx1, 0);
        }
        res++;
    }
}
inline void print(int case_){
    cout<<"Case #"<<case_<<": "<<res<<"\n";
}

int main(){
    cin>>n;
    foE(i,1,n){
        read();
        proc();
        print(i);
    }

return 0;
}

