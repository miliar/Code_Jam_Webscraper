#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int search (string S[], string s1, int start, int n) 
{
  for (int i = start; i < n; i++)
  {
    if ( S[i] == s1)
    {
      return i ;
    }
  }
  return n;
}

int main()
{
  ifstream infile;
  string names;
  int questions;
  infile.open ("Input2.in");
  getline( infile,names);
  questions = atoi(names.c_str());

  int current_question = 1;
  int S;
  int Q;
  while (questions >= current_question)
  {
    getline( infile, names);
    int count = 0;
    S = atoi(names.c_str());

    string search_engine[S];
    while ( S > count)
    {
      getline( infile, names);
    
      search_engine[count] = names;
      count ++;
    }
    count = 0;
    getline( infile, names);
    Q = atoi(names.c_str());
   
    string queries[Q];
    while ( Q > count)
    {
      getline( infile, names);
 
      queries[count] = names;
      count++;
    }
    int turn = 0;
    int index = 0;
    
    int move;
    int start = 0;
    while ( index < Q)
    {
      int top = 0 ;
       for ( int i = 0; i < S ; i++)
      {
        
         move = search ( queries, search_engine[i], start, Q);
      
        if (move > top)
        {
          top = move;
        }
       }
       if (top < Q)
        {
          turn ++;
        }
       index = top;
       start = top;
            
    }
    cout << "Case #"<<current_question<<": "<<turn<<endl;
    current_question++;
    
  }
}
      