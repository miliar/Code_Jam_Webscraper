#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
using namespace std;
#define SL size()
#define LE length()
#define PB push_back
#define MP make_pair
int A[1001];
int RES[2000001];
int posi;
int main(){
	int kases; cin>>kases;
	for (int kas = 1; kas<=kases; kas++) {
		int R,K,N; cin>>R>>K>>N;//runs-capacity-groups
		for (int n=0; n<N ; n++) {
			cin>>A[n];
		}
		int total=0,ac,pos1=0,pos2=0,mapi;
		posi =0;
		map<int,pair<int,int> > S;
		map<int,pair<int,int> >::iterator it;
		int init=0;
		while (true) {
			ac = 0; pos1 = pos2;
			while(ac+A[pos2]<=K){
				ac+=A[pos2];
				pos2++; 
				if(pos2 == N) pos2 = 0;
				if(pos2 == pos1) break;
			}
			mapi = (pos1<<12);
			mapi|= pos2;			
			it = S.find(mapi);
			if(it != S.end()){ init = it->second.first; break;}
			S[mapi] = MP(posi,ac);
			total+=ac;
			RES[posi++] = total;
	//		cout<<"MAPI: "<<mapi<<" P1: "<<pos1<<" P2: "<<pos2<<" AC: "<<ac<<" TOT: "<<total<<endl;
		}
	//	cout<<"INIT: "<<init<<endl;
		int offset=0; 
		for (it = S.begin(); R && it!=S.end(); it++) {
			if(it->second.first<init) {R--; offset+=it->second.second;}
		}
		int sol = offset; total-=offset;
		int loop = posi-init;
	//	cout<<"SOL: "<<sol<<" LOOP: "<<loop<<" R: "<<R<<" TOT: "<<total<<endl;
		if(R){
			//sol+=((R-1)/loop)*total;
			sol+= ( R/loop)*total; 
		//	cout<<"SOLR: "<<sol<<endl;
			R = R%loop;
			if(R){
				sol+=RES[R-1+init];
				if(init)sol-=RES[init-1];
			}
			//R = (R-1)%loop+init;
			//R = R%loop +init-1; 
			//if(R+1<posi){ sol+=RES[R];}
		}
		
		cout<<"Case #"<<kas<<": "<<sol<<endl;
	}
}