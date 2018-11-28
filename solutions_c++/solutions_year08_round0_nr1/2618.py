#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <map>
#define pb push_back

using namespace std;

vector<string> engine;
vector<string> palabraBuscar;

int f(){
	
	int cont=0,usados=0,t=engine.size();
	map<string,int> m;
	
	for(int n=0;n<t;n++) m.insert(make_pair(engine[n],0));
		
	for(int n=0;n<palabraBuscar.size();n++){	
		if(m.end()!=m.find(palabraBuscar[n])&&m[palabraBuscar[n]]==0){		
			m[palabraBuscar[n]]=m[palabraBuscar[n]]+1;
				usados++;
				if(usados==t){				
						cont++;					
						m.clear();
						for(int j=0;j<t;j++) m.insert(make_pair(engine[j],0));						
					
						m[palabraBuscar[n]]++;				
						usados=1;	
				}	
		}			
	}	
	return cont;
}

int main(){
		string fi="A-large.in";
		string fo="A-large.out";
		freopen(fi.c_str(),"r",stdin); 
		freopen(fo.c_str(),"w",stdout);
		int N;	
		scanf("%d",&N);	
	int S,Q;
		
		
		for(int i=0;i<N;i++){
			engine.clear();
			palabraBuscar.clear();			
			scanf("%d\n",&S);			
				for(int j=0;j<S;j++){
					string cad;					
					getline (cin,cad);				
					engine.pb(cad);			
					
				}		
		
			scanf("%d\n",&Q);
				for(int j=0;j<Q;j++){
					string cad;					
					getline(cin,cad);					
					if(palabraBuscar.size()>0){
						if(palabraBuscar[palabraBuscar.size()-1]!=cad)
							palabraBuscar.pb(cad);					
					}else
					palabraBuscar.pb(cad);
					
										
				}
				printf("Case #%d: %d\n",i+1,f());	

			}
	return 0;		
}
