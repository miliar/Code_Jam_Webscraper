
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

#include <vector>
#include <map>
#include <set>

#include <algorithm>

#include <cmath>

template <class T>
std::string to_str(T t) {
    std::stringstream ss;
    ss << t;
    return ss.str();
}
void output(const std::string& str);

int digit(int n) {
    return static_cast<int>(std::log10(static_cast<double>(n))) + 1;
}

int rotate(int n, int d, int rot) {
    rot = rot % d;
    int l = static_cast<int>(std::pow(10.0, rot));
    int r = static_cast<int>(std::pow(10.0, d - rot));
    return  (n % r) * l + (n / r);
}

std::string solve_case(const std::string& str) {

    std::stringstream ss;
    ss << str;
    int A, B;
    ss >> A;
    ss >> B;

    std::set<std::pair<int, int> > recycled;
    for (int n = A; n < B; ++n) {
        int d = digit(n);
        for (int i = 1; i < d; ++i) {
            int rot = rotate(n, d, i);
            if (n < rot && rot <= B) {
                recycled.insert(std::make_pair(n, rot));
            }
        }
    }

    return to_str(recycled.size());

}

int main(int argc, const char** argv) {

    if (argc <= 1) {
        std::cerr << "input file" << std::endl;
        return -1;
    }

    std::string path(argv[1]);
    std::ifstream ifs(path.c_str());

    if (ifs.fail()) {
        std::cerr << "file open error" << std::endl;
        return -1;
    }

    std::string str;

    int num = 0;
    if (std::getline(ifs, str)) {
        sscanf(str.c_str(), "%d", &num);
    }
    else {
        return -1;
    }

    int n = 0;
    while (++n <= num && std::getline(ifs, str)) {
        output(solve_case(str));
    }

    return 0;

}

void output(const std::string& str) {
    static int case_ = 0;
    std::cout << "Case #" << ++case_ << ": " << str << std::endl;
}
