#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

typedef vector<unsigned long> Pile_t;

unsigned long patrickAdd(unsigned long a, unsigned long b);
unsigned long seanAdd(unsigned long a, unsigned long b);
bool patrickCry(unsigned long* seanPile, unsigned long seanSize, unsigned long* patrickPile, unsigned long patrickSize);
unsigned long realPileValue(unsigned long* pile, int size);
unsigned long patrickPileValue(unsigned long* pile, int size);

int unsigned_long_cmp(const void *a, const void *b)
{
    return (*(unsigned long*)a - *(unsigned long*)b);
}

unsigned long patrickAdd(unsigned long a, unsigned long b) {
    unsigned long mask = ~(a & b);
    return (a&mask) + (b&mask);
}

unsigned long seanAdd(unsigned long a, unsigned long b) {
    return a + b;
}

bool patrickCry(unsigned long* seanPile, unsigned long seanSize, unsigned long* patrickPile, unsigned long patrickSize) {
    return (patrickPileValue(seanPile, seanSize) != patrickPileValue(patrickPile, patrickSize));
}

unsigned long split(unsigned long* sweetArray, unsigned long N) {
    qsort(sweetArray, N, sizeof(unsigned long), unsigned_long_cmp);

    for (unsigned long k = 1; k < N; k++) {
        unsigned long* seanPile = sweetArray + k;
        unsigned long seanSize = N-k;
        unsigned long* patrickPile = sweetArray;
        unsigned long patrickSize = k;

        if (!patrickCry(seanPile, seanSize, patrickPile, patrickSize)) {
            return realPileValue(seanPile, seanSize);
        }
    }

    return 0;
}

unsigned long patrickPileValue(unsigned long* pile, int size) {
    unsigned long value = 0;

    for (unsigned long k = 0; k < size; k++) {
        value = patrickAdd(value, pile[k]);
    }

    return value;
}

unsigned long realPileValue(unsigned long* pile, int size) {
    unsigned long value = 0;

    for (unsigned long k = 0; k < size; k++) {
        value += pile[k];
    }

    return value;
}

int main(int argc, const char *argv[])
{
    unsigned long T = 0;
    cin >> T;

    for (unsigned long k = 0; k < T; k++) {
        unsigned long N = 0;
        cin >> N;

        unsigned long* sweetPile = new unsigned long[N];

        for (unsigned long j = 0; j < N; j++) {
            cin >> sweetPile[j];
        }

        unsigned long seanValue = split(sweetPile, N);

        cout << "Case #" << k+1 << ": ";
        if (seanValue == 0) {
            cout << "NO";
        } else {
            cout << seanValue;
        }

        cout << endl;

        delete [] sweetPile;
    }

    return 0;
}
