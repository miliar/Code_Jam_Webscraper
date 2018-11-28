#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int tc=1;tc<=T;++tc){
    int N;
    cin >> N;
    vector<int> orange;
    vector<int> blue;
    vector<char> S;
    for(int i = 0; i < N; ++i){
      char c; int dest;
      cin >> c >> dest;
      S.push_back(c);
      if( c == 'O' ){
	orange.push_back( dest );
      }else{
	blue.push_back( dest );
      }
    }

    int time = 1;
    int opos = 1;
    int op = 0;
    int bpos = 1;
    int bp = 0;
    int seq = 0;
    while( op < orange.size() || bp < blue.size() ){
      bool pushed = false;
      //cout << time << ' ' << op << ' ' << opos << ' ' << bp << ' ' << bpos << ' ' << seq << endl;

      if( op < orange.size() ){
	if( opos < orange[op] ){
	  ++opos;
	}else if( opos > orange[op] ){
	  --opos;
	}else{
	  if( S[seq] == 'O' ){
	    ++op;
	    pushed = true;
	  }
	}
      }

      if( bp < blue.size() ){
	if( bpos < blue[bp] ){
	  ++bpos;
	}else if( bpos > blue[bp] ){
	  --bpos;
	}else{
	  if( S[seq] == 'B' ){
	    ++bp;
	    pushed = true;
	  }
	}
      }

      if( pushed ) ++seq;
      ++time;
    }

    --time;
    cout << "Case #" << tc << ": " << time << endl;

  }
  return 0;
}
