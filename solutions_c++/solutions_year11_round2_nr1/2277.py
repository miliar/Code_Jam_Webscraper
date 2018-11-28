#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cassert>
#include <cmath>

int main(int argc, char **argv) {

    int T;
    std::cin >> T;
    for (int t = 1; t <= T; t++) {

        int N;
        std::cin >> N;
        std::vector<double> wins, looses, wps;
        std::vector<std::string> lines;

        for (int n = 0; n < N; n++) {

            std::string line;
            std::cin >> line;
            lines.push_back(line);

            double win = 0.0, loose = 0.0;

            for (int index = 0, size = line.length(); index < size; index++) {

                if (line[index] == '1') win += 1.0;
                else if (line[index] == '0') loose += 1.0;
            }

            wins.push_back(win);
            looses.push_back(loose);

            if (fabs(win) < 1e-15) wps.push_back(0.0);
            else wps.push_back(win / (win + loose));
        }

        std::vector<double> owps;

        for (int index0 = 0, size0 = lines.size(); index0 < size0; index0++) {

            std::string &line1 = lines[index0];

            int numops = 0;
            double owp = 0.0;

            for (int index1 = 0, size1 = line1.size(); index1 < size1; index1++) {

                if (line1[index1] != '.') {

                    numops++;
                    double win = 0.0, loose = 0.0;

                    std::string &line2 = lines[index1];

                    for (int index2 = 0, size2 = line2.size(); index2 < size2; index2++) {

                        if (index2 != index0) {

                            if (line2[index2] == '1') win += 1.0;
                            else if (line2[index2] == '0') loose += 1.0;
                        }
                    }

                    if (fabs(win) > 1e-15) owp += win / (win + loose);
                }
            }

            if (fabs(owp) < 1e-15) owps.push_back(0.0);
            else owps.push_back(owp / static_cast<double>(numops));
        }

        std::vector<double> oowps;

        for (int index0 = 0, size0 = lines.size(); index0 < size0; index0++) {

            std::string &line1 = lines[index0];

            int numops = 0;
            double oowp = 0.0;

            for (int index1 = 0, size1 = line1.size(); index1 < size1; index1++) {

                if (line1[index1] != '.') {

                    numops++;

                    oowp += owps[index1];
                }
            }

            if (fabs(oowp) < 1e-15) oowps.push_back(0.0);
            else oowps.push_back(oowp / static_cast<double>(numops));
        }

        std::cout << "Case #" << t << ":" << std::endl;

        for (int index = 0, size = lines.size(); index < size; index++) {

            double wp = wps[index];
            double owp = owps[index];
            double oowp = oowps[index];

            std::cout.precision(16);
            std::cout << 0.25 * wp + 0.50 * owp + 0.25 * oowp << std::endl;
        }
    }

    return 0;
}
