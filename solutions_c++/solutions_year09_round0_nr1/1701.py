/*
ID: imranka1
PROG: test
LANG: C++
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


char buf[20];
int __L;
int read(int &ind)
{
	int ret=0;
	while(isdigit(buf[ind]) && ind<__L)
	{
		ret=ret*10+buf[ind++]-'0';
	}
	ind++;
	return ret;
}

char words[5001][17];
bool avl[16][26];
char inp[17];
int main() {
	int L,D,N;int idx;
	gets(buf);__L=strlen(buf);idx=0;
	L=read(idx);D=read(idx);N=read(idx);
	fir(i,0,D) {
		gets(words[i]);
	}
	fir(tc,0,N) {
		printf("Case #%d: ",tc+1);
		memset(avl,0,sizeof(avl));
		gets(inp);
		int pos=0;
		bool bopen=0;
		int len=strlen(inp);
		fir(i,0,len) {
			if (inp[i]=='(') {bopen=1;continue;}
			if (inp[i]==')') {bopen=0;++pos;continue;}
			if (!bopen) {
				avl[pos][inp[i]-'a']=1;
				++pos;
			}
			else {
				avl[pos][inp[i]-'a']=1;
			}
		}
		int cnt=0;
		fir(i,0,D) {
			bool tv=1;
			fir(j,0,L) {
				if (!avl[j][words[i][j]-'a']) {tv=0;break;}
			}
			if (tv) ++cnt;
		}
		printf("%d\n",cnt);
	}
    return 0;
}