#include <cstdio>
#include <vector>
#include <string>
using namespace std;

char table[0x100][0x100];
bool oppos[0x100][0x100];

int main(){
	int T;
	scanf("%d",&T);
	for(int c=1; c<=T; c++){

		//clear tables
		for(int i='A'; i<='Z'; i++)for(int j='A'; j<='Z'; j++) table[i][j] = '*';
		for(int i='A'; i<='Z'; i++)for(int j='A'; j<='Z'; j++) oppos[i][j] = false;

		//read input
		int C, D, N;
		char buf[257];
		scanf("%d ",&C);
		for(int i=0; i<C; i++){
			scanf("%s ",buf);
			char s1 = buf[0], s2 = buf[1], t = buf[2];
			table[s1][s2] = table[s2][s1] = t;
		}
		scanf("%d ",&D);
		for(int i=0; i<D; i++){
			scanf("%s ",buf);
			oppos[buf[0]][buf[1]] = oppos[buf[1]][buf[0]] = true;
		}
		scanf("%d %s ",&N, buf);

		//simulation
		vector<char> st;
		for(int i=0; i<N; i++){
			st.push_back(buf[i]);
			while((int)st.size() >= 2){
				char c1 = st[st.size()-1], c2 = st[st.size()-2];
				if(table[c1][c2] != '*'){
					char ch = table[c1][c2];
					st.pop_back(); st.pop_back();
					st.push_back(ch);
				}
				else{
					break;
				}
			}
			for(int j=0; j<(int)st.size(); j++)for(int k=j+1; k<(int)st.size(); k++){
				if(oppos[st[j]][st[k]]){
					st.clear();
					goto end;
				}
			}
			end:;
		}

		//output
		printf("Case #%d: [",c);
		string ans = "";
		for(int i=0; i<(int)st.size(); i++){
			ans += st[i];
			ans += ", ";
		}
		if(!ans.empty()){
			ans = ans.substr(0,(int)ans.length()-2) + "]";
		}
		else{
			ans = "]";
		}
		puts(ans.c_str());
	}
	return 0;
}
