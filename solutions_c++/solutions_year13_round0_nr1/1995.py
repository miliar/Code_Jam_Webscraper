#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int i = 1; i<=T; ++i) {
	  vector<string> P(4,"");
	  for (int j = 0; j<4; ++j) {
		  cin>>P[j];
	  }
	  bool flag = false;
	 
	  for (int x = 0;x<4;++x){
		  map<char, int> counter;
		  for (int y = 0; y<4; ++y) {
			  counter[P[x][y]]++;
		  }
		  counter['X'] += counter['T'];
		  counter['O'] += counter['T'];
		  if (4 == counter['X']) {
			  cout<< "Case #"<<i<<": X won" <<endl;
			  flag = true;
			  break;
		  }
		  if (4 == counter['O']){
			  cout<< "Case #"<<i<<": O won" <<endl;
			  flag = true;
			  break;
		  }
		  
	  }
	  if (true == flag)
		  continue;

	  for (int y = 0; y<4; ++y){
		  map<char, int> counter;
		  for (int x = 0;x<4;++x) {
			  counter[P[x][y]]++;
		  }
		  counter['X'] += counter['T'];
		  counter['O'] += counter['T'];
		  if (4 == counter['X']) {
			  cout<< "Case #"<<i<<": X won" <<endl;
			  flag = true;
			  break;
		  }
		  if (4 == counter['O']){
			  cout<< "Case #"<<i<<": O won" <<endl;
			  flag = true;
			  break;
		  }	  
	  }
	  if (true == flag)
		  continue;


	  
	  map<char, int> counter1;
	  map<char, int> counter2;
	  for (int x = 0; x<4; ++x) {
		  counter1[P[x][x]]++;
		  counter2[P[x][3-x]]++;
	  }
	  counter1['X'] += counter1['T'];
	  counter1['O'] += counter1['T'];
	  counter2['X'] += counter2['T'];
	  counter2['O'] += counter2['T'];

	  if (4 == counter1['X']) {
		  cout<< "Case #"<<i<<": X won" <<endl;
		  flag = true;
		  continue;
	  }
	  if (4 == counter1['O']){
		  cout<< "Case #"<<i<<": O won" <<endl;
		  flag = true;
		  continue;
	  }

	  
	  if (4 == counter2['X']) {
		  cout<< "Case #"<<i<<": X won" <<endl;
		  flag = true;
		  continue;
	  }
	  if (4 == counter2['O']){
		  cout<< "Case #"<<i<<": O won" <<endl;
		  flag = true;
		  continue;
	  }

	  int countdot = 0;
	  for (int x = 0;x<4;++x)
		  for (int y = 0; y<4; ++y) 
			  if ('.' == P[x][y])
				  countdot++;
	  if ( 0 == countdot) {
		  cout << "Case #"<<i<<": Draw" <<endl;
	  } else {
		  cout << "Case #"<<i<<": Game has not completed" <<endl;
	  }
	}
	return 0;
}