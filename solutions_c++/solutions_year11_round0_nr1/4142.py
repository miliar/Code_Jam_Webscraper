#include <iostream>
#include <vector>
#include<cstdio>
#include<cstring>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

struct move {
    char robot;
    int dis;
};

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int i = 0; i < cas; i++) {
        int n;
        scanf("%d", &n);
        move box[120];
        vector<int> ora;
        vector<int> blue;
        for (int i = 0; i < n; i++) {
            scanf(" %c %d", &box[i].robot, &box[i].dis);
            if (box[i].robot == 'O') ora.push_back(box[i].dis);
            else blue.push_back(box[i].dis);
        }
        int disO = 1, disB = 1;
        int nowO = 0, nowB = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (box[i].robot == 'O') {
                int dis = abs(box[i].dis - disO) + 1;
                disO = box[i].dis;
                cnt += dis;
                nowO++;
                if (nowB < blue.size()) {
                    int d = abs(blue[nowB] - disB);
                    int p = min(d, dis);
                    if (blue[nowB] > disB) disB += p;
                    else disB -= p;
                }
            } else {
                int dis = abs(box[i].dis - disB) + 1;
                disB = box[i].dis;
                cnt += dis;
                nowB++;
                if (nowO < ora.size()) {
                    int d = abs(ora[nowO] - disO);
                    int p = min(d, dis);
                    if (ora[nowO] > disO) disO += p;
                    else disO -= p;
                }
            }
        }
        printf("Case #%d: %d\n", i + 1, cnt);
    }
    return 0;
}
