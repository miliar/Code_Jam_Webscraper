/*
	Author: Imran Khan
*/
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
#include <cassert>
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
int group[1001];
int pos[2001];
long long totben[2001];
long long sum[2001];
int ind;
int main() {
	int tc;
	scanf("%d",&tc);int kase=0;
	while(tc--) {
		kase++;
		int r,k,n;scanf("%d%d%d",&r,&k,&n);
		printf("Case #%d: ",kase);
		long long total=0;
		fir(i,0,n) {scanf("%d",&group[i]);total+=group[i];}
		if (total<=k) {
			long long ans=(long long)total*(long long)r;
			cout<<ans<<endl;
		} else {
			memset(pos,-1,sizeof(pos));
			int si=0;ind=1;
			sum[0]=0;
			while(pos[si]==-1)
			{
				int ni=si;long long size=0;
				while(size+group[ni]<=k) {
					size+=group[ni];
					ni++;
					if (ni>=n) ni=0;
				}
				totben[ind]=size;
				sum[ind]=size;
				sum[ind]+=sum[ind-1];
				pos[si]=ind++;
				si=ni;
			}
			sum[ind]=sum[ind-1];
			long long ans=0;
			for(int i=1;i<ind && r;i++,r--)
			ans+=totben[i];
			if (r)
			{
				ans+=((long long)(r-1)/(ind-pos[si]))*(sum[ind]-sum[pos[si]-1]);
				ans+=sum[(r-1)%(ind-pos[si])+pos[si]]-sum[pos[si]-1];
			}
			cout<<ans<<endl;
		}
	}
    return 0;
}