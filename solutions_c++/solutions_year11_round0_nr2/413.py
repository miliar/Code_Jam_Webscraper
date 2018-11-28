#include<cstdio>
#include<set>
#include<vector>
using namespace std;
char com[40][4];
char opp[40][3];
char s[121];
int main(){
	int C, D, N;
	int T;
	scanf("%d", &T);
	for (int it=1; it<=T; it++){
		scanf("%d", &C);
		for (int i=0; i<C; i++)
			scanf("%s", com[i]);
		scanf("%d", &D);
		for (int i=0; i<D; i++)
			scanf("%s", opp[i]);
		scanf("%d", &N);
		scanf("%s", s);
		vector< char > V;
		for (int i=0; i<N; i++){
			V.push_back(s[i]);
			for (int j=0; j<C; j++){
				for (int k=V.size()-2; k>=0 &&  k<int(V.size())-1; k++)
					if ((V[k] == com[j][0] && V.back()==com[j][1])||
							(V[k] == com[j][1] && V.back()==com[j][0])){
						V.erase(V.begin()+k);
						V.pop_back();
						V.push_back(com[j][2]);
						break;
					}
			}
			for (int j=0; j<D; j++){
				for (int k=0; k<int(V.size())-1; k++){
					if ((V[k] == opp[j][0] && V.back()==opp[j][1])||
							(V[k] == opp[j][1] && V.back()==opp[j][0])){
						V.clear();
						break;
					}
				}
			}
		}
		printf("Case #%d: [", it);
		if (V.size()>0)
			printf("%c", V[0]);
		for (int i=1; i<V.size(); i++)
			printf(", %c", V[i]);
		printf("]\n");
	}
	return 0;
}
