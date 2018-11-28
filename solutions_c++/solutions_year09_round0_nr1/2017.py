#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int procces(string& str, vector<vector<bool> >& matrix) {
    int idx = 0;
    bool inside = false;
    for(int i=0; i<str.size(); ++i) {
        if(str[i] == '(') {
            inside = true;
            continue;
        } else if(str[i] == ')'){
            inside = false;
            idx++;
            continue;
        } else if(str[i] != '(' && str[i] != ')') {
             if(inside)
                matrix[str[i]-'a'][idx] = true;
            else
                matrix[str[i]-'a'][idx++] = true;
        }
    }
}

int answer(string& str, vector<string>& dict) {
    vector<vector<bool> > matrix(26, vector<bool>(dict[0].size(), false));
    procces(str, matrix);
    int count = 0;
    for(int i=0; i<dict.size(); ++i) {
        bool flag = true;
        for(int j=0; j<dict[i].size() && flag; ++j) {
            if(!matrix[dict[i][j]-'a'][j])
                flag = false;
        }
        if(flag) ++count;
    }
    return count;
}

int main() {
    
    #ifndef ONLINE_JUDGE
        freopen("A-large.in", "r", stdin);
        freopen("A-lage.out", "w", stdout);
    #endif
    
    int L, D, N;
    scanf("%d %d %d", &L, &D, &N);
    vector<string> dict(D);
    for(int i=0; i<D; ++i) {
        char buff[20]; scanf("%s", buff);
        dict[i] = buff;
    }
    for(int i=0; i<N; ++i) {
        char buff[1024]; scanf("%s", buff);
        string str = buff;
        printf("Case #%d: %d\n", i+1, answer(str, dict));
    }
    return 0;
}
