#include<cstdio>
#include<vector>
#include<string>
#include<cstring>

using namespace std;

const int max_A = 30;
const int ZERO = 0;


vector<char> V;
class Combo{
    public:
    char from1, from2;
    char to;
    Combo() : from1(0), from2(0), to(0) {}
    Combo(char f1, char f2, char t) : from1(f1), from2(f2), to(t){}
    
    char check(char a, char b) {
        if(from1 == a && from2 == b)
            return to;
        if(from2 == a && from1 == b)
            return to;
        return ZERO;        
    }
};

vector<Combo> Combos;
vector<pair<int, int> > Opposites;

void clear() {
    V.clear();
}
void prepare() {
    clear();
    Combos.clear();
    Opposites.clear();
}
char find_combo(char a, char b) {
    int size = Combos.size();
    for(int i=0; i<size; i++) {
        char r = Combos[i].check(a, b);
        if(r != ZERO)
            return r;
    }
    return ZERO;
}
void check_opposites(char c) {
    int size = Opposites.size();
    for(int i=0; i<size; i++) {
        if(Opposites[i].first == c) {
            char other = Opposites[i].second;
            int s = V.size();
            for(int j=0; j<s; j++)
                if(V[j] == other) {
                    clear();
                    return;
                }
        }
    }
}
void insert(char c) {
    if(V.size()==0) {
        V.push_back(c);
        return;
    }
    char prev = V[V.size()-1];
    char combo = find_combo(c, prev);
    if(combo != ZERO) {
        V.pop_back();
        V.push_back(combo);
        return;
    }
    V.push_back(c);
    check_opposites(c);    
}
const int max_N = 109;
char buf[max_N];

int main() {
    int zw;
    scanf("%d", &zw);
    for(int tc=1; tc<=zw; tc++) {
        prepare();
        int comb;
        scanf("%d", &comb);
        for(int i=0; i<comb; i++) {
            scanf("%s", buf);
            Combos.push_back(Combo(buf[0], buf[1], buf[2]));
        }       
        int op;
        scanf("%d", &op);
        for(int i=0; i<op; i++) {
            scanf("%s", buf);
            Opposites.push_back(make_pair(buf[0], buf[1]));
            Opposites.push_back(make_pair(buf[1], buf[0]));            
        }
        int size;
        scanf("%d", &size);
        scanf("%s", buf);
        for(int i=0; i<size; i++)
            insert(buf[i]);
        printf("Case #%d: [", tc);
        for(int i=0; i<V.size(); i++) {
            if(i==0) 
                printf("%c", V[i]);
            else
                printf(", %c", V[i]);    
        }
        printf("]\n");
    }

    return 0;
}
