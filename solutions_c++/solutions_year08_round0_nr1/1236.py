#include<stdio.h>
#include<set>
#include<string>
#include<assert.h>
#include<map>

using namespace std;

#define SIZE 1009

map< string, int > mm;
map< string, int >::iterator it;
int cnt[SIZE];

int main(){
	int n,x,i,j,s,q,ct,res,temp;
	string ss;
	char str[1000];
	
	freopen("alarge.in","r",stdin);
	freopen("alarge.out","w",stdout);
	scanf("%d",&n);
	for(x= 1; x<=n; ++x){
		scanf("%d",&s);
		gets(str);
		mm.clear();
		for(i=0; i<s; ++i){
			gets(str);
			ss = str;
			if(mm.find(ss) == mm.end()){
				mm.insert(make_pair(ss,i));
			}
			else assert(0);
		}
		scanf("%d",&q);
		gets(str);
		
		ct = 0;
		memset(cnt,0,sizeof(cnt));
		res = 0;
		for(i=0; i<q; ++i){
			gets(str);
			ss = str;
			
			it = mm.find(ss);
			if(it==mm.end()) assert(0);
			temp = it->second;
			if(cnt[temp] == 0){
				cnt[temp]++;
				ct++;
				if(ct==s){
					res++;
					memset(cnt,0,sizeof(cnt));
					cnt[temp]++;
					ct = 1;
				}
			}
		}
		
		printf("Case #%d: %d\n",x, res);
	}
	
	scanf(" ");
	return 0;
}
