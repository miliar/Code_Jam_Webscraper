#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>
#include<map>
#include<string>
#include<deque>
using namespace std;

#define M 1440
#define N 256
#define INF 1000000000

struct train{
	int a,b,ty;
} p[N];
int p_cnt;
bool cmp(train& x,train& y){ return x.a<y.a;}

struct node{
	int ti,w;
	node(int ti=0,int w=0):ti(ti),w(w){}
};
bool operator<(node& x,node& y){ return x.ti>y.ti;}
template<class Item,int __SIZE>class Heap{
public:
	Item array[__SIZE];
	int n;
	int size(){return n;}
	void init(){n=0;}
	void push(Item x){
		array[n++]=x;
		push_heap(array,array+n);
	}
	Item pop(){
		pop_heap(array,array+n);
		return array[--n];
	}
};
int main()
{	

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		int t,na,nb;
		scanf("%d%d%d\n",&t,&na,&nb);
		p_cnt=0;
		while(na--){
			int xa,ya,xb,yb;
			scanf("%2d:%2d %2d:%2d",&xa,&ya,&xb,&yb);
			p[p_cnt].a=xa*60+ya;
			p[p_cnt].b=xb*60+yb+t;
			p[p_cnt++].ty=1;
		}
		while(nb--){
			int xa,ya,xb,yb;
			scanf("%2d:%2d %2d:%2d",&xa,&ya,&xb,&yb);
			p[p_cnt].a=xa*60+ya;
			p[p_cnt].b=xb*60+yb+t;
			p[p_cnt++].ty=2;
		}
		sort(p,p+p_cnt,cmp);
		int ra=0,rb=0;
		int ptr=0;
		Heap< node, N > que;
		que.init();
		int la=0,lb=0;
		for(int i=p[0].a;i<M&&ptr<p_cnt;i++){
			while(que.size()&&que.array[0].ti==i){
				if(que.array[0].w==1) la++;
				else lb++;
				que.pop();
			}
			if(p[ptr].a>i) continue;
			while(p[ptr].a==i){
				if(p[ptr].ty==1){
					if(la>0){
						la--;
					}else
						ra++;
					que.push(node(p[ptr].b,2));
				}else{
					if(lb>0){
						lb--;
					}else
						rb++;
					que.push(node(p[ptr].b,1));
				}
				ptr++;
			}
		}
		printf("%d %d\n",ra,rb);
	}
	return 0;
}