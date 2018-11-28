#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
  unsigned int n;
  cin >> n;

  for (unsigned int i = 0; i < n; ++i) {
    unsigned int current_size, size;
    cin >> current_size >> size;

    unsigned int rest_size = size - current_size;
    vector<double> probabilities;

    for (unsigned int j = 0; j < current_size; ++j) {
      double probability;
      cin >> probability;
      probabilities.push_back(probability);
    }

    unsigned int num_combinations = 1 << probabilities.size();
    vector<double> probability_combinations;
    
    for (unsigned int j = 0; j < num_combinations; ++j) {
      double temp = 1.0;
      
      for (unsigned int k = 0; k < current_size; ++k) {
	if (j & (1 << k)) temp *= 1 - probabilities[current_size - k - 1];
        else temp *= probabilities[current_size - k - 1]; 
      }
      
      probability_combinations.push_back(temp);
    }

    vector<double> num_expected_keystrokes;

    // Keep typing
    double num_expected_keystrokes_keep_typing = probability_combinations.front() * (rest_size + 1);

    for (unsigned int j = 1; j < num_combinations; ++j)
      num_expected_keystrokes_keep_typing += probability_combinations[j] * (rest_size + 1 + size + 1);

    num_expected_keystrokes.push_back(num_expected_keystrokes_keep_typing);

    // Delete j characters
    for (unsigned int j = 1; j <= current_size; ++j) {
      int set_bit_index = -1;
      double temp = 0.0;

      for (unsigned int k = 0; k < num_combinations; ++k) {
	for (int l = current_size - 1; l >= 0; --l) {
	  if (k & (1 << l)) {
	    set_bit_index = current_size - 1 - l;
	    break;
	  }
	}

	if (set_bit_index == -1 || set_bit_index >= current_size - j) temp += probability_combinations[k] * (rest_size + 2 * j + 1);
	else if (set_bit_index < current_size - j) temp += probability_combinations[k] * (rest_size + 2 * j + 1 + size + 1);
      }
      
      num_expected_keystrokes.push_back(temp);
    }
    
    // Press enter right away
    double num_expected_keystrokes_enter_right_away = 0.0;

    for (unsigned int j = 0; j < num_combinations; ++j)
      num_expected_keystrokes_enter_right_away += probability_combinations[j];

    num_expected_keystrokes_enter_right_away *= size + 2;
  
    num_expected_keystrokes.push_back(num_expected_keystrokes_enter_right_away);

    sort(num_expected_keystrokes.begin(), num_expected_keystrokes.end());

    cout.precision(6);
    cout << "Case #" << i + 1 << ": " << fixed << num_expected_keystrokes.front() << endl;
  }

  return 0;
}
