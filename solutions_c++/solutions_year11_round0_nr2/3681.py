#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

char C[50][5], O[50][5], str[30];
vector<char> V;
bool flag;
int t, c, o, n, s;

int main(void){
	scanf("%d", &t);
	for(int k=0; k<t; k++){
		scanf("%d", &c);
		for(int i=0; i<c; i++) scanf("%s", C[i]);
		scanf("%d", &o);
		for(int i=0; i<o; i++) scanf("%s", O[i]);
		scanf("%d", &n);
		scanf("%s", str);

		V.clear();

		V.push_back(str[0]);
		for(int i=1; i<n; i++){
			V.push_back(str[i]);
			s = V.size();
			for(int j=0; j<c; j++){
				if(V[s-1]==C[j][0] && V[s-2]==C[j][1] || V[s-1]==C[j][1] && V[s-2]==C[j][0]){
					V.pop_back();
					V.pop_back();
					V.push_back(C[j][2]);
					break;
				}
			}
			s = V.size();
			flag = false;
			for(int j=0; j<o; j++){
				if(V[s-1]==O[j][0]){
					for(int p=0; p<s-1; p++){
						if(V[p]==O[j][1]){
							flag = true;
							break;
						}
					}
				}
				if(flag) break;

				if(V[s-1]==O[j][1]){
					for(int p=0; p<s-1; p++){
						if(V[p]==O[j][0]){
							flag = true;
							break;
						}
					}
				}
				if(flag) break;
			}
			if(flag){ V.clear(); }
		}

		printf("Case #%d: ", k+1);
		printf("[");
		for(int i=0; i<V.size(); i++){
			printf("%c%s", V[i], i==V.size()-1?"":", ");
		}
		printf("]\n");
	}
	return 0;
}
