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

void Split(std::string path, std::vector<std::string> &dirs) {
    path = path.substr(1);
    while (true) {
        int slashPos = path.find_first_of("/");
        if (slashPos != std::string::npos) {
            dirs.push_back(path.substr(0, slashPos));
            path = path.substr(slashPos + 1);
        } else {
            dirs.push_back(path);
            break;
        }
    }
}

struct TrieNode {
    std::map<std::string, int> children;
};

int Insert(std::vector<TrieNode> &trie, const std::string &path) {
    std::vector<std::string> dirs;
    Split(path, dirs);
    int count = 0;
    int node = 0;
    for (std::vector<std::string>::const_iterator it = dirs.begin(); it != dirs.end(); ++it) {
        const std::string &dir = *it;
        std::map<std::string, int>::iterator found = trie[node].children.find(dir);
        if (found != trie[node].children.end()) {
            node = found->second;
        } else {
            trie.push_back(TrieNode());
            trie[node].children[dir] = trie.size() - 1;
            node = trie.size() - 1;
            ++count;
        }
    }
    return count;
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int testCasesCount;
    std::cin >> testCasesCount;
    for (int testCaseIndex = 1; testCaseIndex <= testCasesCount; ++testCaseIndex) {
        int n, m;
        scanf("%i%i\n", &n, &m);

        std::vector<TrieNode> trie;
        trie.push_back(TrieNode());
        for (int i = 0; i < n; ++i) {
            std::string path;
            std::cin >> path;
            Insert(trie, path);
        }
        int count = 0;
        for (int i = 0; i < m; ++i) {
            std::string path;
            std::cin >> path;
            count += Insert(trie, path);
        }

        std::cout << "Case #" << testCaseIndex << ": " << count << std::endl;

    }

    return 0;
}
