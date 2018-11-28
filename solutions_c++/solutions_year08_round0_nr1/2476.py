#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream in_file;
    ofstream out_file;
    string line;
    int test_case_count;
    int current_test_case;
    int search_engine_count;
    vector<string> search_engines;
    int search_term_count;
    vector<string> search_terms;
    istringstream strin;
    int no_of_switches;
    int exit_condition;
    int switch_position;
    int search_engine_location;
    
    //loop variables
    int i;
    int j;
    int k;
    int l;
 
    in_file.open("A-large.in", ios::binary);
    out_file.open("A-large.out", ios::binary);
    if(in_file.is_open()) 
    {
      getline(in_file, line);
      istringstream strin(line);
      strin >> test_case_count;
      cout << "test case count = " << test_case_count << endl;
      
      //we have the number of test cases now in test_case_count.
      //so start a loop for the number of test cases.
      for(i=0; i < test_case_count; i++)
      {
       //current_test_case++;
       cout << endl << "iteration = " << i << endl;
       
       //read the number of search engines
       getline(in_file, line);
       istringstream strin1(line);
       strin1 >> search_engine_count;
       cout << "search engine count = " << search_engine_count << endl;
       
       //now we have number of search engines,
       //so read the next X search engine entries
       for(j=0; j < search_engine_count; j++)
       {
        getline(in_file, line);
        cout << "engine = " << line << endl;
        search_engines.push_back(line);
       }
       
       //now read the number of search queries
       getline(in_file, line);
       istringstream strin2(line);
       strin2 >> search_term_count;
       cout << "search term count = " << search_term_count << endl;
       
       //number of search terms can be zero
       //check that condition and output to file if zero
       if(search_term_count == 0)
       {
        out_file << "Case #" << i+1 << ": " << "0" << "\n";
        continue;                    
       }
       
       //now read the next X search queries
       for(j=0; j < search_term_count; j++)
       {
        getline(in_file, line);
        cout << "term = " << line << endl;
        search_terms.push_back(line);
       }
        
/*****************Start of Main Logic***************/

        //find the search engine in the list of queries
        //whose first occurance appears last
        no_of_switches = 0;
        exit_condition = 0;
        do
        {
         switch_position = -1;
         //looping through each search engine to find 
         //its occurance in the search terms      
         for(k=0; k < search_engine_count; k++)
         {
          search_engine_location = -1;
          cout << "engine = " << search_engines[k] << endl;
          
          for(l=0; l < search_term_count; l++)
          {
           cout << "term = " << search_terms[l] << endl;
           if(search_terms[l] == search_engines[k])
           {
            //if a search engine was found in the list of terms
            //then record that position of the find
            search_engine_location = l;
            cout << "engine location = " << l << endl;
            //there is a find. so terminate current loop.
            break;
           }
          }
          
          //if search engine not found,
          //end the test case and write to file
          if(search_engine_location == -1)
          {
           out_file << "Case #" << i+1 << ": " << no_of_switches << "\n";
           cout << "*** exiting ***  " << no_of_switches << endl;
           exit_condition = 1;
           break;
          }
         
          //if a search engine was found
          //and if the found position was higher than the current
          //switch position, then note it down
          if(search_engine_location > switch_position)
          {
           switch_position = search_engine_location;
           cout << "Switch pos = " << switch_position << endl;
          }
         }
         
         //now we have processed till the point where a switch has to be made
         //so delete all search terms till the position of switch
         if(!exit_condition)
         {
          search_terms.erase(search_terms.begin(),search_terms.begin()+switch_position);
          search_term_count = search_terms.size();
          no_of_switches++;
          cout << "switches = " << no_of_switches << endl;
         }
        }while(!exit_condition);
        
        //clear vectors and vars
        search_terms.clear();
        search_engines.clear();
      }       
    }
    in_file.close();
    out_file.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
