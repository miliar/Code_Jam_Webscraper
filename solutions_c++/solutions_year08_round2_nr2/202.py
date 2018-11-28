#include<iostream>
#include<set>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;

#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
void print(set<int> s){cout << "Printing the set" << endl;set<int>::iterator itr;for(itr = s.begin() ; itr != s.end() ; itr++)cout << *itr << " " ;cout << endl;}

const int SIZE = 2000;
set<int> factors[SIZE];
int N;

struct DisjointSets{
	
	int parent[SIZE], rank[SIZE];
	
	DisjointSets(){
		//Initially, each node is in a tree by itself, so its rank is zero and the parent is itself
		memset(rank, 0, sizeof rank);
		for(int i = 0 ; i < SIZE ; i++)parent[i]=i;
	}
	
	int find(int e){
		return parent[e]==e ? e : parent[e]=find(parent[e]);
	}
	
	void Union(int e1, int e2){
		int p1 = find(e1), p2 = find(e2);
		if(p1==p2)return;
		if(rank[p1]==rank[p2])rank[p1]++;
		if(rank[p2]>rank[p1])swap(p1,p2);
		parent[p2] = p1;
	}
};

///////////////////////

int A, B, P;

int main(){

	//freopen("1.in", "rt", stdin);
	freopen("B-small.in", "rt", stdin);
	freopen("B-small.out", "wt", stdout);
	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);
	
	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){
		cin >> A >> B >> P;
		int i;
		for(int nn = A ; nn <= B ; nn++){
			factors[nn-A].clear();	
			//factor nn
			int i,a=1,n=nn;
			for(i = 2; i*i <= n; i+=a,a=2){
				if(n%i)continue;
				if(i >= P)factors[nn-A].insert(i);
				while(n%i==0)
					n/=i;
			}
			if(n > 1 && n >= P)factors[nn-A].insert(n);
		}
			
		DisjointSets ds;
		bool again = true;
		while(again){
			again = false;
			for(i = A ; i <= B ; i++)
				for(int j = A ; j <= B ; j++){
					int p1 = ds.find(i-A);
					int p2 = ds.find(j-A);
					if(p1 == p2)continue;//same set
					
					FOREACH(it,factors[p1]){
						if(factors[p2].find(*it) != factors[p2].end()){
							ds.Union(p1,p2);
			
							int p = ds.find(i-A);
							FOREACH(it1, factors[p1])
								factors[p].insert(*it1);
							FOREACH(it1, factors[p2])
								factors[p].insert(*it1);
								
							again = true;
						}
					}
				}
		}
		
		set<int> s;
		for(i = A; i <= B ; i++)
			s.insert(ds.find(i-A));
		cout << "Case #" << t+1 << ": " << s.size() << endl;
	}

	return 0;	
}
