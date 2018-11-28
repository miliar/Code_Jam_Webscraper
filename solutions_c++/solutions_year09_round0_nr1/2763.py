#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

string known[6000];
char temp[1000], tmp[1000];
int L,D,N,n;

int rijesi(int a, int lok, string c, int od = -1){
	//printf("%d %d %s\n",a,lok,c.c_str());
	int sol = 0;
	if( lok == L ) return 1; 
	if( temp[a] == '(' ){
		int b = a;
		for(int x = a;x<n;++x) if( temp[x] == ')' ){ b = x; break; }
		for(int x = a + 1; x < b; ++x){
			if(od == -1){
			for(int y = 0;y<D;++y){
				if(c + temp[x] == known[y].substr(0, lok+1)){
					sol += 1 * rijesi(b+1, lok + 1, c + temp[x], y);
				}
			}
			}else{
				int y = od;
				if(c + temp[x] == known[y].substr(0, lok+1))
					sol += 1 * rijesi(b+1, lok + 1, c + temp[x], od);
				
			}
		}
	}else{
		if(od == -1){
		for(int y = 0;y<D;++y){
			if(c + temp[a] == known[y].substr(0,lok+1)){
				sol += 1 * rijesi(a+1, lok+1, c + temp[a], y);
			}
		}
		}else{
			int y = od;
			if(c + temp[a] == known[y].substr(0,lok+1)){
				sol += 1 * rijesi(a+1, lok+1, c + temp[a], od);
			}
		}
	}
	return sol;
}


int main(){
	scanf("%d %d %d",&L,&D,&N);
	for(int x = 0;x < D;++x){
		scanf("%s", tmp);
		known[x] = tmp;
	}
	for(int x = 0;x < N;++x){
		scanf("%s", temp);
		n = strlen(temp);
		printf("Case #%d: %d\n",x+1, rijesi(0,0, ""));
		
	}
	return 0;
}