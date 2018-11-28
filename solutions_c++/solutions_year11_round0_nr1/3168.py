#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int n, t;
int Case = 0;
int main() {
	scanf("%d", &n);
	while(n--) {
        ++Case;
		scanf("%d", &t);
        vector<pair<char, int> > V(t);
        char c[2];
        int k;
        for(int i = 0; i < t; ++i) {
            scanf("%s %d",  c, &k);
            V[i] = make_pair(c[0], k);
        }
        vector<bool> B(t);

        int T = 0, posO = 1, posB = 1, targetO = -1, targetB = -1;
        int lastO = -1, lastB = -1;        
        while(!B.back()) {
            ++T;

            bool Opressed = false;
            if(targetO == -1) {
                while(++lastO < t && V[lastO].first != 'O');
                targetO = lastO;
            }
            if(targetO < t) {
                if(posO < V[targetO].second) { ++posO; }
                else if(posO > V[targetO].second) { --posO; }
                else if(targetO == 0 || B[targetO - 1]) {
                    B[targetO] = true;
                    targetO = -1;
                    Opressed = true;
                }
            }
            if(targetB == -1) {
                while(++lastB < t && V[lastB].first != 'B');
                targetB = lastB;
            }
            if(targetB < t) {
                if(posB < V[targetB].second) { ++posB; }
                else if(posB > V[targetB].second) { --posB; }
                else if(targetB == 0 || (B[targetB - 1] && !Opressed)) {
                    B[targetB] = true;
                    targetB = -1;
                }
            } 
        }

        printf("Case #%d: %d\n", Case, T);

	}
	return 0;
}
