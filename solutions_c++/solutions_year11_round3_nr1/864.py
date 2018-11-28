#include <cstdio>
#include <vector>
using namespace std;

char gc(char &a){
	switch(a){
		case 'a':
		case 'd':
			return '/';
		case 'b':
		case 'c':
			return '\\';
		default:
			return '.';
	}
}

int main(){
	unsigned int t;
	scanf("%d",&t);
	unsigned int r, c;
	char ch;
	for(unsigned int i = 0; i < t; ++i){
		vector<vector<char> > tiles;
		bool good = true;
		scanf("%d%d", &r, &c);
		//printf("r en c: %d %d\n", r, c);
		for(unsigned int j = 0; j < r; ++j){
			scanf("%c", &ch);
			//printf("line:\n");
			tiles.push_back(vector<char>());
			for(unsigned int k = 0; k < c; ++k){
				scanf("%c", &ch);
				//printf("read char %c\n", ch);
				if(good){
					if(ch=='#'){
						if(j > 0){
							if(tiles[j-1][k]=='a'){
								ch = 'c';
							}else if(tiles[j-1][k]=='b'){
								ch = 'd';
							}else{
								if(k > 0){
									if(tiles[j][k-1] =='a'){
										ch = 'b';
									}else if(tiles[j][k-1]=='c'){
										ch = 'd';
									}else{
										ch = 'a';
									}
								}else{
									ch ='a';
								}
							}
						}else if(k > 0){
							if(tiles[j][k-1] =='a'){
								ch = 'b';
							}else if(tiles[j][k-1]=='c'){
								ch = 'd';
							}else{
								ch = 'a';
							}
						}else{
							ch = 'a';	
						}
					}else{
						if(j > 0){
							if(tiles[j-1][k] == 'a' || tiles[j-1][k] == 'b'){
								good =false;
							}
						}else if(k>0){
							if(tiles[j][k-1] == 'a' || tiles[j][k-1]=='c'){
								good = false;
							}
						}
					}
					if((ch == 'a' || ch == 'b') && (j == r-1)){
						good = false;
					}else if((ch == 'a' || ch == 'c') && (k == c-1)){
						good = false;
					}
					tiles[j].push_back(ch);
				}
			}
		}
		printf("Case #%d:\n",i+1);
		if(good){
			for(vector<vector<char> >::iterator it1 = tiles.begin(); it1 != tiles.end(); ++it1){
				for(vector<char>::iterator it2 = it1->begin(); it2 != it1->end(); ++it2){
					printf("%c", gc(*it2));
				}
				printf("\n");
			}
		}else{
			printf("Impossible\n");
		}
	}
	return 0;
}
