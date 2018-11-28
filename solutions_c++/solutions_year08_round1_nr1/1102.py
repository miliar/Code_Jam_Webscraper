#include <iostream>

using namespace std;

int ncases, nnums, v1[10], v2[10];

int compare(const void *a, const void *b) {
    return (*(int *) a - *(int *) b);
}

int compare2(const void *a, const void *b) {
    return (*(int *) b - *(int *) a);// reverse sort
}

int main() {

    int i, j, k, min;

    cin >> ncases;

    for (i=0; i<ncases; i++) {

        cin >> nnums;

        for (j=0; j<nnums; j++) {
            cin >> v1[j];
        }

        for (j=0; j<nnums; j++) {
            cin >> v2[j];
        }

        qsort(v1, nnums, sizeof(int), compare);
        qsort(v2, nnums, sizeof(int), compare2);

        int pscal = 0;
        for (int m=0; m<nnums; m++) {
            pscal+= v1[m] * v2[m];
       }

        cout << "Case #" << i+1 << ": " << pscal << endl;

    }

}
