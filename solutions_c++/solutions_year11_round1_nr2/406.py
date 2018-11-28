#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
using namespace std;
#define ll long long
#define ull unsigned long long
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X))
#define klr(X) memset(X,-1,sizeof(X))
#define pii pair<int,int>

int main(){
	int casos;
	scanf("%d",&casos);
	for(int caso=1;caso<=casos;caso++){
		int n,m;
		scanf("%d %d",&n,&m);
		set<string> D;
		map<string,int> idx;
		for(int i=0;i<n;i++){
			char buff[20];
			scanf("%s",buff);
			D.insert(buff);
			idx[buff]=i;
		}
		printf("Case #%d: ",caso);
		while(m--){
			char seq[30];
			int ja[30];
		
			scanf("%s",seq);
			int mm=-1;
			set<string> :: iterator ff=D.begin();
			
			for(set<string> :: iterator f = D.begin();f!=D.end();f++){
				clr(ja);
				set<string> G = D;
				vector<string> v;
				string rr =*f;
				//	printf("vou fazer com %s\n",rr.c_str());
				for(set<string>:: iterator it = G.begin();it!=G.end();it++){
					string ss = *it;
					if(sz(ss) != sz(rr))
						v.pb(*it);
				}
				for(int i=0;i<sz(v);i++){
				//	printf("  tirando rm cima %s\n",v[i].c_str());
					G.erase(v[i]);
				}
				int q=0;
				for(int i=0;sz(G)>1;i++){
					int tem=0;
					for(set<string>:: iterator it = G.begin();it!=G.end();it++){
						int j;
						string ss = *it;
						for(j=0;j<sz(ss);j++)
							if( (ss)[j] == seq[i])break;
						if(j<sz(ss)){tem=1;break;}
					}
					ja[seq[i]-'a']=1;
					if(!tem){/*printf("  passei %c\n",seq[i]);*/continue;}
					//printf("   joguei %c\n",seq[i]);
					int k;
					for(k=0;k<sz(rr);k++)
						if(rr[k]==seq[i])break;
					if(k==sz(rr))
						q++;
					v.clear();
					for(set<string>:: iterator it = G.begin();it!=G.end();it++){
						string ss = *it;
						int j;
						for(j=0;j<sz(ss);j++)
							if(ss[j]!=rr[j] && ( ja[rr[j]-'a']||ja[ss[j]-'a'] )){
							//	printf("   deu aqui ss[j]:%c rr[j]:%c ja[rr[j]-'a']=%d ja[ss[j]-'a']=%d\n",
							//			ss[j],rr[j],ja[rr[j]-'a'],ja[ss[j]-'a']);
								v.pb(ss);
								break;
							}
					}
					for(int i=0;i<sz(v);i++){
					//	printf("  tirando %s\n",v[i].c_str());
						G.erase(v[i]);
					}
				}
			//	printf("deu %d\n",q);
				
				if(q>mm) {
					mm=q;
					ff=f;
				}
				else if(q==mm){
					string tt1 = *f, tt2=*ff; 
					if(idx[tt1]<idx[tt2]){
						mm=q;
					ff=f;
					}
				}
			}
			if(m>0)printf("%s ",(*ff).c_str());
			else printf("%s\n",(*ff).c_str());
		}
	}	
	return 0;
}

