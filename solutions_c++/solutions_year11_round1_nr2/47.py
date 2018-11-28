#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

#define INF 1023456789

#define modp(x) (((x)%P+P)%P)

pair<string,int> tmp[10101];
bool contain[10101][128];

main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int casenum=1;casenum<=datasuu;casenum++){
		fprintf(stderr,"%d\n",casenum);
		printf("Case #%d: ",casenum);
		
		vector<string> w;
		vector<string> orig;
		vector<string> r;
		vector<string> ro;
		int n,m;
		scanf("%d%d ",&n,&m);
		w.resize(n);orig.resize(n);
		r.resize(n);ro.resize(n);
		for(int i=0;i<n;i++)for(char j=0;j<127;j++)contain[i][j]=false;
		//puts("Hello");return 0;
		for(int i=0;i<n;i++){
			char buf[100];
			gets(buf);
			w[i]=string(buf);
			orig[i]=w[i];
			int l=w[i].length();
			//for(int j=0;j<11-l;j++)w[i]+='*';
			for(int j=0;j<w[i].length();j++)contain[i][w[i][j]]=true;
			ro[i]=string("");
			for(int j=0;j<w[i].length();j++)ro[i]+='_';
		}
		/*
		for(int i=0;i<n;i++){
			for(int j=0;j<127;j++)if(contain[i][j])printf("%d:%c\n",i,j);
		}
		*/
		//puts("HellO!!!!!!!!!!!!!!");
		
		for(int t=0;t<m;t++){
			int cnt[10101]={};
			char l[100];
			gets(l);
			for(int i=0;i<n;i++){
				r[i]=ro[i];
			}
			for(int p=0;p<26;p++){
				for(int i=0;i<n;i++){
					tmp[i]=make_pair(r[i],i);
				}
				sort(tmp,tmp+n);
				//for(int i=0;i<n;i++)printf("%s %d\n",tmp[i].first.c_str(),tmp[i].second);
				for(int i=0;i<n;){
					int j;
					for(j=i;j<n&&tmp[i].first==tmp[j].first;j++);
					//printf("%d-%d\n",i,j);
					bool aru=false;
					for(int k=i;k<j;k++){
						if(contain[tmp[k].second][l[p]])aru=true;
					}
					if(aru){
						for(int k=i;k<j;k++){
							if(!contain[tmp[k].second][l[p]])cnt[tmp[k].second]++;
						}
					}
					i=j;
				}
				for(int i=0;i<n;i++){
					for(int k=0;k<w[i].length();k++)if(w[i][k]==l[p])r[i][k]=w[i][k];
				}
				//printf("%c: ",l[p]);for(int i=0;i<n;i++)printf("%d:%d ",i,cnt[i]);puts("");
			}
			//for(int i=0;i<n;i++)printf("%d:%d\n",i,cnt[i]);
			
			int ans=0;
			for(int i=1;i<n;i++){
				if(cnt[ans]<cnt[i])ans=i;
			}
			if(t>0)printf(" ");
			printf("%s",orig[ans].c_str());
		}
		puts("");
	}
}