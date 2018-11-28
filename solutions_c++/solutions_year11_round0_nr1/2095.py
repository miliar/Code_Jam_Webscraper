#include <iostream>
#include <vector>
#include <string>
#include <sstream>

enum Bot {

    ORANGE      = 0,
    BLUE        = 1,
};

const int theOtherBot(const int bot) {

    return (1 - bot);
}

int main(int argc, char **argv) {

    int T;
    std::cin >> T;
    for (int t = 1; t <= T; t++) {

        int positions[] = { 1, 1 };
        int times[] = { 0, 0 };

        int N;
        std::cin >> N;
        for (int n = 0; n < N; n++) {

            std::string botstr;
            std::cin >> botstr;

            int button;
            std::cin >> button;

            int bot;
            if (botstr.compare("O") == 0) {

                bot = ORANGE;
            }
            else {

                bot = BLUE;
            }

            const int distance = std::abs(positions[bot] - button);

            if (times[bot] + distance < times[theOtherBot(bot)]) {

                times[bot] = times[theOtherBot(bot)] + 1;
            }
            else {

                times[bot] += distance + 1;
            }

            positions[bot] = button;
            //std::cout << (bot == ORANGE ? "ORANGE" : "BLUE") << ": " << positions[bot] << ", " << times[bot] << std::endl;
        }

        int answer = std::max< int >(times[ORANGE], times[BLUE]);
        std::cout << "Case #" << t << ": " << answer << std::endl;
    }

    return 0;
}
