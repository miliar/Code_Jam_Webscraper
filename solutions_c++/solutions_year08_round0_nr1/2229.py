#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
  int N;
  int S;
  int Q;
  int sw;

  int i,j,k;
  string se;
  set<string> not_used;

  cin >> N;

  for( i = 0; i < N; ++i ) {

    //    cout <<"S:";
    cin >> S;
    getline (cin,se);

    // read search engine list
    for( j = 0; j < S; ++j ) {

      getline (cin,se);
      
    }
    
    // nr of queries
    //    cout <<"Q:";
    cin >> Q;
    getline (cin,se);

    not_used.clear();
    sw = 0;
     // read queries
    for( j=0; j<Q; ++j ) {

      getline (cin,se);
      not_used.insert(se);
      
      if( not_used.size() == S ) {
	
	++sw;
	not_used.clear();
	not_used.insert(se);
	
      }

    }
    
    cout <<"Case #"<<i+1<<": "<<sw<<endl;
    
  }

  return 0;
}
