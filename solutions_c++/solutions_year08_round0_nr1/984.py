#include <iostream>
#include <string>
#include <sstream>
#include <set>

using namespace std;

int main()
{
    int num_of_cases;
    int count = 0;
    string inputline;
    getline(cin, inputline);
    stringstream line;
    num_of_cases = atoi(inputline.c_str());
    while(num_of_cases > count)
    {
        int num_of_switches = 0;
        ++count;
        //cout << "Processing Case#" << count << endl;
        int num_of_engines;
        getline(cin, inputline);
        //cout << "Inputline is :" << inputline << endl;
        num_of_engines = atoi(inputline.c_str());
        //cout << "Number of engines is " << num_of_engines << endl;
        set<string> engines;

        string name;
        
        for(int i=0; i < num_of_engines; ++i)
        {
            getline(cin,name);
            //cout << "Processing search engine: " << name << endl;
        }
        

        int num_of_queries;
        getline(cin, inputline);
        num_of_queries = atoi(inputline.c_str());
        //cout << "Num of queries for this case are " << num_of_queries << endl;
        int querynum = 0;
        while(num_of_queries > 0)
        {
            ++querynum;
            //cout << "Processing query #" << querynum << endl;
            string query;
            getline(cin, query);
            if ((engines.insert(query).second) && (engines.size() == num_of_engines))       
            {
                ++num_of_switches;
                engines.clear();
                engines.insert(query);
            }
            --num_of_queries;
        }
       cout << "Case #" << count << ": " << num_of_switches << endl; 
    }
    return 0; 
}
