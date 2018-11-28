#pragma warning(disable:4018)  // signed/unsigned mistatch
#pragma warning(disable:4244)  // w64 to int cast
#pragma warning(disable:4267)  // big to small -- possible loss of data
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4800)  // forcing int to bool
#pragma warning(disable:4996)  // deprecations
#include "assert.h"
#include "ctype.h"
#include "float.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "stdarg.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "utility"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
#include "iostream"
using namespace std;

typedef long long i64;
#define all(v) (v).begin(), (v).end()
typedef long long i64;
template <class T> void make_unique(T& v) {sort(all(v)); v.resize(unique(all(v)) - v.begin());}
using namespace std;

char grid1[100][100];
char grid2[100][100];

void rotate(int n){
	for(int i=0; i<n; ++i){
		for(int j=0; j<n; ++j){
			grid2[j][n-1-i] = grid1[i][j];
		}
	}
	//gravity
	for(int j=0; j<n; ++j){
		string x;
		for(int i=n-1; i>=0; --i)
			if(grid2[i][j]!='.')x+=grid2[i][j];
		for(int i=n-1, k=0, m=x.size(); k<m && i>=0; --i, ++k)
			grid2[i][j] = x[k];
		for(int i=n-1-x.size(); i>=0; --i)
			grid2[i][j] = '.';
	}
}
bool f(char c, int n, int k){
	for(int i=0; i<n; ++i){
		for(int j=0; j<n; ++j){
			if(grid2[i][j]!=c)continue;
			int x = 0;
			for(int w=i-1; w>=0 && w>=i-(k-1); --w)
				if(grid2[w][j]==c)++x;
			if(x==k-1)return true;
			x = 0;
			for(int w=i+1; w<n && w<=i+(k-1); ++w)
				if(grid2[w][j]==c)++x;
			if(x==k-1)return true;
			x=0;
			for(int w=j-1; w>=0 && w>=j-(k-1); --w)
				if(grid2[i][w]==c)++x;
			if(x==k-1)return true;
			x = 0;
			for(int w=j+1; w<n && w<=j+(k-1); ++w)
				if(grid2[i][w]==c)++x;
			if(x==k-1)return true;
			x=0;
			for(int w=1; w<k && i-w >=0 && j-w >=0; ++w)
				if(grid2[i-w][j-w]==c)++x;
			if(x==k-1)return true;
			x=0;
			for(int w=1; w<k && i-w >=0 && j+w <n; ++w)
				if(grid2[i-w][j+w]==c)++x;
			if(x==k-1)return true;
			x=0;
			for(int w=1; w<k && i+w <n && j-w >=0; ++w)
				if(grid2[i+w][j-w]==c)++x;
			if(x==k-1)return true;
			x=0;
			for(int w=1; w<k && i+w <n && j+w <n; ++w)
				if(grid2[i+w][j+w]==c)++x;
			if(x==k-1)return true;
		}
	}
	return false;
}
void print(int n){
	for(int i=0; i<n; ++i){
		printf("%s\n",grid2[i]);
	}
}
int main(){
	freopen("data2.in","r",stdin);
	freopen("data.out","w",stdout);
	int T; scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		int n,k; scanf("%d %d", &n, &k);
		for(int i=0; i<n; ++i)
			scanf("%s",grid1[i]);
		rotate(n);
		bool red = f('R',n,k);
		bool blue = f('B',n,k);
		printf("Case #%d: ", t);
		//print(n);
		if(red && blue)printf("Both\n");
		else if(red && !blue)printf("Red\n");
		else if(!red && blue)printf("Blue\n");
		else printf("Neither\n");
	}
	return 0;
}