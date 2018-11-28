#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;


vector<int> v;

int T;


int dec () {
    for (int i=0; i<v.size()-1; i++) {
        if (v[i] < v[i+1]) return 0;
    }
    return 1;
}

int solve () {
    v.clear();
    char str[100];
    gets(str);
    
    for (int i=0; i<strlen(str); i++) v.push_back(str[i]-'0');

    if (dec()) {
       sort(v.begin(),v.end());
       v.insert(v.begin(), 0);
       int w = 0;
       for (int i=0; i<v.size(); i++) {
           if (v[i] != 0) {
              w = i;
              break;
           }
       }
       int temp = v[0];
       v[0] = v[w];
       v[w] = temp;
    } else {
      next_permutation(v.begin(),v.end());
    }

    
}

int main () {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    scanf("%d\n",&T);

    for (int i=1; i<=T; i++) {
        solve();
        printf("Case #%d: ",i);
        for (int j=0; j<v.size(); j++) {
            printf("%d",v[j]);
        }
        printf("\n");
    }
    return 0;
}
