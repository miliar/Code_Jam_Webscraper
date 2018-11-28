#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

int main(){
  int N, S, Q, test = 1, switchs, so_far;
  string name, endline;
  map<string, int> names;

  cin >> N;

  while(N--){
    cin >> S;
    getline(cin, endline);

    vector<bool> seen(S, false);

    while(S--){
      getline(cin, name);
      names[name] = S;
    }

    so_far = switchs = 0;

    cin >> Q;
    getline(cin, endline);

    while(Q--){
      getline(cin, name);

      so_far += (seen[names[name]] == (switchs & 1));

      seen[names[name]] = !(switchs & 1);

      if(so_far == names.size()){

	so_far = 1;
	switchs++;
	seen[names[name]] = !(switchs & 1);
      }
    }
 
    cout << "Case #" << test++ << ": " << switchs << endl;

    names.clear();
  }
}

/*
long long saving_the_universe(long long n,
			      long long from,
			      long long engine,
			      vector<long long> queries);

int main(){
  long long N, S, Q, test = 1, label, min, actual, n;
  string name;
  map<string, long long> names;
  vector<long long> sequence;

  cin >> N;

  while(N--){
    cin >> S;

    getline(cin, name);

    label = 0;

    while(S--){
      getline(cin, name);
      names[name] = label++;
    }
    
    cin >> Q;
    getline(cin, name);

    min = 0;

    if(Q){
      while(Q--){
	getline(cin, name);
	sequence.push_back(names[name]);
      }
      
      n = names.size();
      min = sequence.size();
      
      for(long long i = 0 ; i < n ; i++){
	if(i != sequence[0]){
	  actual = saving_the_universe(n, 0, i, sequence);
	  
	  if(actual < min)
	    min = actual;
	}
      }
    }
    else
      min = 0;
    
    cout << "Case #" << test++ << ": " << min << endl;
    
    names.clear();
    sequence.clear();
  }
}

long long saving_the_universe(long long n,
			      long long from,
			      long long engine,
			      vector<long long> queries){

  long long min = queries.size(), actual, j;

  if(from == queries.size())
    return 0;

  for(long long i = 0 ; i < n ; i++){
    if(i != queries[from - 1]){
      
      j = from + 1;
      while(j < queries.size() && queries[j] != engine)
	j++;

      if(j == queries.size())
	return 0;

      actual = 1 + saving_the_universe(n, j, i, queries);

      if(actual < min)
	min = actual;
    } 
  }

  return min;
}
*/
