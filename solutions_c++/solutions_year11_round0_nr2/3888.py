#include <stdio.h>
#include <map>
#include <vector>

int main(){
	int T,t,lp;
	char ct1,ct2,ct3;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		std::vector<std::pair<char,char> > oppose;
		std::vector<std::pair<std::pair<char,char>, char> > add;
		std::vector<char> list;
		scanf("%d",&t);
		while(t--){
			scanf(" %c%c%c",&ct1,&ct2,&ct3);
			add.push_back(std::pair<std::pair<char,char>,char>(std::pair<char,char>(ct1,ct2),ct3));
			#ifdef _DEBUG
			printf("--- Add to [addlist]: %c + %c -> %c\n",ct1,ct2,ct3);
			#endif
		}
		scanf("%d",&t);
		while(t--){
			scanf(" %c%c",&ct1,&ct2);
			oppose.push_back(std::pair<char,char>(ct1,ct2));
			#ifdef _DEBUG
			printf("--- Add to [opposelist]: %c - %c\n",ct1,ct2);
			#endif
		}
		scanf("%d ",&t);
		while(t--){
			scanf("%c",&ct1);
			list.push_back(ct1);
			#ifdef _DEBUG
			printf("--- Add %c\n",ct1);
			#endif
			if(list.size()<2) continue;
			
			//at least two elements
			for(std::vector<std::pair<std::pair<char,char>, char> >::iterator it = add.begin();it!=add.end();it++){
				if(((*it).first.first==list.at(list.size()-1)&&(*it).first.second==list.at(list.size()-2))||
					((*it).first.first==list.at(list.size()-2)&&(*it).first.second==list.at(list.size()-1))){
					#ifdef _DEBUG
					printf("--- Replace %c + %c -> %c\n",list.at(list.size()-1),list.at(list.size()-2),(*it).second);
					#endif
					list.pop_back();
					list.pop_back();
					list.push_back((*it).second);
				}
			}
			for(std::vector<std::pair<char,char> >::iterator it = oppose.begin();it!=oppose.end();it++){
				if((*it).first==list.at(list.size()-1)||(*it).second==list.at(list.size()-1))
					for(std::vector<char>::iterator it2 = list.begin();it2!=list.end();it2++){
						if(((*it).first==list.at(list.size()-1)&&(*it2)==(*it).second)||
						   ((*it).second==list.at(list.size()-1)&&(*it2)==(*it).first)){
							list.clear();
							#ifdef _DEBUG
							printf("--- Clear\n");
							#endif
							break;
						}
					}
			}
		}
		printf("Case #%d: [",i+1);
		for(std::vector<char>::iterator it = list.begin();it!=list.end();it++)
			printf("%c%s",(*it),(it+1==list.end() ? "" : ", "));
		printf("]\n");
	}
}
