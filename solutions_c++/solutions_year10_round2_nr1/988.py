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


int f(const vector <string> &v, map <string,bool> &dir){
	string x="/";
	int res = 0, i=0, n=v.size();
	for(; i<n; ++i){
		x += v[i] + "/";
		if(!dir[x])break;
	}
	if(i == n)return res;
	dir[x] = true, res=1;
	for(i++;i<n;++i){
		x += v[i] +"/";
		res++;
		dir[x] = true;
	}
	return res;
}

int main(){
	freopen("data2.in","r",stdin);
	freopen("data.out","w",stdout);
	int T; scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		int n, m; scanf("%d %d", &n, &m);
		map <string,bool> dir;
		dir["/"]=true;
		char buffer[500];
		for(int i=0; i<n; ++i){
			scanf("%s", buffer);
			string path = buffer;
			for(int j=0, w=path.size(); j<w; ++j)
				if(path[j] == '/')path[j] = ' ';
			istringstream iss(path);
			string x = "/", folder;
			while(iss >> folder){
				x += folder + "/";
				dir[x] = true;
			}
		}
		int res = 0;
		for(int k=0; k<m; ++k){
			scanf("%s", buffer);
			string path = buffer;
			vector <string> v;
			for(int j=0, w=path.size(); j<w; ++j)
				if(path[j] == '/')path[j] = ' ';
			istringstream iss(path);
			string folder;
			while(iss >> folder){
				v.push_back(folder);
			}
			res += f(v,dir);
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}