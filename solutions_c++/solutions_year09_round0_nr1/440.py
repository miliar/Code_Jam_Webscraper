/* Google Code Jam 2009 Qualification
 * Problem A : Alien Language 
 * Coded by Lapro
 * Sep. 3, 2009
 */

#include <iostream>
#include <vector>
#include <string>
using namespace std;
int L, D, N;
struct dictreeNode{
    bool ended;
    int next[26];
    dictreeNode():ended(false){ 
        memset(next, -1, sizeof(next));
    }
};
vector<dictreeNode> dictree;

int calc(string& pattern, int tree_ptr, int cur){
    if (cur > pattern.size()) return 0;
    if (tree_ptr == -1) return 0;
    if (dictree[tree_ptr].ended) return 1;
    if (pattern[cur] == '('){
        int ret = 0;
        int next_cur = cur;
        while (pattern[next_cur] != ')') ++ next_cur;
        for(int i = cur + 1; i < next_cur; ++ i)
            ret += calc(pattern, dictree[tree_ptr].next[pattern[i] - 'a'], next_cur + 1);
        return ret;
    } else if (isalpha(pattern[cur])){
        return calc(pattern, dictree[tree_ptr].next[pattern[cur] - 'a'], cur + 1);
    } 
    return 0;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w+", stdout);
    cin >> L >> D >> N;
    dictree.push_back(dictreeNode());
    for(int i = 0; i < D; ++ i){
        string tmp;
        cin >> tmp;
        int tree_ptr = 0;
        for(int j = 0; j < tmp.size(); ++ j){
            if (dictree[tree_ptr].next[tmp[j] - 'a'] == -1){
                dictree[tree_ptr].next[tmp[j] - 'a'] = dictree.size();
                dictree.push_back(dictreeNode());
            }
            tree_ptr = dictree[tree_ptr].next[tmp[j] - 'a'];
        }
        dictree[tree_ptr].ended = true;
    }
    for(int i = 1; i <= N; ++ i){
        string pattern;
        cin >> pattern;
        printf("Case #%d: %d\n", i, calc(pattern, 0, 0));
    }
    return 0;
}
