#include <cstdio>
#include <vector>
#include <utility>
#include <set>
#include <map>

#define pb(x) push_back((x))

using namespace std;


int main(){
	int z;
	scanf("%d",&z);
	for(int y = 1; y <=z;y++){
		int C;
		scanf("%d",&C);
		map< pair<char,char> , char > combine;
		for(int i=0;i<C;i++){
			char str[5];
			scanf("%s",str);
			pair<char, char> p(str[0], str[1]);
			combine[p] = str[2];
			pair<char, char> q(str[1], str[0]);
			combine[q] = str[2];
		}
		set< pair<char, char> > opposed;
		int D;
		scanf("%d",&D);
		for(int i=0;i<D;i++){
			char str[3];
			scanf("%s",str);
			pair<char, char> p(str[0],str[1]);
			pair<char, char> q(str[1],str[0]);			
			opposed.insert(p);
			opposed.insert(q);
		}
		int N;
		scanf("%d",&N);
		char str[N+1];
		scanf("%s",str);
		int b[256];
		for(int i=0;i<256;i++) b[i] = 0;
		vector<char> stack;
		for(int i=0;i<N;i++){
			char c = str[i];
			stack.pb(c);
			b[c]++;
			bool f = true;
			while(f){
				f = false;
				if(stack.size() > 1){
					char d = stack.back(); stack.pop_back();
					c = stack.back(); stack.pop_back();
					pair<char, char> p(c,d);
					map< pair<char,char> , char >::iterator it = combine.find(p);
					if(it!=combine.end()){
						char e = combine[p];
						stack.pb(e);
						b[e]++;
						b[d]--;
						b[c]--;
						f = true;
						
					} else {
						stack.pb(c);
						stack.pb(d);
					}
				}
				if(!f){
					for(int j=65;j<91;j++){
						if(b[j] > 0){
							c = stack.back();
							set<pair<char,char> >::iterator it = opposed.find(pair<char,char>(c,j));
							if(it!=opposed.end()){
								stack.clear();
								for(int k=65;k<91;k++) b[k] = 0;
								f = false;
								break;
							}
						}
					}
				}
			}
		}
		printf("Case #%d: [", y);
		for(int i=0; i < int(stack.size())-1; i++){
			printf("%c, ", stack[i]);
		}
		if(stack.size() > 0){
			printf("%c", stack[stack.size()-1]);
		}
		printf("]\n");
	}
}












