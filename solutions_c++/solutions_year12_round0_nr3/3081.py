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

vector<pair<int, vector<int> > > data;
int totdata;
void fillup(int n)
{
    vector<int> th;
    int tenp = 1;
    int cn = n/10;
    int ndg = 1;
    while(cn) {tenp *= 10; cn/= 10;++ndg;}
    int nn = n;
    for(int i = 1; i < ndg; i++) {
        int fd = (nn%10);
        nn = (nn%10) * tenp + (nn/10);
        if (nn > n && nn <= 2000000)
            th.p(nn);
    }
    
    srt(th);
    int li = 0;
    int si = 0;
    while(li < th.size()) {
        th[si++] = th[li++];
        while(li < th.size() && th[li] == th[li - 1])
            li++;
    }
    th.resize(si);
    if (th.size())
        data.p(make_pair(n, th));
    totdata += th.size();
}

int main()
{
    totdata = 0;
    for(int i = 1; i <= 2000000; i++) {
        fillup(i);
    }
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++) {
        int A, B;
        cin>>A>>B;
        int ans = 0;
        for(int i = 0 ; i < data.size(); i++) {
            if (data[i].first < A) continue;
            if (data[i].first > B) break;
            for(int j = 0 ; j < data[i].second.size(); j++)
            {
                if (data[i].second[j] < A) continue;
                if (data[i].second[j] > B) break;
                ans++;
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}