#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int calculate_recylcednums(int a, int b) {
    int recyclednums = 0;

    int numdigits_of_a = 0;

    int start = a;
    int end = b;

    int temp_a = 0;
    int mask = 0;
    int highestdigit = 0;
    int lowerdigits = 0;
    int newnum = 0;
    int i = 0;
    int newnum_array[8] = {b+1,b+1,b+1,b+1,b+1,b+1,b+1,b+1};
    // loop over each number from a to b
    for (start = a; start <= end; start++) { 
        temp_a = start;
        mask = 1;
        for (i = 0; i < 8; i++) newnum_array[i] = b+1;

        i = 0;

        numdigits_of_a = 0;
        while(temp_a > 0) {
            numdigits_of_a++;
            temp_a /= 10;
            mask = mask*10;
        }

        mask = mask/10;
        // cout  << " for start = " << start << " num digits = " << numdigits_of_a << " mask = " << mask << "\n";

        highestdigit = 0;
        lowerdigits = 0;
        newnum = start;
        if (numdigits_of_a >= 1) {
            while (numdigits_of_a) {
                // cout << " debug mask = " << mask << " numdigits_of_a = " << numdigits_of_a << "\n";
                highestdigit = newnum / mask;
                lowerdigits = newnum % mask;
                newnum = lowerdigits*10 + highestdigit;

                // cout << " highestdigit = " << highestdigit << " lowerdigits " << lowerdigits << " newnum " << newnum << "\n";
                if ((newnum != start) && (newnum <= b) && (newnum >= start)) {
                    if ((newnum_array[0] != newnum) && (newnum_array[1] != newnum) && (newnum_array[2] != newnum) && (newnum_array[3] != newnum) && (newnum_array[4] != newnum) && (newnum_array[5] != newnum) && (newnum_array[6] != newnum) && (newnum_array[7] != newnum)) {
                    // cout << " newnum_array " << newnum_array[0] << " "  << newnum_array[1] << " "  << newnum_array[2] << " "  << newnum_array[3] << " "  << newnum_array[4] << " "  << newnum_array[5] << " "  << newnum_array[6] << " "  << newnum_array[7] << " \n";
                        // cout << " **** found recycled nums = " << start << " and " << newnum << "\n";
                        recyclednums++;
                        newnum_array[i] = newnum;
                        i++;
                    }
                }
                numdigits_of_a--;
                // mask = mask/10;
            }
        }
    }
    return recyclednums;
}
 
int main() {

ifstream data;
data.open("C-large.in");

ofstream output;
output.open("output.txt");

int junk = 0;
int num_test_cases = 0;

data >> num_test_cases;

int test_cases_processed = 0;
string inputarray;
char* teststring;

cout << num_test_cases << "\n";
int a, b, recyclednums;
while(test_cases_processed < num_test_cases) {
 
    data >> a >> b;
    // cout << " tuple a = " << a << " b = " << b << "\n"; 
recyclednums = calculate_recylcednums(a, b);
     //data >> inputarray;
//     cout << "Case #" << test_cases_processed + 1 << ": " << recyclednums << "\n";
    output << "Case #" << test_cases_processed + 1<< ": " << recyclednums << "\n";

    test_cases_processed ++;

    // cout << "string " << inputarray << "\n";
}

data.close();
output.close();
}
