#include <cstdio>
#include <algorithm>
#include <utility>

using namespace std;

int cases;
pair <int, int> probs[1005];
int levels;
int dummy;

int main(){
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++){
        scanf("%d", &levels);
        for (int j = 0; j < levels; j++){
            scanf("%d", &dummy);
        }
        for (int j = 0; j < levels; j++){
            scanf("%d", &(probs[j].first));
            probs[j].first *= -1;
            probs[j].second = j;
        }
        sort(probs, probs+levels);
        printf ("Case #%d:", i);
        for (int j = 0; j < levels; j++){
            printf (" %d", probs[j].second);
        }
        printf ("\n");
    }
    return 0;
}
