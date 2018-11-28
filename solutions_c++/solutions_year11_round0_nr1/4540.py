#include <stdio.h>
#include <algorithm>
using namespace std;

int b;
int bPos;
int r;
int rPos;

int main(){
    int casein;
    int butten;
    char bot;
    int newPos;

    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);

    scanf("%d", &casein);
    for(int i=1; i<=casein; i++){
        scanf("%d", &butten);
        b = r = 0;
        bPos = rPos = 1;
        while(butten>0){
            scanf(" %c %d", &bot, &newPos);
            if(bot == 'O'){
                r += abs(rPos-newPos)+1;
                if(r <= b){
                    r = b+1;
                }
                rPos = newPos;
            }
            else if(bot == 'B'){
                b += abs(bPos-newPos)+1;
                if(b <= r){
                    b = r+1;
                }
                bPos = newPos;
            }
            butten--;
        }
        printf("Case #%d: %d\n", i, max(b, r));
    }
    return 0;
}
