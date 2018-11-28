#include <vector>
#include <iostream>

#include <stdio.h>

using namespace std;

double solve(const vector<int>&);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    vector<int> numbers;
    int num_numbers;
    cin >> num_numbers;
    for(int j = 0; j < num_numbers; j++){
      int n;
      cin >> n;
      numbers.push_back(n);
    }
    double r = solve(numbers);
    cout.setf(ios::fixed, ios::floatfield);
    cout << "Case #" << i+1 << ": " << r << endl;;
  }
}

double solve(const vector<int>& numbers){
  int num_freeze = 0;
  for(size_t i = 0; i < numbers.size(); i++){
    if(numbers[i] == static_cast<int>(i+1)) num_freeze++;
  }
  return static_cast<double>(numbers.size() - num_freeze);
}
