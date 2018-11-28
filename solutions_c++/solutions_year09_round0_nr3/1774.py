// Usage: rename input file -> input.txt
// output file with the solution is output.txt
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#define MAX_T 100
#define NUM 19 //19

using namespace std;

const char wtcj[] = "welcome to code jam"; // 19

int search(const char * s, int first, int last, int cursor)
{
    int i ;
    int sum = 0;

    i = first;
    bool go = true;
    for (i=first; i<last;i++)
    {
        if (wtcj[cursor] == s[i])
        {
            if (cursor + 1 == NUM)
            {
                sum = sum+1;
            }
            else if (i+1 != last  && last-i >= NUM-cursor)
            {
                sum = sum + search(s,i+1,last,cursor+1);
                sum= sum%10000;
            }
        }
    }

    return sum;
}

int main()
{
    int i, r;
    int N;
    string line;
    char ch;

    ifstream infile("input.txt");
    ofstream outfile("output.txt");

    if (!infile)
    {
        cout << "There was a problem opening the file for reading."
             << endl;
        return 0;
    }

    getline (infile,line);
    stringstream ss(line);
    ss >> N;

    for (i=0;i<N;i++)
    {
        outfile << "Case #"<< i+1 <<": ";
        getline (infile,line);
        r = search (line.c_str(),0,line.length(),0);
        if (r < 10)
            outfile << "0";
        if (r < 100)
            outfile << "0";
        if (r < 1000)
            outfile << "0";
        outfile << r <<endl;
    }

    infile.close();
    outfile.close();

    return 0;
}
