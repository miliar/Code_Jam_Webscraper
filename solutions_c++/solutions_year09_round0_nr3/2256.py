#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


void RunTestCase(int index, const string &input)
{
    const string pattern("welcome to code jam");
    vector<vector<unsigned int> > table(
                pattern.size() + 1, vector<unsigned int>(input.size() + 1, 0));

    //cout << pattern << endl;
    //cout << input << endl;

    //cout << table.size() << endl;
    //cout << table[0].size() << endl;

    vector<unsigned int> &lastRow = table[table.size() - 1];

    for (int i=0; i<lastRow.size(); ++i)
    {
        lastRow[i] = 1;
    }

    for (int i=input.size()-1; i>=0; --i)
    {
        for (int j=pattern.size()-1; j>=0; --j)
        {
            const int col = i;
            const int row = j;

            if (pattern[j] == input[i])
            {
                table[row][col] = (table[row][col+1] % 10000) +
                                  (table[row+1][col+1] % 10000);
            }
            else
            {
                table[row][col] = table[row][col+1];
            }
        }
    }

    //for (int i=0; i<table.size(); ++i)
    //{
        //for (int j=0; j<table[i].size(); ++j)
        //{
            //cout << table[i][j] << " ";
        //}
//
        //cout << endl;
    //}

    cout << "Case #" << (index + 1) << ": "
         << setw(4) << setfill('0') << (table[0][0] % 10000) << endl;
}


int main()
{
    int N;

    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i=0; i<N; ++i)
    {
        string input;
        getline(cin, input);

        RunTestCase(i, input);
    }
}
