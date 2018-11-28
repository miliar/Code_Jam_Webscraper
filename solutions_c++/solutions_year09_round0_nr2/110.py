#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
using namespace std;

int field[128][128];

struct UnionFind
{
	struct Node
	{
		int index;
		int rank;
		int size;
		Node *parent;
		Node(int t,Node * par): index(t),rank(0),size(1),parent(par)
		{;}
	};
	Node **arr;
	int SZ;
	void addNew(int n)
	{
		arr[n] = new Node(n,NULL);		
	}
	UnionFind(int n):SZ(n)
	{
		arr = new Node*[n];
		for(int i=0;i<n;++i)
		{
			arr[i] = new Node(i,NULL);
		}
	}
	~UnionFind(void)
	{
		for(int i=0;i<SZ;++i)
		{
			delete arr[i];
		}
	};
	void merge(const int a,const int b)
	{
		Node *pa = find_set(arr[a]),*pb = find_set(arr[b]);
		if(pa->rank > pb->rank)
		{
			pb->parent = pa;
			pa->size += pb->size;
		}
		else if(pa->rank < pb->rank){
			pa->parent = pb;
			pb->size += pa->size;
		}
		else if(pa != pb){pb->parent = pa;pa->size += pb->size;++(pa->rank);}
		
	}
	Node * find_set(Node *n)
	{
		if(n->parent == NULL || n->parent == n){return n;}
		n->parent = find_set(n->parent);
		return n->parent;
	}
	int find(int in)
	{
		return find_set(arr[in])->index;
	}
	int size_of(int in)
	{
		return find_set(arr[in])->size;
	}
};

int dr[] = {-1,0,0,1};
int dc[] = {0,-1,1,0};

int main(void)
{
	int CC;
	cin >> CC;
	for(int cn=1;cn <= CC;++cn)
	{
		int R,C;
		cin >> R >> C;
		for(int i=0;i<R;++i)
		{
			for(int j=0;j<C;++j)
			{
				cin >> field[i][j];
			}
		}
		UnionFind *uf = new UnionFind(R*C);
		for(int i=0;i<R;++i)
		{
			for(int j=0;j<C;++j)
			{
				int bestt = 999,bestsc = field[i][j];
				for(int t=0;t<4;++t)
				{
					const int NR = i+dr[t];
					const int NC = j+dc[t];
					if(NR < 0 || NR >= R || NC <0 || NC >= C)continue;
					if(field[NR][NC] < bestsc)
					{
						bestsc = field[NR][NC];
						bestt = t;
					}
				}
				if(bestt != 999)
				{
					uf->merge(i*C+j,(i+dr[bestt])*C+(j+dc[bestt]));
				}
			}
		}
		int ss = 0;
		map<int,int> ma;
		cout << "Case #" << cn << ":"<< endl;
		for(int i=0;i<R;++i)
		{
			for(int j=0;j<C;++j)
			{
				int g = uf->find(i*C+j);
				if(ma.find(g) == ma.end()){
					ma[g] = ss++;

				}
				cout << (char)('a'+ma[g]);
				if(j+1 == C){cout << endl;}
				else{cout << " ";}
			}
		}
	}
	return 0;
}
