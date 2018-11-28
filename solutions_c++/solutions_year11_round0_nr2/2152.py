#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
char C[250][250];
int D[250][250];
char s[101];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,ti;
	int n;
	scanf("%d",&T);
	for(ti=1;ti<=T;ti++){
		int c,d;
		memset(C,0,sizeof(C));
		memset(D,0,sizeof(D));
		scanf("%d",&c);
		for(int i=0;i<c;i++){
			scanf("%s",&s);
			C[s[0]][s[1]]=C[s[1]][s[0]]=s[2];
		}
		scanf("%d",&d);
		for(int i=0;i<d;i++){
			scanf("%s",&s);
			D[s[0]][s[1]]=D[s[1]][s[0]]=1;
		}
		scanf("%d",&n);
		scanf("%s",&s);
		vector<char> ans;
		for(int i=0;i<n;i++){
			if(ans.size()>0 && C[s[i]][ans[ans.size()-1]]){
				ans[ans.size()-1]=C[s[i]][s[i-1]];
			}else{
				int b=1;
				for(int j=0;j<ans.size();j++)
					if(D[ans[j]][s[i]]){
						ans.clear();
						b=0;
						break;
					}
				if(b)ans.push_back(s[i]);
			}
		}

		printf("Case #%d: [",ti);
		for(int i=0;i<ans.size();i++){
			printf("%c",ans[i]);
			if(i+1<ans.size())printf(", ");
		}
		printf("]\n");
	}
	return 0;
}
