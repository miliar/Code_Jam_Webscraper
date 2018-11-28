#include <iostream>
#include <vector>
#include <string>


typedef std::vector<std::string> TMatrix;

bool Work(TMatrix &m) {
    size_t N, M;
    std::cin >> N >> M;
    for (size_t i = 0; i < N; ++i) {
        std::string line;
        std::cin >> line;
        m.push_back(line);
    }
    for (size_t i = 0; i < N; ++i) {
        for (size_t j = 0; j < M; ++j) {
            if (m[i][j] == '#') {
                if (i + 1 >= N || j + 1 >= M)
                    return false;
                if (m[i + 1][j] != '#' || m[i][j + 1] != '#' || m[i + 1][j + 1] != '#')
                    return false;
                m[i][j] = '/';
                m[i][j + 1] = '\\';
                m[i + 1][j] = '\\';
                m[i + 1][j + 1] = '/';
            }
        }
    }
    return true;
}

void Output(size_t k, bool res, const TMatrix &m) {
    std::cout << "Case #" << k << ": " << std::endl;
    if (res) {
        for (TMatrix::const_iterator it = m.begin(), end = m.end(); it != end; ++it)
            std::cout << *it << std::endl;
    } else {
        std::cout << "Impossible" << std::endl;
    }
}

int main() {
    size_t t;
    std::cin >> t;
    for (size_t i = 1; i <= t; ++i) {
        TMatrix m;
        Output(i, Work(m), m);
    }
    return 0;
}

