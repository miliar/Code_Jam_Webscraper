#include <cstdio>
using namespace std;

int min(int a, int b) {
    if (a<b) {
        return a;
    }
    return b;
}

int main() {

    // scan in stuff
    // 3 1 5 15 13 11
    // 3 people
    // 1 surprising
    // >= 5
    //
    // calculate: 3n-2 without surprising
    // calculate: 3n-4 with surprising
    //
    // scan through data:
    // count number who are >= 3n-2
    // count number who are < 3n-2 and >= 3n-4
    //
    // answer is first number plus min (num surprising, num b)
    
    int numCases;
    scanf("%d", &numCases);
    for(int x=0; x<numCases; x++) {


        int numGooglers, numSurprising, numToBeat;
        scanf("%d %d %d", &numGooglers, &numSurprising, &numToBeat);
        int numGreater = 0;
        int numWithS = 0;
        int first = (3*numToBeat)-2;
        int second = (3*numToBeat)-4;
        if(second < 1) {
            second = 1;
        }
        for(int i=0; i<numGooglers; i++) {
            int score;
            scanf("%d", &score);
            if(score >= first) {
                numGreater++;
            }
            else if(score >= second) {
                numWithS++;
            }
        }
        int output = numGreater + min(numWithS, numSurprising);
        printf("Case #%d: %d\n", x+1, output);
    }

}
