//	ID : pallab81
// 	PROG : C
// 	LANG : C++
// 	2011-05-07-16.02.04 Saturday
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

VS sNum;
VI iNum;
int N;

inline string getB( int num){
    bitset<20> bt(num);
return bt.to_string<char,char_traits<char>,allocator<char> >();
}
inline string addWrong( string s1, string s2 ){
    string res(LN(s1),' ');
    for(int i = LN(s1)-1 ; i>=0; --i){
        res[i] = (s1[i]==s2[i] ? '0' : '1' );
    }
return res;
}
inline bool checkPossible(){
    string res(20,'0');
    fo(i,0,N){
        res = addWrong(res,sNum[i]);
        //cout<<res<<"\n";
    }
return (count(res.begin(),res.end(),'1')==0 );
}
inline void read(){
    cin>>N;
    sNum.assign(N,"");
    iNum.assign(N,0);
    fo(i,0,N){
        cin>>iNum[i];
    }
    sort(iNum.begin(),iNum.end(),less<int>());
    fo(i,0,N){
        sNum[i]= getB(iNum[i]);
    }
}
inline void proc(int indi){
        if(checkPossible()){
            int res=0;
            fo(i,1,N){
                res+=iNum[i];
            }
            cout<<"Case #"<<indi<<": "<<res<<"\n";
        }
        else{
            cout<<"Case #"<<indi<<": NO\n";
        }
}
int main(){
    int case_;
    cin>>case_;
    foE(i,1,case_){
        read();
        proc(i);
    }
return 0;
}

