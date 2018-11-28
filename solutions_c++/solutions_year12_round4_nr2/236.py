#include <cstdio>
#include <queue>
#include <utility>
#include <algorithm>

using namespace std;

int length[1005];
int xpos[1005];
int ypos[1005];
int width;
int height;
bool flipped;
int cases;
int i,j,k;
int nump;
pair <int, int> rad[1005];
int numfree;
int bestx;
int besty;
int bestl;
int bestindex;
pair <int, int> rec[1005];
int map[1005];

int main(){
    scanf("%d", &cases);
    for (i = 1; i <= cases; i++){
        scanf("%d %d %d", &nump, &width, &height);
        for (j = 0; j < nump; j++){
            scanf("%d", &rad[j].first);
            rad[j].second = j;
        }
        if (height > width){
            height ^= width;
            width ^= height;
            height ^= width;
            flipped = true;
        } else {
            flipped = false;
        }
        sort (rad, rad+nump);
        reverse(rad, rad+nump);
        numfree = 0;
        length[numfree] = width;
        xpos[numfree] = 0;
        ypos[numfree] = 0;
        numfree++;
        for (j = 0; j < nump; j++){
            bestindex = -1;
            for (k = 0; k < numfree; k++){
                if (length[k] >= 2*rad[j].first && ypos[k] <= height && (bestindex == -1 || besty > ypos[k])){
                    // we have a better!
                    bestl = length[k];
                    bestx = xpos[k];
                    besty = ypos[k];
                    bestindex = k;
                }
            }
            if (besty == 0){
                besty -= rad[j].first;
            }
            if (!flipped){
                rec[j] = make_pair(bestx+rad[j].first, besty+rad[j].first);
            } else {
                rec[j] = make_pair(besty+rad[j].first, bestx+rad[j].first);
            }
            
            length[bestindex] -= 2*rad[j].first;
            xpos[bestindex] += rad[j].first*2;
            length[numfree] = 2*rad[j].first;
            xpos[numfree] = bestx;
            ypos[numfree] = besty + 2*rad[j].first;
            numfree++;
        }
        for (j = 0; j < nump; j++){
            map[rad[j].second] = j;
        }
        printf("Case #%d:", i);
        for (j = 0; j < nump; j++){
            printf(" %d %d", rec[map[j]].first, rec[map[j]].second);
        }
        printf("\n");
    }
}
