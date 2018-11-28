#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <map>

int main() {

    std::map<int, std::vector<int> > recycled;
    for(int i=10; i < 2000001; ++i) {
        std::stringstream sstream;
        sstream << i;
        std::string tmp = sstream.str();

        std::string::iterator it;
        for(it=tmp.begin(); it != tmp.end(); ++it) {
            std::string rotated(tmp);
            std::rotate_copy(tmp.begin(), it, tmp.end(), rotated.begin());

            if(rotated[0] != '0' && (! std::equal(tmp.begin(), tmp.end(), rotated.begin()))) {
                int rotate = atoi(rotated.c_str());
                std::vector<int>::iterator it = std::find(recycled[i].begin(), recycled[i].end(), rotate);
                if(it == recycled[i].end()) {
                    recycled[i].push_back(rotate);
                }
            }
        }
    }

    int t;
    std::cin >> t;
    for(int i=0; i < t; ++i) {
        int a, b, count = 0;
        std::cin >> a >> b;

        for(int j=a; j < b; ++j) {
            for(std::vector<int>::iterator it=recycled[j].begin(); it != recycled[j].end(); ++it) {
                if(*it <= b && j < *it) { ++count;}
            }
        }
        
        std::cout << "Case #" << i+1 << ": " << count << std::endl;
    }

    return 0;
}

