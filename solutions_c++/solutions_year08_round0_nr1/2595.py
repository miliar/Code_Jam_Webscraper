/* Built using:
 * g++ (GCC) 4.1.2 20071124 (Red Hat 4.1.2-42)
 */
#include <fstream>
#include <iostream>
#include <vector>
#include <set>
using namespace std;

// For random number generation
#include <stdlib.h>
#include <time.h>

struct ltstr
{
  bool operator()(const char* s1, const char* s2) const
  {
    return strcmp(s1, s2) < 0;
  }
};

class MinSwitches {
 public:
  int find_min_switches(vector<string> &search_engines, vector<string> &queries);
};
int MinSwitches::find_min_switches(vector<string> &search_engines, vector<string> &queries)
{
  int min_switches = 0;
  set<string> se_set;
  if(search_engines.size() == 0 || queries.size() == 0) return 0;
  for(int i = 0; i < search_engines.size(); i++) {
    se_set.insert(search_engines[i]);
  }
  se_set.erase(queries[0]);

  for(int i = 1; i < queries.size(); i++) {
    if(se_set.find(queries[i]) == se_set.end()) continue;
    if(se_set.size() == 1) {
      min_switches++;
      for(int j = 0; j < search_engines.size(); j++) {
	se_set.insert(search_engines[j]);
      }
      se_set.erase(queries[i]);
    } else {
      se_set.erase(queries[i]);
    }
  }

  return min_switches;
}

class TestCaseGen {
public:
  void test_case_gen(int num_cases, int max_engine_num, int max_queries_num, bool use_max_vals_only=false) {
    ofstream ostr("test.txt");
    ostr << num_cases << endl;
    int i = 0;
    string list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789";
    vector<string> engine_list;
    srand(time(NULL));
    while(i < num_cases) {
      engine_list.clear();
      int num_eng = use_max_vals_only ? max_engine_num : 1+rand()%max_engine_num;
      ostr << num_eng << endl;
      for(int k = 0; k < num_eng; k++) {
	int numchars = 1+rand()%99;
	string str("");
	for(int j = 0; j < numchars; j++) {
	  str += list[rand()%list.size()];
	}
	engine_list.push_back(str);
	ostr << str << endl;
      }
      
      //srand(time(NULL));
      int num_queries = use_max_vals_only ? max_queries_num : 1+rand()%max_queries_num;
      ostr << num_queries << endl;
      for(int k = 0; k < num_queries; k++) {
	ostr << engine_list[rand()%engine_list.size()] << endl;
      }
      
      i++;
    }
    ostr.close();
  }
};

int main(int argc, char*argv[])
{
  if(argc < 2) {
    TestCaseGen tc;
    int num_test_cases = 20;
    int max_engines = 100;
    int max_queries = 1000;
    bool use_max_vals_only = false;
    tc.test_case_gen(num_test_cases, max_engines, max_queries, use_max_vals_only);
    return 0;
  }

  ifstream readtest( argv[1] );

  MinSwitches ms;

  int num_cases = 0;
  readtest >> num_cases;

  for(int testcase = 0; testcase < num_cases; testcase++) {
    int num_search_engines = 0;
    readtest >> num_search_engines;

    vector<string> search_engines;
    char tmp[100];
    readtest.getline(tmp,100); // Get the \n character before proceeding
    for(int i = 0; i < num_search_engines; i++) {
      char s_eng[101];
      readtest.getline(s_eng,100);
      search_engines.push_back(s_eng);
    }
    
    int num_queries = 0;
    readtest >> num_queries;

    readtest.getline(tmp,100);
    vector<string> queries;
    for(int i = 0; i < num_queries; i++) {
      char query[101];
      readtest.getline(query,100);
      queries.push_back(query);
    }

    cout << "Case #" << testcase+1 << ": " << ms.find_min_switches(search_engines, queries) << endl;
    //reverse(queries.begin(), queries.end());
    //cout << ms.find_min_switches(search_engines, queries) << endl;
  }
  readtest.close();
  
  return 0;
}
