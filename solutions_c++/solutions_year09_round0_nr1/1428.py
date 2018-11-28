
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

// O(N*D*L) works
// for each word in the dictionary, check if ok with pattern

int L, D, N;
vector <string> dict;
bool check[15][26];

int main() {
    FILE *fin = fopen("A-large.in", "r"), *fout = fopen("A-large.out", "w");
    fscanf(fin, "%d%d%d", &L, &D, &N);
    
    dict.clear();
    for(int i = 0; i < D; ++i) {
        char w[1000];
        fscanf(fin, "%s", w);
        dict.push_back(w);
    }
    
    for(int i = 0; i < N; ++i) {
        int ans = 0;
        char w[1000];
        fscanf(fin, "%s", w);
        
        int at = 0;
        for(int j = 0; j < L; ++j) {
            for(int k = 0; k < 26; ++k)
                check[j][k] = false;
            
            if(w[at] == '(') {
                ++at;
                while(w[at] != ')') {
                    check[j][w[at++]-'a'] = true;
                }
                ++at;
            }
            else {
                check[j][w[at++]-'a'] = true;
            }
        }
        
        for(int j = 0; j < D; ++j) {
            int k = 0;
            for(; k < L; ++k)
                if(!check[k][dict[j][k]-'a'])
                    break;
            if(k == L)
                ++ans;
        }
        
        fprintf(fout, "Case #%d: %d\n", i + 1, ans);    
    }
    
    return 0;
}
