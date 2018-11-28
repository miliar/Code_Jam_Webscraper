#include <iostream>
using namespace std;

int moveAndPush(int& start1, int end1, int& start2, int end2);
int moveEitherDirection(int start, int end);

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        int P[100];
        char R[100];

        cin >> N;
        for (int j = 0; j < N; j++) {
            cin >> R[j] >> P[j];
        }

        int orangePosition = 1, bluePosition = 1, orangeDestination = 0, blueDestination = 0, time = 0;

        for (int j = 0; j < N; j++) {
            if (R[j] == 'O') {
                for (int k = j; k < N; k++) {
                    if (R[k] == 'B') {
                        blueDestination = P[k];
                        break;
                    }
                }
                time += moveAndPush(orangePosition, P[j], bluePosition, blueDestination);
            } else {
                for (int k = j; k < N; k++) {
                    if (R[k] == 'O') {
                        orangeDestination = P[k];
                        break;
                    }
                }
                time += moveAndPush(bluePosition, P[j], orangePosition, orangeDestination);
            }
        }

        cout << "Case #" << i + 1 << ": " << time << endl;
    }
}

int moveAndPush(int& start1, int end1, int& start2, int end2)
{
    int time = 0;
    while (start1 != end1) {
        start1 += moveEitherDirection(start1, end1);
        start2 += moveEitherDirection(start2, end2);
        time++;
    }
    start2 += moveEitherDirection(start2, end2);
    return ++time;
}

int moveEitherDirection(int start, int end)
{
    if (start < end) {
        return 1;
    } else if (start > end) {
        return -1;
    }
    return 0;
}
