// 
// File:   egg_drop.cpp
// Author: rsalmeidafl
//
// Created on 26 de Junho de 2008, 22:52
//

#include <iostream>
#include <map>
#include <string>

using namespace std;
typedef map<string, bool> CQueryList;

int main(int argc, char** argv) {
    
    int num_of_instances;
    int current_instance = 0;
    string getlinefix;
    
    cin >> num_of_instances;
    
    while (current_instance++ < num_of_instances) {
        int number_of_search_engines;
        cin >> number_of_search_engines;
        getline(cin, getlinefix);
        
        /* We don't need to know the name of the search engines, unless
         * optimization turns out to be necessary */
        string unused;
        int i = number_of_search_engines;
        while (i--)
            getline(cin, unused);
        
        int number_of_queries;
        cin >> number_of_queries;
        getline(cin, getlinefix);
        
        CQueryList query_list;
        int number_of_switches = 0;
        
        while (number_of_queries--) {
            string  thisQuery;
            getline(cin, thisQuery);
            
            CQueryList::const_iterator iter = query_list.find(thisQuery);
            if (iter == query_list.end()) {
                // cout << "First occurence of " << thisQuery << '\n';
                if (query_list.size() + 1 == number_of_search_engines) {
                    number_of_switches++;
                    query_list.clear();
                }
                query_list[thisQuery] = true;
            }
        }
        
        cout << "Case #" << current_instance << ": " << number_of_switches << '\n';
    }    
    
    return (EXIT_SUCCESS);
}

