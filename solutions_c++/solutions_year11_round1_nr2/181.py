#include<cstdio>
#include<list>
#include<string>

using namespace std;

const int max_W = 10009;
const int max_S = 30;
char S[max_S];
string Dict[max_W];
int count[max_W];
int words;

int match(int num) {
    list<int> L;
    int in = 0;
    int size = Dict[num].size();
    for(int i=0; i<words; i++)
        if(Dict[i].size() == size) {
            in ++;
            L.push_back(i);
        }
    int letter = 0;
    int count = 0;
    while(in > 1) {
        bool point_lost = true;
        for(int j=0; j<size; j++)
            if(Dict[num][j] == S[letter])
                point_lost = false;
        bool letter_present = false;
        for(list<int>::iterator i = L.begin(); i!= L.end(); i++) {
            for(int j = 0; j<size; j++) {
                if( Dict[*i][j] == S[letter] )
                    letter_present = true;
                if( (Dict[num][j] == S[letter] && Dict[*i][j] != S[letter])||
                    (Dict[num][j] != S[letter] && Dict[*i][j] == S[letter])) {
                    
                    in --;
                    list<int>::iterator it = i;
                    i--;
                    L.erase(it);
                    break;
                }
            }
        }
        letter++;
        if(letter_present && point_lost)
            count++;
    }  
    return count;
}

void solve() {
    int idx=0, value=0, tmp;
    for(int i=0; i<words; i++) {
        tmp = match(i);
        if(tmp > value) {
            value = tmp;
            idx = i;
        }
    }
    printf(" %s", Dict[idx].c_str());
}

int main() {
    int tc;
    scanf("%d", &tc);
    for(int i=1; i<=tc; i++) {
        printf("Case #%d:", i);
        int lists;
        scanf("%d%d", &words, &lists);
        for(int i=0; i<words; i++) {
            scanf("%s", S);
            Dict[i] = S;
        }
        for(int i=0; i<lists; i++) {
            scanf("%s", S);
            solve();
        }
        printf("\n");
    }
    return 0;
}
