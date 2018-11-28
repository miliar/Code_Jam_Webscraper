//I am sorry to say that I missubmitted the program in the Small dataset, this is the correct program.

#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int com[100][100];
int res[100][100];
char str[1000];

int main() {
    int t, n;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for (int cases = 1; cases <= t; ++cases) {
        int C, D, N;
        memset(res, 0, sizeof(res));
        memset(com, 0xff, sizeof(com));
        scanf("%d ",&C);
        //printf("C = %d\n",C);
        for (int i = 0; i < C; ++i) {
            scanf("%s",str);
            com[str[0] - 'A'][str[1] - 'A'] = str[2] - 'A';
            com[str[1] - 'A'][str[0] - 'A'] = str[2] - 'A';
        }
        scanf("%d ", &D);
        //printf("D = %d\n",D);
        for (int i = 0; i < D; ++i) {
            scanf("%s",str);
            res[str[0] - 'A'][str[1] - 'A'] = 1;
            res[str[1] - 'A'][str[0] - 'A'] = 1;
        }
        scanf("%d", &N);
        scanf("%s", str);
        //printf("N = %d str = %s\n",N, str);
        int len = strlen(str);
        vector<int> data;
        for (int i = 0; i < len; ++i) {
           if (data.size() == 0) {
              data.push_back(str[i] - 'A');
           } else {
              if (com[str[i] - 'A'][data[data.size() - 1]] > 0) {
                 int tmp = data[data.size() - 1];
                 data.pop_back();
                 data.push_back(com[str[i] - 'A'][tmp]);
              } else {
                 bool ff = false;
                 for (int j = 0; j < data.size(); ++j) {
                     if (res[str[i] - 'A'][data[j]] > 0) {
                        data.clear();
                        ff = true;
                        break;
                     }
                 }
                 if (!ff) {
                    data.push_back(str[i] - 'A');
                 }
              }
           }
        }
        printf("Case #%d: [",cases);
        for (int i = 0; i < data.size(); ++i) {
            if (i == 0) printf("%c", data[i] + 'A');
            else printf(", %c", data[i] + 'A');
        }
        printf("]\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
