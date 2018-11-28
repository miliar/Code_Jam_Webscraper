#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct elemento {
    int number, frequency;
};

int ncases, P, K, L;
elemento v[1100], v2[1100];
int posicoes[1100];

int compare2(const void *a, const void *b) {
    elemento *p1 = (elemento *) a;
    elemento *p2 = (elemento *) b;
    return (p2->frequency - p1->frequency);// reverse sort
}

int main() {

    int i, j, temp_i;

    cin >> ncases;

    for (i=0; i<ncases; i++) {

        cin >> P >> K >> L;

        for (j=0; j<L; j++) {
            cin >> temp_i;
            v[j].number = v2[j].number = j+1;
            v[j].frequency = v2[j].frequency = temp_i;
        }

        qsort(v, L, sizeof(elemento), compare2);

        int pos = 1;
        int key = 1;
        for (j=0; j<L; j++) {
            if (key > K) {
                ++pos;
                key = 1;
            }
            posicoes[v[j].number] = pos; // posicoes comeca do 1
            ++key;
        }

        /*for (j=0; j<L; j++) {
            cout << posicoes[j+1] << ',';
        }*/
        int t = 0;
        for (j=0; j<L; j++) {
            t = t + posicoes[j+1] * v2[j].frequency;
            //cout << posicoes[j+1] << " = " << v2[j].frequency << endl;
        }

        cout << "Case #" << i+1 << ": " << t << endl;

    }

}
