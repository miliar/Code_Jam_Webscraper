#include <iostream>

typedef unsigned long long ull;
typedef long long ll;

inline ull length(ull i)
{
    ull res = 1;
    i /= 10;
    while (i) {
        res *= 10;
        i /= 10;
    }
    return res;
}

inline ull rotate(ull i)
{
    if (i == 0) return 0;
    ull len = length(i);
    while (i % 10 == 0)
        i = i / 10;
    return len * (i % 10) + i / 10;
}

inline ull test(ull i, ull A, ull B)
{
    if (i < 10) return 0;
    ull sum = 0;
    ull first = i;
    while ((i = rotate(i)) != first)
        if (i >= A && i <= B)
            ++sum;
    return sum;
}

ull count(ull A, ull B)
{
    ull sum = 0;
    for (ull i = A; i <= B; ++i)
        sum += test(i, A, B);
    return sum / 2;
}

using namespace std;

int main(int argc, const char* argv[])
{
    size_t T;
    cin >> T;
    for (size_t test = 1; test <= T; ++test) {
        ull A, B;
        cin >> A >> B;
        cout << "Case #" << test << ": " << count(A, B) << std::endl;
    }
    return 0;
}
