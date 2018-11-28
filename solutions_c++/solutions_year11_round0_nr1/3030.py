#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <cmath>
#include <map>

struct Button{
    int P;
    char R;
};

class Bot{

    public:

    int pos;
    char color;
    int lastButtonPushTime;

    Bot() {}
    Bot(char c) : pos(1), color(c), lastButtonPushTime(0) {}
    int moveTo(int newPos){ int sec = std::abs(pos-newPos); pos = newPos; return sec; }
    void pushButton(int time) { lastButtonPushTime = time; }
};

int main(){

    std::freopen("large.in", "r", stdin);
    std::freopen("large.out", "w", stdout);

    int T;
    std::scanf("%d", &T);

    for(int i = 0; i < T; i++){

        std::map<char,Bot> bots;
        Bot O ('O');
        Bot B ('B');
        bots['O'] = O;
        bots['B'] = B;

        int N;
        std::scanf("%d", &N);

        std::vector<Button> seq;

        for(int j = 0; j < N; j++){

            char Ri;
            int Pi;
            std::scanf(" %c %d", &Ri, &Pi);

            Button b;
            b.R = Ri;
            b.P = Pi;
            seq.push_back(b);

        }

        int count = 0;

        for(int j = 0; j < N; j++){

            int secs = 0;

            char R = seq[j].R;
            int P = seq[j].P;
            secs += bots[R].moveTo(P);
            int timeDiff = secs - (count - bots[R].lastButtonPushTime);
            if(timeDiff >= 0){
                count += timeDiff ;
            }
            count += 1;
            bots[R].pushButton(count);

        }

        printf("Case #%d: %d\n", i+1, count);

    }

    return 0;

}
