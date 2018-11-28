#include<stdio.h>
#include <string>
#include<set>
#include<vector>

using namespace std;

vector<string> v;

vector<char> ar[100];

int main () {
    freopen("aaa.in","r",stdin);
    freopen("a.out","w",stdout);


    int N,D,L;
    char str[10000];

    scanf("%d%d%d\n", &L,&D,&N);

    for (int i=0; i<D; i++) {
        scanf("%s\n", str);
        string s = str;
        v.push_back(s);
    }


    for (int i=1; i<=N; i++) {
        scanf("%s\n", str);
        for (int j=0; j<L; j++) ar[j].clear();
        
        int j = 0;
        int k = 0;
        int flag = 0;
        while (j < strlen(str)) {
              if (str[j] == '(') {
                 flag = 1;
              } else if (str[j] == ')') {
                 flag = 0;
                 k++;
              } else {
                 ar[k].push_back(str[j]);
                 if (flag == 0) k++;
              }
              j++;
        }

        for (int j=0; j<L; j++) sort(ar[j].begin(), ar[j].end());

        int ans = 0;
        for (int j=0; j<D; j++) {
            int flag = 1;
            for (int l=0; l<L; l++) {
                if (find(ar[l].begin(),ar[l].end(), v[j][l]) == ar[l].end()) {
                   flag = 0;
                   break;
                }
            }
            ans += flag;
        }
        printf("Case #%d: %d\n",i,ans);
    }

    

    return 0;
}
