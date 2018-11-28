#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include "assert.h"

using namespace std;

#define CHECK_LIMIT_SMALL(x) assert(1 <= (x) && (x) <= 3)
#define CHECK_LIMIT_LARGE(x) assert(1 <= (x) && (x) <= 100)

bool compare_int_desc(int i, int j)
{
    return i > j;
}

bool validate_threshold(int remainder, int min_allowed_element)
{
    float mean = remainder / (float) 2;

    return mean >= min_allowed_element;
}

int find_max_googlers(const vector<int>& googlers, int& remaining_surprises, int threshold)
{
    typedef vector<int>::const_iterator CI;

    int max_googlers = 0;

    for(CI iter = googlers.begin(); iter != googlers.end(); ++iter){
        int curr_max_remainder = *iter - threshold;
        if(curr_max_remainder < 0){
            break;
        }

        if(validate_threshold(curr_max_remainder, threshold - 1)){
            max_googlers++;
        }
        else if(remaining_surprises > 0){
            if(validate_threshold(curr_max_remainder, threshold - 2)){
                max_googlers++;
                remaining_surprises--;
            }
            else{
                break;
            }
        }
    }

    return max_googlers;
}

int main()
{
    ifstream input("file.in");
    ofstream output("file.out");

    string first_line;
    getline(input, first_line);
    istringstream string_input(first_line);
    int T;
    string_input >> T;
    assert(1 <= T && T <= 100);

    for(int currentCase = 1; currentCase <= T; currentCase++){
        string current_line = "";
        getline(input, current_line);
        istringstream current_string_input(current_line);

        int N;
        current_string_input >> N;
        CHECK_LIMIT_LARGE(N);
        int S;
        current_string_input >> S;
        assert(0 <= S && S <= N);
        int p;
        current_string_input >> p;
        assert(0 <= p && p <= 10);

        vector<int> googlers;

        for(int i=0; i<N; i++){
            int t;
            current_string_input >> t;
            assert(0 <= t && t <= 30);
            googlers.push_back(t);
        }

        sort(googlers.begin(), googlers.end(), compare_int_desc);

        output << "Case #" << currentCase << ": " << find_max_googlers(googlers, S, p) << endl;
    }

    return 0;
}
