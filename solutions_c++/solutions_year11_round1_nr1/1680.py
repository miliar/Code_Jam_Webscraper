#include <iostream>

bool Work() {
    int PG, PD, N;
    std::cin >> N >> PD >> PG;
    if (PG == 100 && PD != 100)
        return false;
    if (PG == 0 && PD != 0)
        return false;
    int QD = 100;
    if (PD % 4 == 0)
        QD /= 4;
    else if (PD % 2 == 0)
        QD /= 2;
    if (PD % 25 == 0)
        QD /= 25;
    else if (PD % 5 == 0)
        QD /= 5;
    return QD <= N;
}

void Output(int t, bool res) {
    std::cout << "Case #" << t << ": " << (res ? "Possible" : "Broken") << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 1; i <= t; ++i) {
        Output(i, Work());
    }
    return 0;
}

