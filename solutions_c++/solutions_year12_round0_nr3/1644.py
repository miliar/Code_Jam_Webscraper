#include <stdio.h>
#include <string.h>
#include <iostream>
#include <set>

using namespace std;

const uint64_t buflen = 10;

uint64_t rotate(char* digits, size_t len, size_t start_index) {
    uint64_t r = 0;
    for(int i = 0, j = start_index; i < len; ++i, ++j) {
        r = r * 10 + (digits[j % len] - '0');
    }
    return r;
}


uint64_t goodRotations(uint64_t n, uint64_t A, uint64_t B) {
    char buffer[buflen];
    sprintf(buffer, "%llu", n);
    size_t digits = strlen(buffer);
    set<uint64_t> rotations;
    for(size_t i = 0; i < digits; ++i) {
        uint64_t r = rotate(buffer, digits, i);
        if(A <= r && r <= B) {
            rotations.insert(r);
        }
    }
    if(n == *rotations.begin()) {
        return rotations.size();
    } else {
        return 0;
    }
}

int main() {
    size_t N;
    cin >> N;
    for(size_t i = 0; i < N; ++i) {
        uint64_t A, B;
        cin >> A >> B;
        uint64_t r = 0;
        for(size_t j = A; j <= B; ++j) {
            uint64_t g = goodRotations(j, A, B);
            r += g*(g - 1)/2;
        }
        cout << "Case #" << (i + 1) << ": " << r << endl;
    }
    return 0;
}



