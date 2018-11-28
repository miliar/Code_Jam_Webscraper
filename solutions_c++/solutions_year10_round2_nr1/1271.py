#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<map>
#include<set>
using namespace std;

struct nodo{
	char *val;
	nodo(){}
	nodo(char *v){
		val=v;
	}
	vector<nodo *> sub;
};

int main(){
	freopen("A-large(2).in","r",stdin);
	freopen("out.txt","w",stdout);
	int r;
	cin>>r;	
	for(int t=1;t<=r;t++){
		int n,m;
		scanf("%d%d",&n,&m);
		getchar();
		int C=0;
		vector<nodo *> roots;
		for(int i=0;i<n;i++){
			char cad[104];
			gets(cad);
			char *ptr=strtok(cad+1,"/");
			int y;
			bool ok=false;
			for(y=0;y<roots.size();y++){
				if (!strcmp(roots[y]->val,ptr)){
					ok=true;
					break;
				}
			}
			nodo *recorrido;
			if(!ok){
				roots.push_back(new nodo(strdup(ptr)));
				recorrido=roots[roots.size()-1];
			}
			else recorrido=roots[y];
			int k=0;
			while(ptr!=NULL){
				ptr=strtok(NULL,"/");
				if(ptr==NULL) break;
				bool tok=false;
				int sz=recorrido->sub.size();
				for(y=0;y<sz;y++){
					if (!strcmp(recorrido->sub[y]->val,ptr)) {tok=true;break;}
				}
				if (!tok){
					recorrido->sub.push_back(new nodo(strdup(ptr)));
					recorrido=recorrido->sub[sz];
				}else
					recorrido=recorrido->sub[y];
			}
		}
		
		for(int i=0;i<m;i++){
			char cad[104];
			gets(cad);
			char *ptr=strtok(cad+1,"/");
			int y;
			bool ok=false;
			for(y=0;y<roots.size();y++){
				if (!strcmp(roots[y]->val,ptr)){
					ok=true;
					break;
				}
			}
			nodo *recorrido;
			if(!ok){
				roots.push_back(new nodo(strdup(ptr)));
				C++;
				recorrido=roots[roots.size()-1];
			}
			else recorrido=roots[y];
			int k=0;
			while(ptr!=NULL){
				ptr=strtok(NULL,"/");
				if(ptr==NULL) break;
				bool tok=false;
				int sz=recorrido->sub.size();
				for(y=0;y<sz;y++){
					if (!strcmp(recorrido->sub[y]->val,ptr)) {tok=true;break;}
				}
				if (!tok){
					recorrido->sub.push_back(new nodo(strdup(ptr)));
					C++;
					recorrido=recorrido->sub[sz];
				}else
					recorrido=recorrido->sub[y];
			}
		}	
		printf("Case #%d: %d\n",t,C);
	}
	
}			