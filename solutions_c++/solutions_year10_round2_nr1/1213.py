#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>
#include <stack>
#include <stdexcept>
#include <gmpxx.h>

#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string/classification.hpp>
#include <boost/smart_ptr.hpp>

using namespace std;

struct Node 
{
    std::map<std::string,Node> children;
};

size_t insert (std::vector<std::string>& path, Node* root) 
{
    size_t ret = 0;
    Node* current_node = root;
    for(size_t i = 0; i < path.size(); ++i) 
    {
        // std::cerr << "'" << path[i] << "'" << std::endl;
        if (!current_node->children.count (path[i])) 
        {
            ++ret;

        }
        current_node = &current_node->children[path[i]];
    }
    return ret;
}

   

int main() {

    int num_cases;
    cin >> num_cases;
    cin.ignore();
  
    for (int case_num = 1; case_num <=  num_cases; ++case_num) {
        cout << "Case #" << case_num << ": ";
        string line;
        getline (cin,line);
        int n,m;
        {
            istringstream is (line);
            is >> n>> m;
        }
        //std::cerr << n << " " << m << std::endl;
        
        Node root;
        for (int i = 0; i < n; ++i) 
        {
            getline (cin,line);
            if (line == "/") continue;
            line = line.substr (1);
            std::vector<std::string> path;
            boost::split (path,line,boost::is_any_of ("/"),boost::token_compress_on);
            insert (path,&root);
        }
        size_t ret = 0;
        for (int i = 0; i < m; ++i) 
        {
            getline (cin,line);
            if (line == "/") continue;
            line = line.substr (1);
            std::vector<std::string> path;
            boost::split (path,line,boost::is_any_of ("/"),boost::token_compress_on);
            ret += insert (path,&root);
        }
        std::cout << ret << std::endl;
    }
}


