#include <stdio.h>
#include <string>
#include <map>
#include <vector>
#include <string.h>

using namespace std;

int T,N,M;
char dic[10010][12];
int count[10010];
char seq[30];
int mark[300];
int bn,ba;
map< string,vector<int> > mapa;
map< string,int > tem;

string makeHash(int k){
	string a = string("");
	int len = strlen(dic[k]);
	for(int i=0; i<len; i++){
		if(mark[dic[k][i]] == 1){
			a += dic[k][i];
		}
		else{
			a += '_';
		}
	}
	return a;
}

int completa(int k){
	int len = strlen(dic[k]);
	for(int i=0; i<len; i++){
		if(mark[dic[k][i]] == 0) return 0;
	}
	return 1;
}

int checa(int k, char c){
	int len = strlen(dic[k]);
	for(int i=0; i<len; i++){
		if(dic[k][i] == c)return 1;
	}
	return 0;
}

int main(){
	scanf(" %d",&T);
	
	for(int t=0; t<T; t++){
		printf("Case #%d:",t+1);
		scanf(" %d %d", &N, &M);
		for(int i=0; i<N; i++){
			scanf(" %s",dic[i]);
		}
		for(int m=0; m<M; m++){
			scanf(" %s",seq);
			bn = 0;
			memset(mark,0,sizeof(mark));
			memset(count, 0, sizeof(count));
			for(int i=0; i<26; i++){
				
				mapa.clear();
				tem.clear();
				
				for(int j=0; j<N; j++){
					string r = makeHash(j);
					if(checa(j,seq[i])==1){
						tem[r] = 1;				
					}
					mapa[r].push_back(j);	
					//printf("push %d %d %d\n",i,j,mapa[r].size());
				}
				int cont = 0;
				for(int j=0; j<N; j++){
					string r = makeHash(j);
					//printf("i:%d j%d - %s\n",i,j,r.c_str());
					//if(tem.find(r) != tem.end()){
						//printf("tem i:%d j:%d \n",i,j);
					//}
					if(tem.find(r) != tem.end() && /*mapa[r].size() > 1 && */checa(j,seq[i])== 0 ){
						count[j]++;
					}
					/*if(mapa[r].size() > 1){
						cont = 1;
						if(count[j] > count[bn] || (count[j] == count[bn] && j<bn) ){
							bn = j;
						}
					}*/
				}
				mark[seq[i]] = 1;
			}
			bn = 0;
			for(int j=0; j<N; j++){
				if(count[j] > count[bn]){
					bn = j;
				}
			}
			printf(" %s",dic[bn]);
		}
		printf("\n");
	}
}
