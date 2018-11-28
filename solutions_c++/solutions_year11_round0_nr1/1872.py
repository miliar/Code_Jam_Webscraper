#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

struct node {
    char c;
    int  p;
} que[300];

queue<int> O, B, P, Time;
int N;
bool hash[102][102][102];
int mv[8][2] = {{1, 0}, {1, 1}, {1, -1}, 
                {0, 1}, {0, -1},
                {-1, 0}, {-1, 1}, {-1, -1} };
int push[3] = {1, -1, 0};

int solve() {
    while (!O.empty()) O.pop();
    while (!B.empty()) B.pop();
    while (!P.empty()) P.pop();
    while (!Time.empty()) Time.pop();
    O.push(1); B.push(1); P.push(1); Time.push(0);
    memset(hash, 0, sizeof hash);
    hash[1][1][1] = 0;
    while (!O.empty()) {
        int Orange = O.front(); O.pop();
        int Blue = B.front(); B.pop();
        int Position = P.front(); P.pop();
        int CostTime = Time.front(); Time.pop();
        
        int Next_Orange;
        int Next_Blue;
        int Next_Position;
        int Next_CostTime = CostTime + 1;
        
        //cout << Orange << ' ' << Blue << endl;
        if (que[Position].p == Orange && que[Position].c == 'O') {
            for (int i=0 ;i<3; i++) {
                Next_Position = Position + 1;
                Next_Orange = Orange;
                Next_Blue = Blue + push[i];
                if (Next_Orange <= 0 || Next_Blue <= 0 ||
                    Next_Orange > 100|| Next_Blue > 100)
                        continue;
                if (!hash[Next_Orange][Next_Blue][Next_Position]) {
                    hash[Next_Orange][Next_Blue][Next_Position] = 1;
                    O.push(Next_Orange);
                    B.push(Next_Blue);
                    P.push(Next_Position); 
                    Time.push(Next_CostTime);
                    if (Next_Position > N) return Next_CostTime;
                }
            }
        }
        if (que[Position].p == Blue && que[Position].c == 'B') {
            for (int i=0; i<3; i++) {
                Next_Position = Position + 1;
                Next_Orange = Orange + push[i];
                Next_Blue = Blue;
                if (Next_Orange <= 0 || Next_Blue <= 0 ||
                    Next_Orange > 100|| Next_Blue > 100)
                        continue;
                if (!hash[Next_Orange][Next_Blue][Next_Position]) {
                    hash[Next_Orange][Next_Blue][Next_Position] = 1;
                    O.push(Next_Orange);
                    B.push(Next_Blue);
                    P.push(Next_Position); 
                    Time.push(Next_CostTime);
                    if (Next_Position > N) return Next_CostTime;
                }
            }
        }
        for (int i=0; i<8; i++) {
            Next_Position = Position;
            Next_Orange = Orange + mv[i][0];
            Next_Blue = Blue + mv[i][1];
            if (Next_Orange <= 0 || Next_Blue <= 0 ||
                Next_Orange > 100|| Next_Blue > 100)
                    continue;
            if (!hash[Next_Orange][Next_Blue][Next_Position]) {
                hash[Next_Orange][Next_Blue][Next_Position] = 1;
                O.push(Next_Orange);
                B.push(Next_Blue);
                P.push(Next_Position); 
                Time.push(Next_CostTime);
                if (Next_Position > N) return Next_CostTime;
            }
        } 
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    int T = 1, cas;
    scanf("%d", &cas);
    while (cas --) {
        scanf("%d", &N);
        for (int i=1; i<=N; i++) {
            char s[2]; int d;
            scanf("%s %d", s, &d);
            que[i].c = s[0];
            que[i].p = d;
        }
        printf("Case #%d: %d\n", T ++, solve());
    }
    return 0;
}
