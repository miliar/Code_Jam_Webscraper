#include <iostream>
#include <fstream>
using namespace std;

int main( void ){
  int num_cases = 0;
  cin >> num_cases;
  for(int current_case = 0; current_case < num_cases; current_case++){
    int num_dancers = 0, num_specials = 0, score_thresh = 0;
    int dancer_score;
    int min_thresh_special = 0, max_thresh_special = 0;
    int num_dancers_good = 0;

    cin >> num_dancers >> num_specials >> score_thresh;

    min_thresh_special = score_thresh*3 - 4;
    max_thresh_special = score_thresh*3 - 3;
    if(score_thresh == 1){
      num_specials = 0;
    }

    for(int current_dancer = 0; current_dancer < num_dancers; current_dancer++){
      cin >> dancer_score;
      if(dancer_score > max_thresh_special)
        num_dancers_good++;
      else if(dancer_score >= min_thresh_special && num_specials > 0){
        num_specials--;
        num_dancers_good++;
      }
    }
    cout << "Case #" << (current_case+1) << ": " << num_dancers_good << endl;
  }
}
