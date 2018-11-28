#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>
#include <ext/hash_map>


using namespace std;



int solveProblem(int S,int Q,int N, vector<string>& upperQueries, vector<string>& searchEngines);

string upperCase(string s)
{
  for(int i = 0; i < s.length(); i++)
    {
      if(isalpha(s[i]))
      {
	if(islower(s[i]))
	  s[i] = toupper(s[i]);
      }
    }
  return s;
}

int main()
{

  int N;
  string buf;
  
  //Inputing the number of tests
  cin>>N;

  getline(cin, buf);
  // cout<<N<<endl;
  vector<int> switches;

  //Starting the loop

  for(unsigned i = 0; i < N; i++)
    {
      int S, res;

      cin>>S;
    
      getline(cin, buf);
      
      vector<string> searchEngines(S);

      for(int i = 0; i < S; i++)
	{
	  getline(cin, searchEngines[i]);
	  searchEngines[i] = upperCase(searchEngines[i]);
       
	}
      
      int Q;
      cin>>Q;
 
      getline(cin, buf);
  
      vector<string> queries(Q);
      vector<string> upperQueries(Q);
      for(int i = 0; i < Q; i++)
	{
	  getline(cin, queries[i]);
	  upperQueries[i] = upperCase(queries[i]);
	  
	}
      res = solveProblem(S,Q,N, upperQueries, searchEngines);
     
      switches.push_back(res);
    }
  for(int i = 0; i < N; i++)
    {
      cout<<"Case #"<<i+1<<": "<<switches[i]<<endl;
    }


  return 0;
}
      

int solveProblem(int S, int Q,int N, vector<string>& upperQueries, vector<string>& searchEngines)
{
 
  
  
  
  sort(searchEngines.begin(), searchEngines.end());
  map<const char*, int> posFinder;
    
    for(int i = 0; i < S; i++)
      {
	posFinder[searchEngines[i].c_str()] = i;
      }

    int switcher = 0;
  
  vector<int> isFound(S,0);
  int count = 0;
  bool foundAll = false;
  unsigned int num = 0;
  unsigned int index = 0;

 
  
  
  while(num < Q)
    {
      
      int pos;
      for(int j = 0; j < S; j++)
	{
	  if(searchEngines[j] == upperQueries[num])
	     pos = j;
	}
	     
      
      int temp = isFound[pos]++;
      if(temp == 0)
	{
	  
	  count++;
	}
      if(count == S)
	{
	  
	  switcher++;
	 
	  count = 1;
	  for(int i = 0; i < S; i++)
	    {
	      isFound[i] = 0;
	    }
	  
	  isFound[pos] = 1;
	}
      num++;
    }
 
  return switcher;
}
	  
      
      
      
      
      


  
  
  
