// code_contest.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <cstdio>

using namespace std;

typedef struct __CASE
{
        __CASE(): se_no(0),query_no(0){};
        int se_no;
        string name[100];
        int query_no;
        string query[1000];
}TEST_CASE;

typedef struct __POS
{
        __POS() : pos(0), count(0){};
        int pos;
        int count;
}POS;

typedef map<string,POS> CONTAINER;


int main()
{
	string tmp;
	ifstream inFile("1.txt");
	map<int, TEST_CASE> diff_case;
	int N = 0;
	getline(inFile,tmp);
        N = atoi(tmp.c_str());

	int case_no = 1;

	while((!inFile.eof()) && (case_no <= N))
	{
//          cout<<"case_no "<< case_no<<endl;
	  TEST_CASE test;
          tmp.clear();
	  getline(inFile,tmp);
          int seq = atoi(tmp.c_str());
          test.se_no = seq;
//          cout<<seq<<endl;
      for(int i = 0; i < seq; i++)
	  {
		getline(inFile,test.name[i]);
//                cout<<"Engine: "<<test.name[i]<<endl;
      }
      tmp.clear();
      getline(inFile,tmp);
      int query_no = atoi(tmp.c_str());
//          cout<<"query_no"<<query_no<<endl;

      test.query_no = query_no;

      for(int i = 0; i < query_no; i++)
	  {
 		getline(inFile,test.query[i]);
//                cout<<"Query: "<<test.query[i]<<endl;
      } 
      diff_case.insert(make_pair(case_no,test));
      case_no++;
     }
        
     map<int, TEST_CASE>::iterator case_it;
     for(case_it = diff_case.begin();
      case_it != diff_case.end(); case_it++)
     {
//		cout<<"case no: "<< case_it->first<<endl;
		CONTAINER contain;
        TEST_CASE tmp = case_it->second;
//		cout<<"engine no: "<<tmp.se_no<<endl;
		for(int i = 0; i < tmp.se_no; i++)
		{
			POS pos;
			contain.insert(make_pair(tmp.name[i],pos));
//			cout<<"engine: "<<tmp.name[i]<<endl;
		}
//		cout<<"query_no: "<<tmp.query_no<<endl;
		int switch_no = 0;
		int rnd = 0;
              
//		int test_rnd = 0;
	
		while(rnd != (tmp.query_no-1))
		{
//        test_rnd++;
    
		  for (int i = rnd; i < tmp.query_no; i++) // boundary maybe error
		  {
//			  cout<<"round "<<test_rnd<<" "<<"query "<<i<<" "<<tmp.query[i]<<endl;
                          CONTAINER::iterator co_it 
				  = contain.find(tmp.query[i]);
			  if(co_it != contain.end())
			  {
				  if(co_it->second.count == 0)
				  {
					  co_it->second.pos = i;
				  }
				  co_it->second.count += 1;
			  }
		  }
		  CONTAINER::iterator chk_it;
		  bool is_all_zero = false;
		  int pos = 0;
		  for(chk_it = contain.begin();
			  chk_it != contain.end(); chk_it ++)
		  {
			  if(chk_it->second.pos > pos)
			  {
				 pos = chk_it->second.pos;
			  }
			  if(chk_it->second.count == 0)
			  {
				is_all_zero = true;
			  }
		  }
		  if(is_all_zero)
		  {
			switch_no += 0;
			rnd = (tmp.query_no - 1);
		  }
		  else
		  {
			switch_no ++;
//			rnd = pos+1;
			rnd = pos;
		  }
		  for(chk_it = contain.begin();
			  chk_it != contain.end(); chk_it++)
		  {
			  chk_it->second.count = 0;
			  chk_it->second.pos = 0;
		  }
		}
		cout<<"Case #"<<case_it->first<<": "<<switch_no<<endl;
//			cout<<"query: "<<tmp.query[i]<<endl;
     }

	return 0;
}

