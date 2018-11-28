
#include <string>
#include <iostream>
#include <fstream>

const char* table = "yhesocvxduiglbkrztnwjpfmaq";

std::string translate(const std::string& str) {
    std::string s(str);
    for (std::size_t i = 0, end = s.size(); i < end; ++i) {
        s[i] = table[s[i] - 'a'];
    }
    return s;
}

int main(int argc, const char** argv) {

    if (argc <= 1) {
        return -1;
    }

    std::string path(argv[1]);
    std::ifstream ifs(path.c_str());

    if (ifs.fail()) {
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
        std::cout << "Case #" << n << ": " << translate(str) << std::endl;
    }

    return 0;

}
