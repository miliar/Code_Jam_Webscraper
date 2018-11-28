#pragma comment(linker, "/STACK:36777216")

#include <algorithm>
#include <iostream>
#include<stdio.h>
#include <string>
#include<sstream>   
#include<string.h>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<int,pii> p3i;
typedef long double ld;
typedef vector<ld> vd;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define SORT(a) sort((a).begin(),(a).end())

struct bi{
    int a[61];

    bi(){CL(a,0);}
    bi(string s){
        CL(a,0);
        REP(i,s.size())
            a[60-s.size()+1+i]=s[i]-'0';
    }
    bool bigger(bi s2){
        REP(i,61) if(a[i]!=s2.a[i])
            return a[i]>=s2.a[i];
        return true;
    }
    void sub(bi s){

        for(int  i=60;i>=1;i--){
            a[i]-=s.a[i];
            if(a[i]<0) a[i]+=10,a[i-1]--;
        }
    }
    void out(){
        int pos=0;
        while(pos<60 && !a[pos]) pos++;
        FOR(i,pos,61) cout<<a[i];
    }
    void add(bi s){
        for(int i=60;i>=0;i--){
            a[i]+=s.a[i];
            if(a[i]>=10) a[i]-=10,a[i-1]++;
        }
    }
    bool isNot0(){
        REP(i,61) if(a[i]) return 1;
        return 0;
    }
    void sh10(){
        REP(i,60) a[i]=a[i+1];
        a[60]=0;
    }
    void dec10(){
        for(int i=59;i>=0;i--) a[i+1]=a[i];        
    }
    void div(bi s){
        bi t;
        int num = 0;
        while(bigger(s)) num++,s.sh10();
        for(int i=0;i<=num;i++){
            while(bigger(s)){
                sub(s);
                t.a[60-num+i]++;
            }
            s.dec10();
        }
        REP(i,61) a[i]=t.a[i];
    }
    void mul(bi s){
        bi t;
        REP(i,61)REP(j,61)if(i+j-60>=0)
            t.a[i+j-60]+=a[i]*s.a[j];
        for(int i=60;i>=0;i--)
            if(t.a[i]>=10){
                t.a[i-1]+=t.a[i]/10;
                t.a[i]%=10;
            }
        REP(i,61) a[i]=t.a[i];
    }
};

bi ccin(){
    string s;
    cin>>s;
    return bi(s);
}

bi diff(bi s1,bi s2){
    if(s1.bigger(s2)) return s1.sub(s2),s1;
    else return s2.sub(s1),s2;
}

int n;
bi a[1111];

bi mod(bi a,bi b){
    bi t = a;
    t.div(b);
    t.mul(b);
    a.sub(t);
    return a;
}
bi gcd(bi a,bi b){
    while(a.isNot0()&&b.isNot0()){
        
        if(a.bigger(b))
            a=mod(a,b);
        else b=mod(b,a);
    }
    return a.add(b),a;
}

int main(){
#ifdef LocalHost
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int TC;
    cin>>TC;
    REP(tc,TC){
        cin>>n;
        REP(i,n) a[i]=ccin();
        bi g;
        REP(i,n)REP(j,i) 
            g=gcd(g,diff(a[i],a[j]));
        bi mn;
        REP(i,n){
            bi t = a[i];
            t.add(g);
            t.sub(bi("1"));
            t.div(g);
            t.mul(g);
            t.sub(a[i]);
            if(t.bigger(mn)) mn=t;
        }
        cout<<"Case #"<<tc+1<<": ";
        mn.out();
        puts("");
    }

    return 0;


}