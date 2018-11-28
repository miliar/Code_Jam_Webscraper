#include <stdio.h>
#include <string>
using namespace std;

int L, D, N;

string word[5001];
string pattern[501];

char tmp[5001];
void init() {
    int i;
    scanf("%d%d%d", &L, &D, &N);
    for (i=0; i<D; ++i) {
        scanf("%s", tmp);
        word[i] = tmp;
    }    
    for (i=0; i<N; ++i) {
        scanf("%s", tmp);
        pattern[i] = tmp;
    }    
}    

bool isMatch(const string &p, const string &w) {
    const char * pt = p.c_str();
    const char * pw = w.c_str();
    while (*pw && *pt) {
        if (*pt!='(') {
            if (*pt != *pw) return false;
            else pt++;
        } else {
            pt++;
            while (*pt != *pw && *pt && *pt!=')') pt++;
            // find one
            if (*pt == *pw) {
                while (*pt && *pt!=')') pt++;
                if (*pt) pt ++;
            } // not find
            else {
                return false;
            }    
        }        
        
        pw++;
    }    
    return true;
}    

int matches(const string &p) {
    int cnt = 0;
    int i;
    for (i=0; i<D; ++i)
        if (isMatch(p, word[i]))
           cnt++;
    return cnt;
}   


 
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    init();    
    for (int i=0; i<N; ++i) {
        int ans = matches(pattern[i]);
        printf("Case #%d: %d\n", i+1, ans);
    }    
   // while (1);
    return 0;
}    
/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
*/
