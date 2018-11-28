#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <algorithm>

using namespace std;


typedef pair <int, int> WIRE;
typedef vector<WIRE>    WIRESEQ;

int intersection(WIRESEQ wires)
{
    int count = 0;
    sort(wires.begin(), wires.end());
    for (unsigned int i=0; i<wires.size(); i++) {
        for (unsigned int j=i+1; j<wires.size(); j++) {
            WIRE w1 = wires[i], w2 = wires[j];
            if (w1.first<w2.first && w1.second>w2.second) {
                count++;
            }
        }
    }
    return count;
}

int main(void)
{
    int T;
    scanf("%d\n", &T);
    for (int i=0; i<T; i++) {
        int N;
        scanf("%d\n", &N);

        WIRESEQ wires;
        for (int j=0; j<N; j++) {
            int a, b;
            scanf("%d %d\n", &a, &b);
            WIRE w = make_pair(a, b);
            wires.push_back(w);
        }

        printf("Case #%d: %d\n", i+1, intersection(wires));
    }
    return 0;
}
