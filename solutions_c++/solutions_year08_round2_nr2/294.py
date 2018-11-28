#include<iostream>
#include<vector>
#include<map>
#include<cmath>
using namespace std;
int L[1000005], vn;
map<long long, long long> M;
long long vA;
void initSets(long long A, long long B){
	M.clear();
	vA=A;
	vn=B-A+1;
	for(int i=0; i<vn; i++)
		L[i]=i;
}

int find(int v){
	if(v!=L[v])
		L[v]=find(L[v]);
	return L[v];
}

void unify(int u, int v){
	L[find(u)]=L[find(v)];
}

void putSet(long long N, long long Pr){
	if(M.find(Pr)!=M.end())
		unify(M[Pr]-vA, N-vA);
	M[Pr]=N;
}

int countSets(){
	for(int i=0; i<vn; i++)
		L[i]=find(L[i]);
	/*
	for(int i=0; i<vn; i++)
		cout<<i+vA<<' ';
	cout<<endl;
	for(int i=0; i<vn; i++)
		cout<<L[i]<<' ';
	cout<<endl;
	*/
	sort(L, L+vn);
	return unique(L,L+vn)-L;
}

bool checkPrim(int n){
	for(int i=2, en=(int)sqrt(n); i<=en; i++)
		if(n%i==0)
			return false;
	return true;
}

int main(){
	int N;cin>>N;
	for(int test=1; test<=N; test++){
		int A,B,P;
		cin>>A>>B>>P;
		vector<long long> Anl(B-A+1);
		initSets(A,B);
		for(int i=A; i<=B; i++)
			Anl[i-A]=i;
		for(int i=2; i<=min(B+10,1000005); i++)
			if(checkPrim(i)){
				int j=i*(int(A/i)-1);
				while(j<A)
					j+=i;
				while(j<=B){
					if(i>=P)
						putSet(j, i);
					while(Anl[j-A]%i==0)
						Anl[j-A]/=i;
					j+=i;
				}
			}
		for(int i=0; i<Anl.size(); i++)
			if(Anl[i]!=1 && Anl[i]>=P){
				putSet(A+i,Anl[i]);
			}
		cout<<"Case #"<<test<<": "<<countSets()<<endl;
	}

	return 0;
}
