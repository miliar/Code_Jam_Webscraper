#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <map>

class ElementChecker {

private:

    std::map< std::pair< char, char >, char > combineTo_;
    std::map< std::pair< char, char >, bool > isOpposed_;

public:

    ElementChecker(const std::vector< std::string > &combines,
            const std::vector< std::string > &opposeds) {

        for (char ch0 = 'A'; ch0 <= 'Z'; ch0++) {

            for (char ch1 = ch0; ch1 <= 'Z'; ch1++) {

                for (std::vector< std::string >::const_iterator it = combines.begin();
                        it != combines.end();
                        it++) {

                    if ((it->at(0) == ch0 && it->at(1) == ch1) ||
                            (it->at(0) == ch1 && it->at(1) == ch0)) {

                        combineTo_[std::make_pair< char, char >(ch0, ch1)] = it->at(2);
                        combineTo_[std::make_pair< char, char >(ch1, ch0)] = it->at(2);
                    }
                }

                for (std::vector< std::string >::const_iterator it = opposeds.begin();
                        it != opposeds.end();
                        it++) {

                    if ((it->at(0) == ch0 && it->at(1) == ch1) ||
                            (it->at(0) == ch1 && it->at(1) == ch0)) {

                        isOpposed_[std::make_pair< char, char >(ch0, ch1)] = true;
                        isOpposed_[std::make_pair< char, char >(ch1, ch0)] = true;
                    }
                }
            }
        }
    }

    const char combineTo(const char ch0, const char ch1) const {

        std::map< std::pair< char, char >, char >::const_iterator it =
                combineTo_.find(std::make_pair< char, char >(ch0, ch1));

        if (it != combineTo_.end()) {

            return it->second;
        }
        else {

            return 0;
        }
    }

    const bool isOpposed(const char ch0, const char ch1) const {

        std::map< std::pair< char, char >, bool >::const_iterator it =
                isOpposed_.find(std::make_pair< char, char >(ch0, ch1));

        if (it != isOpposed_.end()) {

            return it->second;
        }
        else {

            return false;
        }
    }
};

const std::string check_combine(
        const ElementChecker &checker,
        const std::string &elements) {

    if (elements.length() < 2) {

        return elements;
    }

    const char ch0 = elements.at(elements.length() - 2);
    const char ch1 = elements.at(elements.length() - 1);

    const char combineTo = checker.combineTo(ch0, ch1);

    if (combineTo != 0) {

        return elements.substr(0, elements.length() - 2) + combineTo;
    }
    else {

        return elements;
    }
}

const std::string check_opposed(
        const ElementChecker &checker,
        const std::string &elements) {

    if (elements.length() == 0) {

        return elements;
    }

    const char element = elements.at(elements.length() - 1);

    for (std::string::const_iterator it = elements.begin();
            it != elements.end() - 1;
            it++) {

        if (checker.isOpposed(*it, element)) {

            return std::string();
        }
    }

    return elements;
}

const std::string make_answer(const std::string &elements) {

    std::string answer = "[";

    if (elements.length() > 0) {

        for (std::string::const_iterator it = elements.begin();
                it != elements.end();
                it++) {

            answer += *it;
            answer += ", ";
        }

        answer = answer.substr(0, answer.length() - 2);
    }

    answer += "]";

    return answer;
}

int main(int argc, char **argv) {

    int T;
    std::cin >> T;
    for (int t = 1; t <= T; t++) {

        std::vector< std::string > combines;
        int C;
        std::cin >> C;
        for (int c = 0; c < C; c++) {

            std::string combine;
            std::cin >> combine;
            combines.push_back(combine);
        }

        std::vector< std::string > opposeds;
        int D;
        std::cin >> D;
        for (int d = 0; d < D; d++) {

            std::string opposed;
            std::cin >> opposed;
            opposeds.push_back(opposed);
        }

        int N;
        std::cin >> N;

        std::string origin;
        std::cin >> origin;

        assert(static_cast< int >(origin.length()) == N);

        std::string elements;
        ElementChecker checker(combines, opposeds);

        for (int n = 0; n < N; n++) {

            elements += origin.at(n);
            elements = check_combine(checker, elements);
            elements = check_opposed(checker, elements);
        }

        std::string answer = make_answer(elements);
        std::cout << "Case #" << t << ": " << answer << std::endl;
    }

    return 0;
}
