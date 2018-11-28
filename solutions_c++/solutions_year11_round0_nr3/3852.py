#define FILENAME "C-small-attempt2"
/* -------------------------------------------------------------------------- */
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <vector>

#define INPUT_EXT ".in"
#define OUTPUT_EXT ".out"
#define MAX_T 100
#define MAX_C 1000000
#define MAX_N 1000

using namespace std;

vector<int> sean, patric;
int sean_max = -1;
int comp = 0;
bool compare(vector<int> *first, vector<int> *second, int pivot) {
//    cout << comp++ << endl;
//    cout << "first: ";
//    for (unsigned i=0; i<first->size(); i++) {
//        cout << first->at(i) << " ";
//    }
//    cout << endl;
//
//    cout << "second: ";
//    for (unsigned i=0; i<second->size(); i++) {
//        cout << second->at(i) << " ";
//    }
//    cout << endl;

    bool found = false;

    int first_crazy_sum = 0, second_crazy_sum=0;
    for (unsigned i=0; i<first->size(); i++) {
        first_crazy_sum ^= first->at(i);
    }
    for (unsigned i=0; i<second->size(); i++) {
        second_crazy_sum ^= second->at(i);
    }

    if (first_crazy_sum == second_crazy_sum && second->size() > 0) {
        found = true;

        int sum_first = 0, sum_second = 0;
        int local_max = -1;
        for (unsigned i=0; i<first->size(); i++) {
            sum_first += first->at(i);
        }
        for (unsigned i=0; i<second->size(); i++) {
            sum_second += second->at(i);
        }
        local_max = sum_first > sum_second ? sum_first : sum_second;
        if (local_max > sean_max) {
            sean_max = local_max;
            sean = vector<int>(*first);
            patric = vector<int>(*second);
//            cout << "max now is: " << local_max << endl;
        }
    }

    if (first->size() > 1) {
        for (unsigned i=pivot; i<first->size(); i++) {
            int moved = first->at(i);
            first->erase(first->begin()+i);
            second->push_back(moved);
            compare(first, second, i);
            first->insert(first->begin()+i, moved);
            second->erase(second->end()-1);
        }
    }

    return found;
}

int main(int argc, char** argv)
{
    fstream input(FILENAME INPUT_EXT);
    ofstream output(FILENAME OUTPUT_EXT, ios_base::out);

    int T = 0; // Test cases
    int N = 0; // Length of one case

    input >> T;
    for (int i=0; i<T; i++) {
        sean_max = 0;
        vector<int> start_first;
        vector<int> start_second;
        int candy;
        bool success = false;

        input >> N;
        for (int j=0; j<N; j++) {
            input >> candy;
            start_first.push_back(candy);
        }
        success = compare(&start_first, &start_second, 0);


        ostringstream res_out;
        res_out << "Case #" << i+1 << ": ";

        if (sean_max > 0) {
            res_out << sean_max;
//            cout << "Sean: ";
            for (int j=0; j<sean.size(); j++) {
//                cout << sean.at(j) << " ";
            }
//            cout << endl;

//            cout << "Patric: ";
            for (int j=0; j<patric.size(); j++) {
//                cout << patric.at(j) << " ";
            }
//            cout << endl;
        } else {
            res_out << "NO";
        }
        res_out << endl;

//        cout << res_out.str();
        output << res_out.str();
    }

    output.close();
    input.close();

    return 0;
}
