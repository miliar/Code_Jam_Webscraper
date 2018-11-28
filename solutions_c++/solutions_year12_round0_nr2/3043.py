#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#include <cstring>
#include <fstream>
using namespace std;
#define all(x) (x).begin(),(x).end()

#define vs vector <string>
#define vi vector <int>
#define p(X) push_back((X))

#define fir(i,j,n) for(int (i)=(j);(i)<(n);(i)++)
#define fire(i,j,n) for(int (i)=(j);(i)<=(n);(i)++)
#define firr(i,j,n) for(int (i)=(j);(i)>(n);(i)--)
#define firre(i,j,n) for(int (i)=(j);(i)>=(n);(i)--)
#define tr(v,it) for(typeof(v.begin()) it=v.begin();it!=v.end();it++)

#define srt(v) sort((v).begin(),(v).end())
#define srtc(v) sort(v.begin(),v.end(),cmp)

#define _bc(i) __builtin_popcount(i)

string lower(string s) {for(int i=0;i<s.size();i++) s[i]=tolower(s[i]);return s;}
vector<string> sep(string s,char c) { string temp;vector<string> res;for(int i=0;i<s.size();i++) { if (s[i]==c) {if (temp!="") res.push_back(temp);temp="";continue;}temp=temp+s[i];}if (temp!="") res.push_back(temp);return res;}
template<class T> T toint(string s)
{
	stringstream ss(s);
	T ret;
	ss>>ret;
	return ret;
}
template<class T> string tostr(T inp)
{
	string ret;
	stringstream ss;ss<<inp;
	ss>>ret;
	return ret;
}
template<class T> void D(T A[],int n) {for(int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template<class T> void D(vector<T> A,int n=-1) {if (n==-1) n=A.size();for(int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}

int tot[110];
pair<int, int> data[110];
int N, S, P;

int dp[101][101];

int solve(int cn, int cs)
{
    if (cn >= N) {
        if (cs != S)
            return -2;
        return 0;
    }
    
    if (dp[cn][cs] != -1)
        return dp[cn][cs];
    int ret = -2;
    if (data[tot[cn]].first != -1)
    {
        int th = solve(cn + 1, cs);
        if (th != -2 && data[tot[cn]].first >= P)
            th++;
        if (th != -2) {
            if (ret == -2 || ret < th)
                ret = th;
        }
    }
    if (data[tot[cn]].second != -1 && cs < S)
    {
        int th = solve(cn + 1, cs + 1);
        if (th != -2 && data[tot[cn]].second >= P)
            th++;
        if (th != -2) {
            if (ret == -2 || ret < th)
                ret = th;
        }
    }
    
    //cout<<cn <<" "<<cs<<" "<<ret<<endl;
    return dp[cn][cs] = ret;
}
int main()
{
    memset(data, -1, sizeof(data));
    
    for(int n1 = 0; n1 <= 30; n1++) {
        for(int n2 = max(0, n1 - 2); n2 <= n1; n2++)
        {
            for(int n3 = max(0, n1 - 2); n3 <= n1; n3++) {
                if (n1 + n2 + n3 > 30) continue;
                int ttot = n1 + n2 + n3;
                if (n1 - n2 != 2 && n1-n3 != 2)
                    data[ttot].first = max(data[ttot].first, n1);
                else
                    data[ttot].second = max(data[ttot].second, n1);
            }
        }
    }
    
    int T;
    cin>>T;
    int kase = 0;
    while(T--) {
        ++kase;
        cin>>N>>S>>P;
        fir(i, 0, N) cin>>tot[i];
        memset(dp, -1, sizeof(dp));
        cout<<"Case #"<<kase<<": "<<solve(0, 0)<<endl;
    }
    return 0;
}