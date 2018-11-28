#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;
char c[36][4],d[28][3],n[101];
int contain[256];
vector<char> ans;

void push(int tc){
	ans.push_back(tc);
	++contain[tc];
}
void pop(){
	int tc = ans[ans.size()-1];
	ans.pop_back();
	--contain[tc];
}
int main(){
	int t;
	cin>>t;
	for(int kk=1;kk<=t;++kk){
		int C,D,N;
		cin>>C;
		for(int i=0; i<C; ++i)
			cin>>c[i];
		cin>>D;
		for(int i=0; i<D; ++i)
			cin>>d[i];
		cin>>N>>n;

		ans.clear();
		memset(contain, 0, sizeof(contain));
		for(int i=0; i<N; ++i){
			push(n[i]);
			if(ans.size()==1)
				continue;
			char tc = n[i], tcp = ans[ans.size()-2];
			for(int j=0; j<C; ++j)
				if((tc==c[j][0] && tcp==c[j][1]) || (tc==c[j][1] && tcp==c[j][0])){
					pop();
					pop();
					push(c[j][2]);
					break;
				}
			for(int j=0; j<D; ++j)
				if(contain[(int)d[j][0]] && contain[(int)d[j][1]]){
					ans.clear();
					memset(contain, 0, sizeof(contain));
					break;
				}
		}
		printf("Case #%d: [",kk);
		if(!ans.empty()){
			printf("%c",ans[0]);
			for(size_t i=1; i<ans.size(); ++i)
				printf(", %c",ans[i]);
		}
		printf("]\n");
	}
	return 0;
}

