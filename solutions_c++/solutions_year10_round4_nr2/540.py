#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
const LL INF = 20000000000000000;
struct node{
	node * a,* b;
	LL cost;
	LL worst;

	LL best[20];
	node(LL cost, node * a=0, node * b=0):cost(cost), a(a), b(b),worst(min(a->worst, b->worst)){init();}
	node(LL cost, LL worsta, LL worstb):cost(cost), a(0), b(0), worst(min(worsta, worstb)){init();}
	void init(){
		for(int i =0; i<20; i++) best[i]=-1;
	}

	LL getBest(int x){
		if(best[x]!=-1) return best[x];
		else
		{
			if(a==0){
				if(x>worst) return best[x]=INF;
				else if(x==worst) return best[x]=cost;
				else return best[x]=0;
			}
			else{
				if(x>worst) return best[x]=INF;
				else if(x==worst) return best[x]=cost+a->getBest(x)+b->getBest(x);
				else return best[x]=min(cost+a->getBest(x)+b->getBest(x), a->getBest(x+1)+b->getBest(x+1));
			}
		}
	}

	~node(){if(a) delete a; if(b) delete b;}


};

int M[10000];
node * O[10000];
node * T[10000];

LL jeden(){
	int p; scanf("%d", &p);

	for(int i = 0; i<(1<<p); i++) scanf("%d", M+i);

	for(int i = 0; i< p; i++){
		if(i==0)
		for(int j = 0; j<1<<(p-i-1); j++)
		{
			int c; scanf("%d", &c);
			O[j]= new node(c, M[j<<1], M[(j<<1)+1]);
		}
		else{

			for(int j = 0; j<1<<(p-i-1); j++){
				int c; scanf("%d", &c);
				T[j] = new node(c,O[j<<1], O[(j<<1)+1]);
			}

			for(int j = 0; j<1<<(p-i-1); j++)
				O[j]=T[j];
		}
	}
	node * root = O[0];

	LL res = root->getBest(0);

	delete root;
	return res;
}

int main(int argc, char* argv[])
{
	int n; scanf("%d", &n);
	for(int i = 0; i<n; i++){
		printf("Case #%d: %lld\n", i+1, jeden());
	}

	return 0;
}

