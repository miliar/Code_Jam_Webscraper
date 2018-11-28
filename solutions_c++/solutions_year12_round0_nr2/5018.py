

#include <iostream>
#include <vector>

using namespace std;


int dis(int a, int b)
{
    int d = a - b;
    d = d > 0 ? d : -d;
    return d;
}

int max(int a, int b, int c)
{
    int r = a > b ? a : b;
    r = r > c ? r : c;
    return r;
}

struct ScoreItem
{
    int  score1;
    int  score2;
    int  score3;
    int  score;
    int  sum;
    bool surprising;
};

vector<ScoreItem> g_ScoreSum[31];

int main(void)
{
    int i, j, k;
    for (i = 0; i <= 10; i++) {
        for (j = 0; j <= 10; j++) {
            for (k = 0; k <= 10; k++) {
                int dis1 = dis(i,j);
                int dis2 = dis(j,k);
                int dis3 = dis(k,i);

                if (dis1 <= 2 && dis2 <= 2 && dis3 <= 2) {

                    ScoreItem score;
                    score.score = max(i,j,k);
                    score.score1 = i;
                    score.score2 = j;
                    score.score3 = k;
                    score.sum = i + j + k;
                    if (dis1 == 2 || dis2 == 2 || dis3 == 2)
                        score.surprising = 1;
                    else
                        score.surprising = 0;

                    g_ScoreSum[score.sum].push_back(score);

                    //printf("%2d %2d %2d -> socre:%2d sum:%2d suprise:%d\n", i,j,k, max(i,j,k), (score.sum), score.surprising);
                }
            }
        }
    }

    int nTestCase;
    scanf("%d", &nTestCase);

    for (i = 0; i < nTestCase; i++) {
        int score_sum, nCount = 0;
        int nDancer, nSuprise, nLestScore;
        scanf("%d %d %d", &nDancer, &nSuprise, &nLestScore);

        for (j = 0; j < nDancer; j++) {
            scanf("%d", &score_sum);

            bool bCanSuprise = false;
            for (k = 0; k < g_ScoreSum[score_sum].size(); k++) {
                ScoreItem score = g_ScoreSum[score_sum][k];

                if (score.score >= nLestScore) {
                    if (score.surprising)
                        bCanSuprise = true;
                    else {
                        bCanSuprise = false;
                        nCount++;
                        break;
                    }
                }
            }
            if (bCanSuprise && nSuprise) {
                nSuprise--;
                nCount++;
            }
        }
        
        printf("Case #%d: %d\n", i+1, nCount);
    }
    return 0;
}