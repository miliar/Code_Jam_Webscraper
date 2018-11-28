#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int mapa[256];
char word[70];
int casos = 1;

int read(){
    scanf("%s", word);
    return 1;
}
void process(){
    int basis = 0;
    int count = 1;
    memset(mapa, -1, sizeof(mapa));
    unsigned long long answ = 0;
    int passou = 1;
    for(int i = 0; word[i]; i++){
        if(mapa[word[i]] == -1){
            if(count == 2 && passou){
                mapa[word[i]] = 0;
                passou = 0;
            }
            else mapa[word[i]] = count++;
            basis++;
        }
    }
    if(basis == 1)basis = 2;
    for(int i = 0; word[i]; i++){
        answ *= basis;
        answ += mapa[word[i]];
    }
    printf("Case #%d: %llu\n", casos++, answ);
}
int main(){
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int casos;
    scanf("%d", &casos);
    while(casos-- && read())process();
    return 0;
}
