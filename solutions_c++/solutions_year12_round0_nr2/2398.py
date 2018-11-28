
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>

#include <vector>
#include <map>
#include <set>

#include <algorithm>

template <class T>
std::string to_str(T t) {
    std::stringstream ss;
    ss << t;
    return ss.str();
}
void output(const std::string& str);

std::string solve_case(const std::string& str) {

    std::stringstream ss;
    ss << str;
    int N, S, p;
    ss >> N;
    ss >> S;
    ss >> p;

    std::vector<int> t;
    for (int i = 0; i < N; ++i) {
        int n;
        ss >> n;
        t.push_back(n);
    }
    std::sort(t.begin(), t.end());

    bool check = false;
    std::vector<int> max_score;

    for (int p_ = p; p_ <= 10; ++p_) {
        std::vector<int> max_score_;
        int surprising = 0;
        for (int i = 0, end = t.size(); i < end; ++i) {
            int t_ = t[i];
            if (t_ >= 29) { max_score_.push_back(10); continue; }
            if (t_ == 1) { max_score_.push_back(1); continue; }
            if (t_ == 0) { max_score_.push_back(0); continue; }
            int temp = t_ - (p_ + p_ - 2);
            if (surprising < S && p_ - 2 <= temp && temp <= p_) {
                ++surprising;
                max_score_.push_back(p_);
                continue;
            }
            if (t_ % 3 == 0) { max_score_.push_back(t_ / 3); continue; }
            max_score_.push_back(t_ / 3 + 1);
        }
        //if (S == surprising) {
            check = true;
            max_score = max_score_;
            break;
        //}
    }

    if (!check) {
        return "error";
    }

    int ret = 0;
    for (std::size_t i = 0, end = max_score.size(); i < end; ++i) {
        if (max_score[i] >= p) ++ret;
    }

    return to_str(ret);

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
