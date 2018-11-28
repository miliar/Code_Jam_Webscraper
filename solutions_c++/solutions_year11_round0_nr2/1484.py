#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int C, D, N;
char s[105], cbn[40][5], ops[40][5];
vector<char> v;

void combine(){
	int n = v.size();
	char i = v[n-2], k = v[n-1];
	for(int j=0;j<C;j++){
		if(i==cbn[j][0] && k==cbn[j][1] || i==cbn[j][1] && k==cbn[j][0]){
			v.pop_back();
			v.pop_back();
			v.push_back(cbn[j][2]);
			combine();
			break;
		}
	}

}

void oppose(){
	char c = v.back();
	for(int i=0;i<v.size();i++){
		char k = v[i];
		for(int j=0;j<D;j++){
			if(c==ops[j][0] && k==ops[j][1] || c==ops[j][1] && k==ops[j][0]){
				v.clear();
				break;
			}
		}
	}
}

int main(){
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++){
		v.clear();
		scanf("%d",&C);
		for(int i=0;i<C;i++) scanf("%s",cbn[i]);
		scanf("%d",&D);
		for(int i=0;i<D;i++) scanf("%s",ops[i]);
		scanf("%d%s",&N,s);
		for(int i=0;i<N;i++){
			v.push_back(s[i]);
			combine();
			oppose();
		}
		printf("Case #%d: [",test);
		for(int i=0;i<v.size();i++){
			printf("%c", v[i]);
			if(i!=v.size()-1) printf(", ");
		}
		puts("]");
	}
}
