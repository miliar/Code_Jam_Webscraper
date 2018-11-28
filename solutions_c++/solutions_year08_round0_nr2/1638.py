#include <cstdio>
#include <algorithm>

using namespace std;

pair<int,int> qa[200],qb[200];
int sa[1600],sb[1600];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int N,k,t,na,nb,i,j,ansa,ansb,h1,m1,h2,m2,ca,cb;
	scanf("%d",&N);
	char st[15];
	for(k=1;k<=N;k++){
		ansa=ansb=0;
		for(i=0;i<1600;i++)sa[i]=sb[i]=0;
		scanf("%d%d%d",&t,&na,&nb);
		gets(st);
		for(i=0;i<na;i++){
			gets(st);
			st[2]=st[8]=' ';
			sscanf(st,"%d%d%d%d",&h1,&m1,&h2,&m2);
			qa[i]=make_pair(h1*60+m1,h2*60+m2);
		}
		for(i=0;i<nb;i++){
			gets(st);
			st[2]=st[8]=' ';
			sscanf(st,"%d%d%d%d",&h1,&m1,&h2,&m2);
			qb[i]=make_pair(h1*60+m1,h2*60+m2);
		}
		sort(qa,qa+na);
		sort(qb,qb+nb);
		ca=cb=0;
		while(ca<na || cb<nb){
			if(ca<na && cb<nb){
				if(qa[ca].first<qb[cb].first){
					sb[qa[ca].second+t]++;
					for(i=qa[ca].first;i>=0;i--)
						if(sa[i]){
							sa[i]--;
							ansa--;
							break;
						}
					ansa++;
					ca++;
				}else{
					sa[qb[cb].second+t]++;
					for(i=qb[cb].first;i>=0;i--)
						if(sb[i]){
							sb[i]--;
							ansb--;
							break;
						}
					ansb++;
					cb++;
				}
			}else
				if(ca<na){
					sb[qa[ca].second+t]++;
					for(i=qa[ca].first;i>=0;i--)
						if(sa[i]){
							sa[i]--;
							ansa--;
							break;
						}
					ansa++;
					ca++;
				}else{
					sa[qb[cb].second+t]++;
					for(i=qb[cb].first;i>=0;i--)
						if(sb[i]){
							sb[i]--;
							ansb--;
							break;
						}
					ansb++;
					cb++;
				}
		}
		printf("Case #%d: %d %d\n",k,ansa,ansb);
	}

	return 0;
}