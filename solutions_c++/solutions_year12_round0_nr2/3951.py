#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    int num_lines;
    cin >> num_lines;
    int num_googlers;
    int surprising;
    int score_at_least;
    for(int i=1; i<=num_lines; ++i) {
        cin >> num_googlers;
        cin >> surprising;
        cin >> score_at_least;
        int rounded_score = 3*score_at_least;
        int case_count = 0;
        cout << "Case #" << i << ": ";
        for(int j = 0; j<num_googlers; ++j) {
            int temp_input;
            cin >> temp_input;
            if(temp_input >= rounded_score) {
                ++case_count;
            } else if(temp_input >= rounded_score-2 && temp_input >= score_at_least ) {
                ++case_count;
            } else if(temp_input >= rounded_score-4 && temp_input >= score_at_least && surprising > 0) {
                ++case_count;
                --surprising;
            }
        }
        cout << case_count << endl;
    }
}
