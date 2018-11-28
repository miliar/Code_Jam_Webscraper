#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>

#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sz size()
#define VER(x) cout << #x" = " << x << "\n"
#define MAXINT 2147483647
using namespace std;
string enteroaString(int n){stringstream ss;ss<<n;return ss.str(); }
int stringEntero(string s){int n;stringstream ss(s);ss>>n;return n; }
map<string,int> init_memobuscadores(vector<string> buscadores){
	map<string,int> d;
		for(int i=0;i<buscadores.sz;i++){
				d.insert(make_pair(buscadores[i],0));
			}
	return d;		
	}
int contarSw(vector<string> buscadores,vector<string> consultas){
	int contarswitch=0;
//	map<string,int> memo;
	map<string,int> memobuscadores;
	memobuscadores	 = init_memobuscadores(buscadores);
	
	int nroBuscadoresUsados=0;
	
	for(int i=0;i<consultas.sz;i++){
		//si la palabra es un buscador
		if(memobuscadores.end()!=memobuscadores.find(consultas[i])){
			int num = memobuscadores[consultas[i]];
			//cout<<"num : "<<num<<" consultas :"<<consultas[i]<<endl;
			if(num==0){//no se uso el buscador
			//VER(consultas[i]);
			memobuscadores[consultas[i]]=memobuscadores[consultas[i]]+1;
				nroBuscadoresUsados++;
				if(nroBuscadoresUsados==buscadores.sz){
					//aqui hay un switch
					//cout<<"i :"<<i<<" switch : "<<consultas[i]<<endl;
						contarswitch++;					
						memobuscadores	 = init_memobuscadores(buscadores);	
						memobuscadores[consultas[i]]=memobuscadores[consultas[i]]+1;				
						nroBuscadoresUsados=1;	
				}
					
			}
	
		}
			
	}
	
	return contarswitch;
	}

int main(){
		/*
		freopen("A-small.in","r",stdin); //A-small.in//A-large.in
		freopen("A-small.out","w",stdout);
		*/
		freopen("A-large.in","r",stdin); 
		freopen("A-large.out","w",stdout);
		
		int N;		
		cin>>N;
		
		vector<string> buscadores;
		vector<string> consultas;
		//map<string,int> search;
		
		for(int i=0;i<N;i++){
			buscadores.clear();
			consultas.clear();

			int S;
				cin>>S;
				scanf("\n");
				for(int j=0;j<S;j++){
					string cad;					
					getline (cin,cad);
					//VER(cad);
					buscadores.pb(cad);			
					
				}
			
			int Q;
				cin>>Q;
				scanf("\n");
				for(int j=0;j<Q;j++){
					string cad;					
					getline(cin,cad);					
					if(consultas.sz>0){
						if(consultas[consultas.sz-1]!=cad){
							consultas.pb(cad);
							
						}
					}else{
						consultas.pb(cad);
						//VER(consultas[j]);
					}					
				}
				
			//	for(int j=0;j<consultas.sz;j++)
//				VER(consultas[j]);
				
				int nrosw=contarSw(buscadores,consultas);
				
			cout<<"Case #"<<i+1<<": "<<nrosw<<endl;
			}
			
//system("pause");
}
