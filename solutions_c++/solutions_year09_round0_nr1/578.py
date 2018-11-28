#include <cstdio>
#include <string>
#include <vector>
using namespace std;
vector<string> a;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int l,d,n;
	scanf("%d %d %d\n",&l,&d,&n);
	for(int i=0; i<d; i++){
		char s[111];
		scanf("%s\n",s);
		a.push_back(string(s));
	}
	for(int k=1; k<=n; k++){
		int ans = 0;
		char s[1111];
		scanf("%s\n",s);
		vector<char> b[1111];
		int what = 0;
		bool now = false;
		for(int i=0; i<strlen(s); i++){
			if(s[i]=='('){
				now=true;
			}
			else if(s[i]==')'){
				now=false;
				what++;
			}
			else{
				b[what].push_back(s[i]);
				if(!now)
					what++;
			}
		}
		for(int i=0; i<d; i++){
			int cnt = 0;
			for(int j=0; j<l; j++){
				bool ok = false;
				for(int k=0; k<(int)b[j].size(); k++){
					if(a[i][j]==b[j][k]){
						ok=true;
					}
				}
				if(ok)
					cnt++;
			}
			if(cnt==l)
				ans++;
		}
		printf("Case #%d: %d\n",k,ans);
	}
	return 0;
}
