#include <iostream>
#include <string>
#include <set>

int main () {
    
    int cases;
    std::cin >> cases;
    
    for (int case_num = 1; case_num <= cases; ++case_num) {
        
        int num_engines;
        std::cin >> num_engines;
        
        //std::cout << "Number of engines is " << num_engines << std::endl;
        
        for (int i=0; i<=num_engines; ++i) {
            std::cin.ignore (128, '\n');
        }
        
        //std::cout << "Done reading engines" << std::endl;
        
        int num_queries;
        std::cin >> num_queries;
        std::cin.ignore (128, '\n');
        
        int switches = 0;
        
        std::set<std::string> encountered;
        
        while (num_queries--) {
            
            std::string query;
            std::getline (std::cin, query);
            
            encountered.insert (query);
            
            if (encountered.size() == num_engines) {
                ++switches;
                encountered.clear();
                encountered.insert (query);
            }
        }
        
        std::cout << "Case #" << case_num << ": " << switches << std::endl;
    }
}
