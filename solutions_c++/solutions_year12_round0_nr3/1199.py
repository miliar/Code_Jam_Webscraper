
/*
* Author: yash_coder 
* Email: yash.171290@gmail.com
*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <stdio.h>
#include <sstream>
#include <list>
using namespace std ;
#define INF 0xffffff00
#define ESP 1e-6
#define FASTIO 1
#ifndef FASTIO
char *ipos, *opos, InpFile[20000000], OutFile[20000000], DIP[20];
inline int input(int flag=0) {
 
while(*ipos <= 32) ++ipos;
if ( flag ) return (*ipos++ - '0'); /* For getting Boolean Characters */
int x=0, neg = 0;char c;
while( true ) {
c=*ipos++; if(c == '-') neg = 1;
else {
if (c<=32 || c == '.' ) return neg?-x:x;
x=(x<<1)+(x<<3)+c-'0';
}
}
}
inline void output(int x,int flag) {
int y,dig=0;
while (x||!dig) { y=x/10;DIP[dig++]=x-((y << 3) + (y << 1))+'0';x=y;}
while (dig--) *opos++=DIP[dig];
*opos++= flag ? '\n' : ' ';
}
inline void InitFASTIO() {
ipos = InpFile; opos = OutFile;
fread_unlocked(InpFile,20000000,1,stdin);
}
inline void FlushFASTIO() {
	fwrite_unlocked(OutFile,opos-OutFile,1,stdout);
}
#endif
int toint(string s){
		int n;
			istringstream is(s);
				is>>n;
					return n;
}
string tostring(int n){
		stringstream is;
			is<<n;
				return is.str();
}
long long int modulo(int a,int b,int c){
	long long x=1,y=a; // long long is taken to avoid overflow of intermediate results
	while(b > 0){
		if(b%2 == 1){
			x=(x*y)%c;
		}
		y = (y*y)%c; // squaring the base
		b /= 2;
	}
	return x%c;
}
long long mulmod(long long a,long long b,long long c){
	long long x = 0,y=a%c;
	while(b > 0){
		if(b%2 == 1){
			x = (x+y)%c;
		}
		y = (y*2)%c;
		b /= 2;
	}
	return x%c;
}
int query(const vector<int> &tree, int a, int b) {
    if (a == 0) {
        int sum = 0;
        for (; b >= 0; b = (b & (b + 1)) - 1)
          sum += tree[b];
        return sum; 
    } else {
        return query(tree, 0, b) - query(tree, 0, a-1);
    }
}

// Increases value of k-th element by inc.
void increase(vector<int> &tree, int k, int inc) {
    for (; k < (int)tree.size(); k |= k + 1)
        tree[k] += inc;

}
map<pair<int,int>, int> dp;
int main () {
	int t,a,b;
	scanf("%d",&t);
	string str;
	int num;
	int len;
	int num1,num2;
	pair<int,int> tmp;
	char ch;
	int i,j;
	int yash;
	int den;
	for(yash=1;yash<=t;yash++){
	scanf("%d%d",&a,&b);
	dp.clear();
	str=tostring(a);
	len=str.size();
	den=pow(10,len-1);
	for(i=a;i<=b;i++){
	num1=i;
	num2=i;
	for(j=1;j<len;j++){
	num2=(num2%den)*10+(num2/den);
	tmp.first=min(num1,num2);
	tmp.second=max(num1,num2);
	if(tmp.first<tmp.second&&tmp.first>=a&&tmp.first<=b&&tmp.second>=a&&tmp.second<=b&&dp[tmp]==0){
	dp[tmp]=1;
	}
	}
	}
	printf("Case #%d: %d\n",yash,dp.size());
	}
	return 0 ;
}
