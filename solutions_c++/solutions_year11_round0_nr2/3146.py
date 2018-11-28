#include <stdio.h>
#include <vector>
#include <map>
#include <string>
#include <list>

using namespace std;

int main(){
	FILE *fp= fopen("c:\\drugi.out", "w+");
	int t;
	char s[100];
	map<pair<char,char>, char> mapa;
	map<pair<char,char>, char> opposed;
	
	map<char, int> brojac_slova;
	vector<char> niz;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		int c;
		scanf("%d",&c);
		for(int j=0;j<c;j++){
			scanf("%s",s);
			brojac_slova[s[0]]=0;
			brojac_slova[s[1]]=0;
			brojac_slova[s[2]]=0;
			mapa[make_pair(s[0],s[1])]=s[2];
			mapa[make_pair(s[1],s[0])]=s[2];
			}
		int d;
		scanf("%d",&d);
		
		for(int j=0;j<d;j++){
			scanf("%s",s);
			brojac_slova[s[0]]=0;
			brojac_slova[s[1]]=0;
			opposed[make_pair(s[0],s[1])]=1;
			opposed[make_pair(s[1],s[0])]=1;
		}
		int n;
		string niz_naredbi;
		scanf("%d",&n);
		scanf("%s",s);
		//printf("%c, od r ",opposed['R']);
		for(int j=0;j<n;j++){
			int pom=0;		
			if(niz.size()>0){
				if(mapa.count(make_pair(s[j],niz.back()))!=0){
					printf("mc: %d\n", mapa.count(make_pair(s[j],niz.back())));
					char temp = niz.back();
					niz.pop_back();
					brojac_slova[temp]--;
					printf("%c i %c u %c \n", s[j],temp, mapa[make_pair(s[j],temp)]);
					char pom1 = mapa[make_pair(s[j],temp)];
					niz.push_back(pom1);
					if(brojac_slova.count(pom1)>0){
						brojac_slova[pom1]=brojac_slova[pom1]+1;
					}else{
						brojac_slova[pom1]=1;
					}
					continue;
				}
			}
			
			if(niz.size()>0)
			for(int k=0;k<niz.size();k++)
			if(opposed[make_pair(s[j],niz[k])]==1){
				printf("%c, %c brisi sve\n",s[j], niz.back());
				niz.clear();
				brojac_slova.clear();
				pom=1;
				continue;
			}
			if(pom)
				continue;
			niz.push_back(s[j]);
		}
		
		fprintf(fp, "Case #%d: [",(i+1));
		printf("Case %d: [",(i+1));
		for(int j=0;j<niz.size();j++){
			printf("%c",niz[j]);
			fprintf(fp,"%c",niz[j]);
			if(j!=niz.size()-1){
				fprintf(fp,", ");
				printf(", ");
			}
		}
		printf("]\n");
		fprintf(fp,"]\n");
		niz.clear();
		brojac_slova.clear();
		mapa.clear();
		opposed.clear();
	}
	
	
}