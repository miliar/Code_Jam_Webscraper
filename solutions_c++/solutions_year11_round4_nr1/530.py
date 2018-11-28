#include <stdio.h>

#include <algorithm>
#include <vector>
using namespace std;

struct Walks {
  public:
    int len;
    int walkSpeed;

    Walks(int start, int end, int walkSpeed) :
        len(end - start), walkSpeed(walkSpeed) {}

    struct comp {
        bool operator()(const Walks &a, const Walks &b) {
            return a.walkSpeed < b.walkSpeed;
        }
    };
};

vector<Walks> walks;

int main(void) {
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        int idist, iwalkS, irunS, irunT, wC;
        scanf("%d%d%d%d%d", &idist, &iwalkS, &irunS, &irunT, &wC);
        walks.clear();

        double dist = (double)idist;
        double walkS = (double)iwalkS;
        double runS = (double)irunS;
        double runT = irunT;

        int currPos = 0;
        for (int i = 0; i < wC; ++i) {
            int begin, end, speed;
            scanf("%d%d%d", &begin, &end, &speed);
            if (begin > currPos) {
                Walks walk(currPos, begin, iwalkS);
                walks.push_back(walk);
            }
            Walks walk(begin, end, speed + iwalkS);
            walks.push_back(walk);
            currPos = end;
        }
        if (currPos != idist) {
            Walks walk(currPos, idist, iwalkS);
            walks.push_back(walk);
        }

        sort(walks.begin(), walks.end(), Walks::comp());

        int runDiff = irunS - iwalkS;
        double totalT = 0.0;
        for (vector<Walks>::iterator it = walks.begin(); it != walks.end(); ++it) {
            double totalRunTime = (double)it->len / (double)(it->walkSpeed + runDiff);
            if (totalRunTime < runT) {
                totalT += totalRunTime;
                runT -= totalRunTime;
            } else {
                double walkDist = (double)it->len - runT * (double)(it->walkSpeed + runDiff);
                totalT += runT;
                runT = 0.0;
                totalT += walkDist / (double)it->walkSpeed;
            }
        }
        printf("Case #%d: %.10f\n", cC + 1, totalT);
    }
    return 0;
}
