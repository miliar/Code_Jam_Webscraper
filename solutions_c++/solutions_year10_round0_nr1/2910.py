#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>

//Input : vector<pair <int, int>>
//Output : vector<bool>

#define INPUT "A-large.in"
#define OUTPUT "A-large.out"

using namespace std;

void readInput(const char * filename, vector<pair<int, int> > & tab);
void analyse(const vector<pair<int, int> > & input, vector<bool> & output);
void writeOutput(const char * filename, const vector<bool> & tab);
bool isOn(int n, int k);
int exp2(int n);

int main()
{
    vector<pair<int, int> > input;
    vector<bool> output;
    try
    {
        readInput(INPUT, input);

        analyse(input, output);

        writeOutput(OUTPUT, output);
    }
    catch(const string & s)
    {
        cout << "Fatal Error : " << s << endl;
    }
    return 0;
}

void readInput(const char * filename, vector<pair<int, int> > & tab)
{
    tab.clear();
    FILE * file = fopen(filename, "r");
    if(file == NULL)
        throw string("Can't open the input file : " + string(filename));
    int line;
    fscanf(file, "%d\n", &line); //Take the number of line in the input file;
    int n, k;

    for(int i = 0 ; i < line ; ++i)
    {
        fscanf(file, "%d %d\n", &n, &k);
        tab.push_back(pair<int, int>(n, k));
    }

    fclose(file);
}

void analyse(const vector<pair<int, int> > & input, vector<bool> & output)
{
    output.clear();
    int inputSize = input.size();
    pair<int, int> current;
    for(int i = 0 ; i < inputSize ; ++i)
    {
        current = input[i];
        if(current.second == 0)
        {
            output.push_back(false);
        }
        else
        {
            if(isOn(current.first, current.second))
            {
                output.push_back(true);
            }
            else
            {
                output.push_back(false);
            }
        }
    }
}

void writeOutput(const char * filename, const vector<bool> & tab)
{
    FILE * fichier = fopen(filename, "w+");
    if(fichier == NULL)
        throw string("Can't open output file : " + string(filename));
    int outputSize = tab.size();

    for(int i = 0 ; i < outputSize ; ++i)
    {
        fprintf(fichier, "Case #%d: %s\n", i+1, ((tab[i] == true) ? "ON" : "OFF"));
    }

    fclose(fichier);
}

bool isOn(int n, int k)
{
    int e = exp2(n);
    if((e & k) == e)
        return true;
    return false;
}

int exp2(int n)
{
    int ret = 1;
    ret <<= n;
    return ret-1;
}
