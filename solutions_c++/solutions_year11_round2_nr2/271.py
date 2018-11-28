#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int C, D;
int P[200];
int V[200];

bool works(double dist) {
    int i, j;
    double prev = -dist + P[0];
    for (j = 1; j < V[0]; j++) {
        if(prev + D > P[0] + dist)
            return 0;
        prev = max(prev + D, P[0]-dist);
    }  
    for (i = 1; i < C; i++) {
        for (j = 0; j < V[i]; j++) {
            if(prev + D > P[i] + dist)
                return 0;
            prev = max(prev + D, P[i]-dist);
        }
    }  
    return 1;
}  

double binsearch(double start, double end) {
    if (end-start < 1e-3)
        return (end+start)/2;
    if (works((end+start)/2))
        return binsearch(start, (end+start)/2);
    return binsearch((end+start)/2, end);
} 

int main() {
    int t, T;
    scanf("%d", &T);
    for (t = 0; t < T; t++) {
        int i, j;
        scanf("%d %d", &C, &D);
        for (i = 0; i < C; i++)
            scanf("%d %d", &P[i], &V[i]);
        printf("Case #%d: %.2lf\n", t+1, binsearch(0.0, 1000000000000.0));  
    }
}
