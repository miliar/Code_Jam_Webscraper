#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int C, D, N;
        string combine[36], opposed[28], invoke, elementList;

        cin >> C;
        for (int j = 0; j < C; j++) {
            cin >> combine[j];
        }

        cin >> D;
        for (int j = 0; j < D; j++) {
            cin >> opposed[j];
        }

        cin >> N >> invoke;
        for (int j = 0; j < N; j++) {
            elementList += invoke[j];
            if (elementList.length() < 2) {
                continue;
            }

            for (int k = 0; k < C; k++) {
                if (elementList[elementList.length() - 2] == combine[k][0] && elementList[elementList.length() - 1] == combine[k][1]
                    || elementList[elementList.length() - 2] == combine[k][1] && elementList[elementList.length() - 1] == combine[k][0]) {
                    elementList.erase(elementList.length() - 2);
                    elementList += combine[k][2];
                }
            }

            for (int k = 0; k < D; k++) {
                if (elementList.find_first_of(opposed[k][0]) != string::npos
                    && elementList.find_first_of(opposed[k][1]) != string::npos
                    && elementList.find_first_of(opposed[k][0]) != elementList.find_last_of(opposed[k][1])) {
                    elementList.erase();
                }
            }
        }

        printf("Case #%d: [", i + 1);
        for (int j = 0; j < elementList.length(); j++) {
            if (j > 0) {
                printf(", ");
            }
            printf("%c", elementList[j]);
        }
        printf("]\n");
    }
}
