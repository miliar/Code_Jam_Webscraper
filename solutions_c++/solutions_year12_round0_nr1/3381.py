#include <iostream>
#include <cmath>

#define SIZE 128

using namespace std;

int main() {
  int t;
  char str[SIZE];
  char translate[26] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

  cin >> t;
  cin.getline(str, SIZE);
  
  for(int i = 0; i < t; i++){
    cout << "Case #" << (i+1) << ": ";
    cin.getline(str, SIZE);
    for(int j = 0; str[j] != '\0'; j++) {
      if (str[j] >= 'a' && str[j] <= 'z') {
	str[j] = translate[str[j] - 'a'];
      }
    }
    cout << str << endl;
  }

  return 0;
}
