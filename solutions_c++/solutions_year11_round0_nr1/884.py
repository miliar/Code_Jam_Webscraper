#include <iostream>
#include <vector>
#include <algorithm>

std::vector<size_t>  Buttons, Orange, Blue;

void ReadData() {
    Buttons.clear();
    Orange.clear();
    Blue.clear();
    size_t n;
    std::cin >> n;
    for (; n > 0; --n) {
        char color;
        size_t button;
        std::cin >> color >> button;
        if (color == 'O')
            Orange.push_back(Buttons.size());
        else
            Blue.push_back(Buttons.size());
        Buttons.push_back(button);
    }
}

size_t Work() {
    const size_t INF = 1000;
    size_t oPos = 1, bPos = 1, oIdx = 0, bIdx = 0, res = 0;
    for (; oIdx < Orange.size() || bIdx < Blue.size(); ) {
        size_t oNum = oIdx < Orange.size() ? Orange[oIdx] : INF;
        size_t bNum = bIdx < Blue.size() ? Blue[bIdx] : INF;
        size_t oTarget = oIdx < Orange.size() ? Buttons[Orange[oIdx]] : oPos;
        size_t bTarget = bIdx < Blue.size() ? Buttons[Blue[bIdx]] : bPos;
        size_t oDist = std::abs(static_cast<int>(oTarget - oPos));
        size_t bDist = std::abs(static_cast<int>(bTarget - bPos));
        //std::cout << oPos << " " << oTarget << " " << oDist << std::endl;
        //std::cout << bPos << " " << bTarget << " " << bDist << std::endl << std::endl;
        if (oNum < bNum) {
            res += (oDist + 1);
            oPos = oTarget;
            ++oIdx;
            bPos += ((bTarget > bPos ? 1 : -1) * std::min(oDist + 1, bDist));
        } else {
            res += (bDist + 1);
            bPos = bTarget;
            ++bIdx;
            oPos += ((oTarget > oPos ? 1 : -1) * std::min(bDist + 1, oDist));
        }
    }
    return res;
}

void Output(size_t k, size_t res) {
    std::cout << "Case #" << k << ": " << res << std::endl;
}

int main() {
    size_t t;
    std::cin >> t;
    for (size_t i = 1; i <= t; ++i) {
        ReadData();
        Output(i, Work());
    }
    return 0;
}

