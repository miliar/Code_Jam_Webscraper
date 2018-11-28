/* Author: Zuo.Overmind.Zerg */
#include<cassert>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
//#include<deque>
//#include<functional>
//#include<iostream>
//#include<list>
#include<map>
//#include<set>
#include<vector>
using namespace std;

typedef long long i64;
typedef unsigned u32;
template<class _> void maz(_ &a,const _ b) {if(b>a)a=b;}
template<class _> void miz(_ &a,const _ b) {if(b<a)a=b;}

class Heap {
	private:
		int size,data[1000];
	public:
		void clear() {size=0;}
		bool empty() const {return !size;}
		int top() const {return data[0];}
		void pop() {pop_heap(data,data+size--);}
		void push(int x) {data[size++]=x;push_heap(data,data+size);}
};

int N,G;
int val[1000];
int num[1000];
Heap heap[10001];

bool test(int g) {
	int i,x,y,z;
	for(i=0;i<=10000;i++)heap[i].clear();
	for(i=0;i<N;i++) {
		x=val[i];
		y=num[i];
		while(y--) {
			if(heap[x].empty()) {
				if(x+g-1>val[N-1])return false;
				heap[x+1].push(g-1);
			} else {
				z=heap[x].top();
				heap[x].pop();
				if(z)z--;
				if(x+1<=10000)heap[x+1].push(z);
			}
		}
	}
	for(i=0;i<=10000;i++)if(!heap[i].empty()&&heap[i].top()!=0)return false;
	return true;
}

int solve() {
	if(N==0)return 0;
	int _l=1,_r=G,_m;
	while(_l<=_r) {
		_m=((_l+_r)>>1);
		if(test(_m))_l=_m+1;
		else _r=_m-1;
	}
	return _r;
}

void input() {
	int n,i,x;
	map<int,int> rec;
	map<int,int>::iterator it;
	scanf("%d",&n);
	for(i=0;i<n;i++) {
		scanf("%d",&x);
		rec.insert(make_pair(x,0)).first->second++;
	}
	N=0;
	G=0;
	for(it=rec.begin();it!=rec.end();++it) {
		val[N]=it->first;
		num[N]=it->second;
		G+=num[N++];
	}
}

int main() {
	int T,S;
	scanf("%d",&T);
	for(S=1;S<=T;S++) {
		input();
		printf("Case #%d: %d\n",S,solve());
	}
	return 0;
}
