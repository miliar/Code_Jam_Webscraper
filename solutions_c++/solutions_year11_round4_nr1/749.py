#include<stdio.h>
#include<stdlib.h>

double w[2000];

int compare(const void *a, const void *b){
    int c = *(int*)a;
    int e = *(int*)b;

    double g = w[c];
    double h = w[e];

    if(g > h){
        return 1;
    }
    else if(g < h){
        return -1;
    }
    else{
        return 0;
    }
}

int main(){
    int test_case, ptr;
    int i, j, k;

    double b[2000];
    double e[2000];

    double d[2000];
    int index[2000];

    double only_walk;

    double answer;

    double x, s, r, t, n;

    freopen("ain.txt", "r", stdin);
    freopen("aout.txt", "w", stdout);

    scanf("%d", &test_case);



    for(i = 0; i < test_case; ++i){
        answer = 0;
        scanf("%lf %lf %lf %lf %lf", &x, &s, &r, &t, &n);

        only_walk = x;
        for(j = 0; j < n; ++j){
            scanf("%lf %lf %lf", &b[j], &e[j], &w[j]);
            index[j] = j;
            d[j] = (e[j] - b[j]);
            only_walk -= d[j];
        }

        if((r)*t > only_walk){
            answer += only_walk/(r);
            t -= (only_walk/(r));
        }
        else{
            only_walk -= (r)*t;
            answer += t;
            t = 0;
            answer += only_walk/(s);
        }

        qsort(index, n, sizeof(int), compare);

        for(j = 0; j < n; ++j){
            ptr = index[j];
            if(t <= 0){
                break;
            }
            if((w[ptr]+r)*t > d[ptr]){
                answer += d[ptr]/(r+w[ptr]);
                t -= (d[ptr]/(r+w[ptr]));
            }
            else{
                d[ptr] -= (r+w[ptr])*t;
                answer += t;
                t = 0;
                answer += d[ptr]/(s+w[ptr]);
            }
        }
        for(; j < n; ++j){
            ptr = index[j];
            answer += (d[ptr]/(s+w[ptr]));
        }

        printf("Case #%d: %f\n", i+1, answer);
    }

    return 0;
}
