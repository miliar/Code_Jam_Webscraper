#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include "assert.h"

using namespace std;

#define CHECK_LIMIT_SMALL(x) assert(1 <= (x) && (x) <= 1000)
#define CHECK_LIMIT_LARGE(x) assert(1 <= (x) && (x) <= 2000000)

//vector<string> recnums;

int recycled_num_count(int num, int max)
{
    int num_count = 0;

    if(num >= 10){
        ostringstream string_output;
        string_output << num;
        string num_as_string = string_output.str();

        for(unsigned int curr_pos = 0; curr_pos < num_as_string.length(); curr_pos++){
            string::iterator iter = num_as_string.begin();
            char c = *iter;
            num_as_string.erase(iter);
            num_as_string.push_back(c);

            int recycled_num = atoi(num_as_string.c_str());
            if(num < recycled_num && recycled_num <= max){
                //recnums.push_back(string_output.str() + "," + num_as_string);
                num_count++;
            }
        }
    }

    return num_count;
}

int recycled_num_count_in_range(int min, int max)
{
    int range_num_count = 0;

    int curr_num = min;

    while(curr_num <= max){
        range_num_count += recycled_num_count(curr_num, max);
        curr_num++;
    }

    return range_num_count;
}

void print_vector(ostream& out, const vector<int>& v)
{
    typedef vector<int>::const_iterator CI;

    for(CI iter = v.begin(); iter != v.end(); ++iter){
        out << *iter << endl;
    }
}

void print_vector(ostream& out, const vector<string>& v)
{
    typedef vector<string>::const_iterator CI;

    for(CI iter = v.begin(); iter != v.end(); ++iter){
        out << *iter << endl;
    }
}

int main()
{
    fstream input("file.in");
    ofstream output("file.out");

    string first_line;
    getline(input, first_line);
    istringstream string_input(first_line);
    int T;
    string_input >> T;
    assert(1 <= T && T <= 50);

    for(int currentCase = 1; currentCase <= T; currentCase++){
        string current_line = "";
        getline(input, current_line);
        istringstream current_string_input(current_line);

        int A;
        current_string_input >> A;
        CHECK_LIMIT_LARGE(A);
        int B;
        current_string_input >> B;
        CHECK_LIMIT_LARGE(B);
        assert(A <= B);

        output << "Case #" << currentCase << ": " << recycled_num_count_in_range(A, B) << endl;
        //sort(recnums.begin(), recnums.end());
        //print_vector(output, recnums);
    }

    return 0;
}
