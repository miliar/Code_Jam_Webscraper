#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
pair<int,int> ba[1010],nba[1010];
int bwmn,bwmx,nbwmn,nbwmx;
int bhmn,bhmx,nbhmn,nbhmx;
int main(){
	int ca; scanf("%d",&ca);
	for (int tt=1; tt<=ca; tt++){
		printf("Case #%d:\n",tt);
		int n; scanf("%d",&n);
		int b,nb;
		b=nb=0;
		bwmn=bhmn=nbwmn=nbhmn=1<<29;
		bwmx=bhmx=nbwmx=nbhmx=0;
		for (int i=0; i<n; i++){
			int hh,ww; scanf("%d%d",&hh,&ww);
			char s[100]; gets(s);
			char ss[10]; sscanf(s,"%s",ss);
			if (ss[0]=='B'){
				ba[b++]=make_pair(hh,ww);
				if (ww<bwmn) bwmn=ww;
				if (ww>bwmx) bwmx=ww;
				if (hh<bhmn) bhmn=hh;
				if (hh>bhmx) bhmx=hh;
			}else{
				nba[nb++]=make_pair(hh,ww);
				if (ww<nbwmn) nbwmn=ww;
				if (ww>nbwmx) nbwmx=ww;
				if (hh<nbhmn) nbhmn=hh;
				if (hh>nbhmx) nbhmx=hh;
			}
		}
		int m; scanf("%d",&m);
		while (m--){
			int hh,ww; scanf("%d%d",&hh,&ww);
			int ans=-1;
			if ((bhmn<=hh && hh<=bhmx) && (bwmn<=ww && ww<=bwmx)){
				ans=1;
			}else{
				int tbhmn=bhmn;
				int tbhmx=bhmx;
				int tbwmn=bwmn;
				int tbwmx=bwmx;
				if (ww<tbwmn) tbwmn=ww;
				if (ww>tbwmx) tbwmx=ww;
				if (hh<tbhmn) tbhmn=hh;
				if (hh>tbhmx) tbhmx=hh;
				for (int i=0; i<nb; i++){
					int th=nba[i].first,tw=nba[i].second;
					if ((tbhmn<=th && th<=tbhmx) && (tbwmn<=tw && tw<=tbwmx)){
						ans=0;
					}
				}
			}
			if (ans==-1) printf("UNKNOWN\n");
			else if (ans==0) printf("NOT BIRD\n");
			else printf("BIRD\n");
		}
	}
	return 0;
}
