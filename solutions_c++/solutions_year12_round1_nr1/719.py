#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int cases;
    int typed, total;
    double probs[100005];
    double prob;
    double keeptyping, backspaces[100005], enter;
    double best = 1000000000;
    scanf("%d", &cases);
    for (int i =0; i < cases; i++){
        scanf ("%d %d", &typed, &total);
        best = 1000000000;
        for (int j = 0; j < typed; j++){
            scanf("%lf", probs+j);
        }
        // keep typing
        prob = 1;
        for (int j = 0; j < typed; j++){
            prob *= probs[j];
        }
        keeptyping = (1+total-typed)*prob + (1+total-typed+total+1)*(1-prob);
        best = min(best, keeptyping);
        //printf ("keep %lf\n", keeptyping);
        // various backspaces
        prob = 1;
        for (int j = 0; j < typed; j++){
            backspaces[j] = prob*((typed-j) + (total-j) + 1) + 
                         (1-prob)*((typed-j) + (total-j) + 1 + total+1);
            best = min(best, backspaces[j]);
            prob *= probs[j];
          //  printf ("%d %lf\n", j, backspaces[j]);
        }


        // enter straight away
        enter = total+2;
        best = min(best, enter);
        //printf ("enter %lf\n", enter);
        printf ("Case #%d: %lf\n", i+1, best);
    }
}
