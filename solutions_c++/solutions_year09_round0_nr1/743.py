#include <iostream>
#include <cmath>
#include <string>
#include <vector>

#define TASK "file"
#define N 300000
#define M 20
using namespace std;

int l,d,n;

int next[N][27];
int size;
int stop[N];
string s;
vector<int> G[M];
int ans;
int k;

void fuck(int top,int cur){
	if (cur>=k){
		ans+=stop[top];
		//printf("stop - %i\n",stop[top]);
		return;
	}
	//printf("%i - %i\n",top,cur);
	for (int i=0;i<G[cur].size();i++){
		if (next[top][G[cur][i]]){
			fuck(next[top][G[cur][i]],cur+1);
		}
	}
}

int main(void){
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
	scanf("%i %i %i\n",&l,&d,&n);
	size=1;
	for (int i=0;i<d;i++){		
		getline(cin,s);
		int top=1;
		for (int j=0;j<l;j++){
			if (!next[top][s[j]-'a']){
				size++;
				next[top][s[j]-'a']=size;
			}
			top=next[top][s[j]-'a'];
		}
		stop[top]++;
	}
	for (int i=0;i<n;i++){
		for (int j=0;j<20;j++) G[j].clear();
		getline(cin,s);
		k=0;
		int flag=0;
		for (int j=0;j<s.size();j++){
			if (s[j]=='('){
				flag=1;
				continue;
			}
			if (s[j]==')'){
				flag=0;
				k++;
				continue;
			}
			G[k].push_back(s[j]-'a');
			if (!flag){
				k++;
			}
		}		
		ans=0;
		fuck(1,0);
		printf("Case #%i: %i\n",i+1,ans);
	}

	
	return 0;
}