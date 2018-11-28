#include <cstdio>
#include <map>
#include <vector>

using namespace std;
struct combination{
	combination(char other, char new_char):other_(other), new_char_(new_char){}
	char other_;
	char new_char_;
};

int main(){
	unsigned int t;
	scanf("%d", &t);
	unsigned int c, d, n;
	char c1, c2, c3;
	char last;
	bool clear = false;
	bool added = false;
	multimap<char, char> opposites;
	multimap<char, combination> combinations;
	vector<char> tokens;
	for(unsigned int i = 0; i < t; ++i){
		//printf("case %d\n", i);
		opposites.clear();
		combinations.clear();
		tokens.clear();
		scanf("%d", &c);
		for(unsigned int j = 0; j < c; ++j){
			scanf(" %c%c%c", &c1, &c2, &c3);
			//printf("combination: %c and %c form %c\n", c1, c2, c3);
			combinations.insert(pair<char, combination>(c1, combination(c2, c3)));
			if(c1 != c2)
				combinations.insert(pair<char, combination>(c2, combination(c1, c3)));
		}
		scanf("%d", &d);
		for(unsigned int j = 0; j < d; ++j){
			scanf(" %c%c", &c1, &c2);
			//printf("opposites: %c and %c\n", c1, c2);
			opposites.insert(pair<char, char>(c1, c2));
			opposites.insert(pair<char, char>(c2, c1));
		}
		scanf("%d", &n);
		scanf("%c", &c1);
		for(unsigned int j = 0; j < n; ++j){
			scanf("%c", &c1);
			//printf("token: %c\n", c1);
			if(tokens.size() > 0){
				added = false;
				last = tokens.back();
				for(multimap<char, combination>::iterator it = combinations.lower_bound(c1); it != combinations.upper_bound(c1); ++it){
					if(it->second.other_ == last){
						tokens.pop_back();
						tokens.push_back(it->second.new_char_);
						//printf("combined %c and %c to %c\n", c1, last, it->second.new_char_);
						added = true;
						break;
					}
				}
				if(added)
					continue;
				clear = false;
				for(vector<char>::iterator it = tokens.begin(); it != tokens.end(); ++it){
					//printf("check if %c is opposite with %c\n", c1, *it);
					for(multimap<char, char>::iterator it2 = opposites.lower_bound(c1); it2 != opposites.upper_bound(c1); ++it2){
						//printf("checking: %c\n", it2->second);
						if(it2->second == *it){
							//printf("clear!!\n");
							clear = true;
							break;
						}
					}
					if(clear){
						break;
					}
				}
				if(clear){
					tokens.clear();
					continue;
				}
				tokens.push_back(c1);
			}else{
				tokens.push_back(c1);
			}
		}
		printf("Case #%d: [", i+1);
		for(unsigned int j = 0; j < tokens.size(); ++j){
			printf("%c", tokens[j]);
			if(j < tokens.size() - 1){
				printf(", ");
			}
		}
		printf("]");
		if(i < t-1){
			printf("\n");
		}
	}
	return 0;
}
