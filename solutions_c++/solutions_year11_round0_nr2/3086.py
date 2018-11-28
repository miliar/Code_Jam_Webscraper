#include <stdio.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int abs(int n){
	return n<0?-n:n;
}
int sgn(int n){
	return n<0?-1:(n>0?1:0);
}
int main(){
	int T;
	scanf("%d\n",&T);
	for(int Case=0;Case<T;Case++){
		vector<char>list;
		map<pair<char,char>,char>comb;
		map<char,set<char> >opp;
		
		int numcomb;
		scanf("%d ",&numcomb);
		for(int i=0;i<numcomb;i++){
			char a,b,c;
			scanf("%c%c%c ",&a,&b,&c);
			comb[pair<char,char>(a,b)]=c;
			comb[pair<char,char>(b,a)]=c;
		}
		
		int numopp;
		scanf("%d ",&numopp);
		for(int i=0;i<numopp;i++){
			char a,b;
			scanf("%c%c ",&a,&b);
			opp[a].insert(b);
			opp[b].insert(a);
		}
		
		int N;
		char ch;
		scanf("%d ",&N);
		for(int i=0;i<N;i++){
			ch=getchar();
			char last='\0';
			if(ch=='\n')break;
			if(!list.empty())last=*(list.end()-1);
			int insert=1;
			if(comb.find(pair<char,char>(ch,last))!=comb.end()){
				*(list.end()-1)=comb[pair<char,char>(ch,last)];
				insert=0;
			}
			else if(opp.find(ch)!=opp.end()){
				for(int j=0;j<list.size();j++)
					if(opp[ch].find(list[j])!=opp[ch].end()){
						list.clear();
						insert=0;
						break;
					}
			}
			if(insert){
				list.push_back(ch);
			}
		}
		while(Case<N-1&&ch!='\n')ch=getchar();
		
		printf("Case #%d: [",Case+1);
		for(int i=0;i<list.size();i++){
			if(i)printf(", ");
			printf("%c",list[i]);
		}
		printf("]\n");
	}
	return 0;
}