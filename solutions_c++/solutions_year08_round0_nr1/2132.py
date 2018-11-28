#include <cstdio>
#include <set>
#include <string>
using namespace std;
set<string> s;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tt=1; tt<=t; tt++){
		int ans = 0;
		int ns,nq;
		scanf("%d\n",&ns);
		s.clear();
		for(int i=1; i<=ns; i++){
			char a[1000];
			scanf("%[^\n]\n",a);
		}
		scanf("%d\n",&nq);
		for(int i=1; i<=nq; i++){
			char a[1000];
			scanf("%[^\n]\n",a);
			string aa=  a;
			s.insert(aa);
			if(s.size()==ns){
				ans++;
				s.clear();
				s.insert(aa);
			}
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}