#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<deque>
#include<vector>

using namespace std;

#define MAXN (1024*128)

set<string> paths;

int inseri(char *s){
	int resp = 0;
	
	if(paths.find(s) != paths.end()) return 0;	

	resp++;
	paths.insert(s);
	
	int tam = strlen(s);	
	int i = tam;
	
	while(1){
		i--;
		while(s[i] != '/') i--;
		if(i == 0) return resp;
		s[i] = '\0';
	
		if(paths.find(s) != paths.end()) return resp;
		resp++;
		paths.insert(s);		
	}
	
}

char buf[1024];

int main(){
	int nT,T;
	int resp,n,m,i;
	
	scanf("%d",&nT);
	for(T=1;T<=nT;T++){
		printf("Case #%d: ",T);
		scanf("%d %d",&n,&m);
		
		paths.clear();
		
		for(i=0;i<n;i++){
			scanf(" %s",buf);
			paths.insert(buf);
		}
		
		resp = 0;
		
		for(i=0;i<m;i++){
			scanf(" %s",buf);
			resp += inseri(buf);
		}
		
		printf("%d\n",resp);
		
	}
}
