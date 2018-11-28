#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

int GetDigit(const char chr) {
    if (isalpha(chr)) {
        return chr + 10 - 'A';
    } else {
        return chr - '0';
    }
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int testCasesCount;
    std::cin >> testCasesCount;
    for (int testCaseIndex = 1; testCaseIndex <= testCasesCount; ++testCaseIndex) {
        int width, height;
        scanf("%i%i\n", &width, &height);
        std::vector< std::vector<int> > board(width, std::vector<int>(height));
        for (int i = 0; i < width; ++i) {
            std::string row;
            std::cin >> row;
            for (int j = 0; j < height / 4; ++j) {
                char d = GetDigit(row[j]);
                board[i][4 * j] = (d >> 3) & 1;
                board[i][4 * j + 1] = (d >> 2) & 1;
                board[i][4 * j + 2] = (d >> 1) & 1;
                board[i][4 * j + 3] = (d >> 0) & 1;
            }
        }

        std::cerr << "complete\n";
        std::vector< std::pair<int, int> > answers;
        for (int size = std::min(width, height); size >= 1; --size) {
            int count = 0;
            for (int i = 0; i <= width - size; ++i) {
                for (int j = 0; j <= height - size; ++j) {
                    if (board[i][j] > 1) {
                        continue;
                    }
                    bool flag = true;
                    for (int k = 1; k < size; ++k) {
                        for (int l = 1; l < size; ++l) {
                            if (board[i + k][j + l] <= 1) {
                                if (board[i + k - 1][j + l - 1] != board[i + k][j + l]) {
                                    flag = false;
                                    break;
                                }
                                if (board[i + k - 1][j + l] != 1 - board[i + k][j + l]) {
                                    flag = false;
                                    break;
                                }
                                if (board[i + k][j + l - 1] != 1 - board[i + k][j + l]) {
                                    flag = false;
                                    break;
                                }
                            } else {
                                flag = false;
                                break;
                            }
                        }
                    }
                    if (flag) {
                        for (int k = 0; k < size; ++k) {
                            for (int l = 0; l < size; ++l) {
                                board[i + k][j + l] = 2;
                            }
                        }
                        ++count;
                    }
                }
            }
            if (count > 0) {
                answers.push_back(std::make_pair(size, count));
            }
        }

        std::cout << "Case #" << testCaseIndex << ": " << answers.size() << std::endl;
        for (int s = 0; s < answers.size(); ++s) {
            std::cout << answers[s].first << " " << answers[s].second << std::endl;
        }
    }

    return 0;
}
