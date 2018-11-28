#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <string>
#include <math.h>
#include <algorithm>
#include <queue>
#include <vector>
using namespace	std;
const int max_size = 30;

vector <char> answ;

int main(){
#ifdef	xDx
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	int T,C,D,N;
	char combine[max_size][max_size];
	bool opposed[max_size][max_size];
	scanf("%d",&T);
	for(int i=0; i<T; i++){
		memset(combine,-1,sizeof(combine));
		memset(opposed,0,sizeof(opposed));
		answ.clear();
		scanf("%d",&C);
		for(int j=0; j<C;j++){
			char tmp_s[5];
			scanf("%s",tmp_s);
			combine[tmp_s[0]-'A'][tmp_s[1] - 'A'] = tmp_s[2];
			combine[tmp_s[1]-'A'][tmp_s[0] - 'A'] = tmp_s[2];
		}
		scanf("%d",&D);
		for(int j=0; j<D;j++){
			char tmp_s[5];
			scanf("%s",tmp_s);
			opposed[tmp_s[0]-'A'][tmp_s[1] - 'A'] = true;
			opposed[tmp_s[1]-'A'][tmp_s[0] - 'A'] = true;
		}
		scanf("%d",&N);
		char posled[105];
		scanf("%s",posled);
		for(int j=0; j<N; j++){
			answ.push_back(posled[j]);
			if((int)answ.size() > 1){
				int end = (int)answ.size()-1;
				if(combine[answ[end]-'A'][answ[end-1]-'A']!=-1){
					char new_el = combine[answ[end]-'A'][answ[end-1]-'A'];
					answ.pop_back();
					answ.pop_back();
					answ.push_back(new_el);
				}
			}
			bool p=true;
			
			for(int k=0;p && k<(int)answ.size()-1; k++){
				if(opposed[answ[(int)answ.size()-1]-'A'][answ[k] - 'A']){
					p = false;
					answ.clear();
				}
			}
		}
		printf("Case #%d: [",i+1);
		for(int k=0; k<(int)answ.size(); k++){
			printf("%c",answ[k]);
			if(k!=(int)answ.size()-1)
				printf(", ");			
		}
		printf("]\n");
	}

	return 0;
}