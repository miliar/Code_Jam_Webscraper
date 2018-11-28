#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cassert>

const int NUM_OF_BITS = 20;

int main(int argc, char **argv) {

    int T;
    std::cin >> T;
    for (int t = 1; t <= T; t++) {

        std::vector< int > candies;
        std::vector< int > bits(NUM_OF_BITS, 0);

        int N;
        std::cin >> N;
        for (int n = 0; n < N; n++) {

            int candy;
            std::cin >> candy;

            candies.push_back(candy);

            for (int index = 0; index < NUM_OF_BITS; index++) {

                if (candy % 2) {

                    bits[index]++;
                }

                candy >>= 1;
            }
        }

        bool possibility = true;
        for (int index = 0; index < NUM_OF_BITS; index++) {

            if (bits[index] % 2) {

                possibility = false;

                break;
            }
        }

        std::string answer;
        if (possibility) {

            std::sort(candies.begin(), candies.end());

            assert(candies.size() > 1);

            int sum = 0;
            for (int index = 1, size = candies.size(); index < size; index++) {

                sum += candies[index];
            }

            std::stringstream sin;
            sin << sum;
            answer = sin.str();
        }
        else {

            answer = "NO";
        }

        std::cout << "Case #" << t << ": " << answer << std::endl;
    }

    return 0;
}
