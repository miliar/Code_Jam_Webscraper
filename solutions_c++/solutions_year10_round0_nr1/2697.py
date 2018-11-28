#include <cstring>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
    unsigned int T, N, K;
	string temp = "";
	cin >> T;
	cin.get();

    for (int i=0; i<T; ++i)
    {
	  getline(cin, temp);
	  stringstream ss(temp);

	  ss >> N;
	  ss >> K;

	  unsigned int total = pow(2.0, N);
	  unsigned int left = K % total;

	  printf("Case #%d: ", i+1);
	  if (left == total-1)
		cout << "ON" << endl;
	  else
		cout << "OFF" << endl;
    }   
    return 0;
}
