#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

#define INF 1023456789

main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int t=1;t<=datasuu;t++){
		printf("Case #%d: ",t);
		
		char comb[100][100];
		bool opp[100][100];
		for(char c='A';c<='Z';c++)for(char d='A';d<='Z';d++){
			comb[c][d]='\0';
			opp[c][d]=false;
		}
		int c,d,n;
		char buf[100];
		scanf("%d ",&c);
		for(int i=0;i<c;i++){
			scanf("%s",buf);
			comb[buf[0]][buf[1]]=comb[buf[1]][buf[0]]=buf[2];
		}
		scanf("%d ",&d);
		for(int i=0;i<d;i++){
			scanf("%s",buf);
			opp[buf[0]][buf[1]]=opp[buf[1]][buf[0]]=true;
		}
		scanf("%d ",&n);
		scanf("%s",buf);
		vector<char> hoge;
		for(int i=0;i<n;i++){
			char elem=buf[i];
			if(hoge.size()>0 && comb[elem][hoge.back()]!='\0'){
				char nelem=comb[elem][hoge.back()];
				hoge.pop_back();
				hoge.push_back(nelem);
			}else{
				bool vani=false;
				for(int i=0;i<hoge.size();i++){
					if(opp[elem][hoge[i]])vani=true;
				}
				if(vani)hoge.clear();
				else hoge.push_back(elem);
			}
		}
		printf("[");
		for(int i=0;i<hoge.size();i++){
			if(i!=0)printf(", ");
			printf("%c",hoge[i]);
		}
		printf("]\n");
	}
}