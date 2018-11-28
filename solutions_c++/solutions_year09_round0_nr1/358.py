#include<all>
using namespace std;
string s[10000];
int match(string a, string b){
	int k=0;
	for(int i=0; i<(int)a.size(); i++){
		if(b[k]!='('&&b[k]!=a[i])
			return false;
		if(b[k]==a[i]){
			k++;
			continue;
		}
		if(b[k]=='('){
			int mat=false;
			while(b[k]!=')'){
				k++;
				if(b[k]==a[i]){
					mat=true;
				}
			}
			if(!mat)
				return false;
			k++;
		}
	}
	return true;
}
int main(){
	int l,d,n;
	cin >> l >> d >> n;
	for(int i=0; i<d; i++){
		cin >> s[i];
	}
	for(int kase=1; kase<=n; kase++){
		cerr<<kase<<endl;
		string g;
		cin >> g;
		int left=false;
		int word=0;
		for(int i=0; i<(int)g.size(); i++){
			if(g[i]=='('){
				left=true;
				word++;
				continue;
			}
			if(g[i]==')'){
				left=false;
				continue;
			}
			if(left)
				continue;
			word++;
		}
		if(word!=l){
			printf("Case #%d: %d\n",kase,0);
			continue;
		}
		int ans=0;
		for(int i=0; i<d; i++){
			if(match(s[i], g)){
				ans++;
			}
		}
		printf("Case #%d: %d\n",kase,ans);
	}
}

