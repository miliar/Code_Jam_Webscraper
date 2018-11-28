#include <iostream>
#include <string>
#include <sstream>
#include <list>
#include <vector> 
#include <algorithm> 
#include <map>
#include <set>
#include <cmath>

using namespace std;
#define PI 3.14159265358979323846264338327950288

#define CASE(x) "Case #" << x << ": " 

string linebuf; 
#define cinline getline(cin, linebuf);\
		stringstream(linebuf)

void process_case()
{
    int P, K, L, f;
    int ans = 0; 
    vector<int> freq; 
    cinline  >> P >> K >> L; 
    for (int i = 0; i < L; i++) {
	cin >> f;
	freq.push_back(f); 
    }
    cin.ignore(); 
    sort(freq.begin(),freq.end(), greater<int>());
    for (int j = 0; j < freq.size(); j++) {
	ans +=freq[j] * (j/K +1); 
    }
    cout << ans; 
}

int main(int argc, char* argv[])
{
    int cases; 
    cinline >> cases;  
    for (int i = 1; i <= cases; i++) {
	cout << CASE(i); 
	process_case();
	cout << endl; 
    }
}
