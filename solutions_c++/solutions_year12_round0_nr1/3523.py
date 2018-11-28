#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {

// char mapping[] = "ynficwlbkuomxsevzpdrjgthaq ";
char mapping[] = "yhesocvxduiglbkrztnwjpfmaq ";
/* char* mapping[27] = {
'y', // a
'n', // b
'f', //c
'i', //d
'c', //e
'w', //f
'l', //g
'b', //h
'k', //i
'u', //j
'o', //k
'm', //l
'x', //m
's', //n
'e', //o
'v', //p
'z', //q
'p', //r
'd', //s
'r', //t
'j', //u
'g', //v
't', //w
'h', //x
'a', //y
'q', //z
' ' //space
};*/

ifstream data;
//data.open("input.txt");
data.open("A-small-attempt0.in");

int junk = 0;
int num_test_cases = 0;

data >> num_test_cases;

int test_cases_processed = 0;
string inputarray;
char* teststring;

// cout << num_test_cases << "\n";
int len = 0;
int i = 0;
char* outputarray;
int index;
while(test_cases_processed <= num_test_cases) {
    if (test_cases_processed == 0) { getline(data, inputarray); test_cases_processed++; continue; }

    getline(data,inputarray); // Saves the line in STRING.
len = inputarray.length();
    // cout<< " dumping " << inputarray << " length = " << len << "\n"; // Prints our STRING.
cout << "Case #" << test_cases_processed << ": ";

for (i = 0; i < len; i++) {
// cout << " ascii value of " << inputarray.at(i) << " is " << inputarray.at(i) - 0 << "\n";
index = inputarray.at(i) - 97;
    if (inputarray.at(i) != ' ') cout << mapping[index];
    else cout << ' ';
}

cout << "\n";
    //data >> inputarray;
    test_cases_processed ++;

    // cout << "string " << inputarray << "\n";
}

data.close();

}
