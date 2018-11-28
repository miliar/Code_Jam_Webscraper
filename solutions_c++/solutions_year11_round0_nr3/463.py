#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solve(const vector<int>&);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    vector<int> candies;
    int num_candies;
    cin >> num_candies;
    for(int j = 0; j < num_candies; j++){
      int c;
      cin >> c;
      candies.push_back(c);
    }
    int r = solve(candies);
    if(r == -1) 
      cout << "Case #" << i+1 << ": NO"<< endl;
    else 
      cout << "Case #" << i+1 << ": " << r << endl;
  }
}

int solve(const vector<int>& candies){
  int pat_sum = 0;
  int sum = 0;
  for(size_t i = 0; i < candies.size(); i++){
    pat_sum ^= candies[i];
    sum += candies[i];
  }
  if(pat_sum != 0) return -1;
  int min = *min_element(candies.begin(),candies.end());
  return sum - min;
}
