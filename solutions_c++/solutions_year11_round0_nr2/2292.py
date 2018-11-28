#include <cstdio>
#include <map>
#include <vector>
#include <stack>
#include <utility>

using namespace std;

int main(){
	int w;
	scanf("%d",&w);
	for(int o = 0; o < w; o++){
		int d;
		scanf("%d",&d);
		char a,b,c;
		char stk[100];
		int index = 0;
		map<char,vector<pair<char,char> > > combine;  
		map<char,vector<char> > destroy;
		for(int i = 0; i < d; i++){
			scanf(" %c%c%c",&a,&b,&c);
			combine[a].push_back(make_pair(b,c));
			combine[b].push_back(make_pair(a,c));
		}
		scanf("%d",&d);
		for(int i = 0; i < d; i++){
			scanf(" %c%c",&a,&b);
			destroy[a].push_back(b);
			destroy[b].push_back(a);	
		}
		scanf("%d ",&d);
		for(int i = 0; i < d; i++){
			scanf("%c",&a);
			if(index == 0){
				stk[index] = a;
				index++;
			}else{
				bool ok = false;
				for(int j = 0; j < combine[a].size(); j++){
					if(stk[index-1] == combine[a][j].first){
						stk[index-1] = combine[a][j].second;
						ok = true;
						break;
					}
				}
				if(!ok){
					for(int j = 0; j < destroy[a].size(); j++){
						for(int k = 0; k < index; k++){
							if(stk[k] == destroy[a][j]){
							//printf("aqyu\n");
								index = 0;
								ok = true;
								break;
							}
						}
						if(ok) break;
					}
				}
				if(!ok){
					stk[index] = a;
					index++;
				}
			}
		}
		printf("Case #%d: [",o+1);
		for(int i = 0; i < index-1; i++){
			printf("%c, ",stk[i]);
		}
		if(index != 0){
			printf("%c",stk[index-1]);
		}
		printf("]\n");
	}
}
