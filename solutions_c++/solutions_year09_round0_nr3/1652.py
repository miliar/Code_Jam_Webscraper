#include <iostream>
using namespace std;

const int N = 32;
const char* magic = "welcome to code jam";

int main() {

  char buffer[1024];

  int n;
  cin >> n;
  cin.getline(buffer, 1024, '\n');

  for(int caseNum = 0; caseNum < n; ++caseNum) {
    cin.getline(buffer, 1024, '\n');


    int ways[N];
    int ways2[N];
    for(int j = 0; j < N; ++j) {
      ways[j] = 0;
    }
    ways[0] = 1;

    for(int i = 0; buffer[i] != '\0'; ++i) {

      for(int j = 0; j < N; ++j) {
	ways2[j] = ways[j];
      }
      for(int j = 0; magic[j] != '\0'; ++j) {
	if(buffer[i] == magic[j]) {
	  ways2[j+1] = (ways2[j+1] + ways[j]) % 1000;
	}
      }

      for(int j = 0; j < N; ++j){
	ways[j] = ways2[j];
      }
    }

    cout << "Case #" << (caseNum+1) << ": " << ((ways[19]/1000)%10) << ((ways[19]/100)%10) << ((ways[19]/10)%10) << (ways[19]%10) << endl;
  }


  return(0);
}
