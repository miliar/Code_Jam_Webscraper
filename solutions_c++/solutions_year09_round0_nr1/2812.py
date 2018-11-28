#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

#define OUTPUT_DEFAULT  "./output.txt"

using namespace std;

int Length;
int Dict;
int N;

vector<string> dictionary;
vector<string> trial_input;
vector<int>    trial_output;

string input_file;
string output_file;

int CalculatePossibilities(string test_case);

int main(int argc, char** argv)
{
    stringstream output;

    if(argc > 1)
        input_file = argv[1];
    else
    {
        cout << "No file specified. Closing." << endl;
        return -1;
    }

    ifstream infile;
    infile.open(input_file.c_str());
    if(!infile.is_open())
    {
        cout << "COULD NOT OPEN FILE! Closing..." << endl;
        return -1;
    }

    //Collect input data into objects...

    infile >> Length;
    infile >> Dict;
    infile >> N;

    cout << "Length of words: " << Length << endl;
    cout << "Dictionary size: " << Dict << endl;
    cout << "Number of trials: " << N << endl;

    dictionary.resize(Dict);
    for(int i = 0; i < Dict; i++)
    {
        infile >> dictionary.at(i);
    }

    trial_input.resize(N);
    for(int i = 0; i < N; i++)
    {
        infile >> trial_input.at(i);
    }
    infile.close();


    // Now go through each input and determine output...

    trial_output.resize(N);
    for(int i = 0; i < N; i++)
    {
        cout << "Trial " << i+1 << endl;
        trial_output.at(i) = CalculatePossibilities(trial_input.at(i));
    }

    for(int i = 0; i < trial_output.size(); i++)
    {
        if(i)
            output << endl;
        output << "Case #" << i+1 << ": " << trial_output.at(i);
    }

    ofstream file_out;
    file_out.open(OUTPUT_DEFAULT);
    if(!file_out.is_open())
        cout << "COULD NOT OPEN OUTPUT FILE" << endl;
    else
    {
        file_out << output.str();
        file_out.close();
    }

    cout << output.str();

}

int CalculatePossibilities(string test_case)
{
    int possible = 0;
    int votes = 0;
    vector<string> separated;


        // This is used for determining how many sections/letters of the word there are.
        // That info is already given so we're taking this code piece out.

    int current_section = 0;
    bool within_p = 0;

    separated.resize(Length);

    for(int i = 0; i < test_case.length(); i++)
    {
        if(test_case[i] == '(')
        {
            within_p = 1;
            continue;
        }
        if(test_case[i] == ')')
        {
            within_p = 0;
            current_section++;
            continue;
        }

        separated.at(current_section) += test_case[i];
        if(!within_p)
            current_section++;
    }

    for(int i = 0; i < dictionary.size(); i++)
    {
        votes = 0;
        for(int j = 0; j < separated.size(); j++)
        {
            for(int n = 0; n < separated.at(j).length(); n++)
            {
                if(separated.at(j)[n] == dictionary.at(i)[j])
                {
                    votes++;
                    break;
                }
            }
        }
        if(votes == Length)
            possible++;
    }

    return possible;

}
