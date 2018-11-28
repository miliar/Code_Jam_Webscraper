#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <cstdio>
#include <cstdlib>

//Input : vector<Input>
//Output : vector<int>

#define INPUT "C-small-attempt0.in"
#define OUTPUT "C-small-attempt0.out"

using namespace std;

class Input
{
    public :
        int numberOfRide;
        int numberOfPlace;
        list<int> group;
};

void readInput(const char * filename, vector<Input> & tab);
void analyse(vector<Input> & input, vector<int> & output);
void writeOutput(const char * filename, const vector<int> & output);

int main(void)
{
    vector<Input> input;
    vector<int> output;
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


    return EXIT_SUCCESS;
}

void readInput(const char * filename, vector<Input> & tab)
{
    FILE * file = fopen(filename, "r");
    if(file == NULL)
        throw string("Can't open input file : " + string(filename));

    tab.clear();
    int line;
    int nGroup;
    int currentg;

    fscanf(file, "%d\n", &line);

    for(int i = 0 ; i < line ; ++i)
    {
        tab.push_back(Input());

        fscanf(file, "%d %d %d\n", &(tab[i].numberOfRide), &(tab[i].numberOfPlace), &nGroup);
        nGroup--;
        for(int j = 0 ; j < nGroup ; ++j)
        {
            fscanf(file, "%d ", &currentg);
            tab[i].group.push_back(currentg);
        }
        fscanf(file, "%d\n", &currentg);
        tab[i].group.push_back(currentg);
    }

    fclose(file);
}

void analyse(vector<Input> & input, vector<int> & output)
{
    int inputSize = input.size();
    int nRide;
    int room;
    int currentRoom;
    int current;
    int money;
    int lsize;
    list<int> copy;

    for(int i = 0 ; i < inputSize ; ++i)
    {
        money = 0;
        nRide = input[i].numberOfRide;
        room = input[i].numberOfPlace;
        for(int j = 0 ; j < nRide ; ++j)
        {
            currentRoom = room;
            copy = input[i].group;
            lsize = copy.size();
            for(int k =  0 ; currentRoom >= copy.front() and k < lsize ; ++k)
            {
                money += copy.front();
                currentRoom -= copy.front();
                current = copy.front();
                input[i].group.push_back(current);
                copy.pop_front();
                input[i].group.pop_front();
            }
        }
        output.push_back(money);
    }
}


void writeOutput(const char * filename, const vector<int> & output)
{
    FILE * fichier = fopen(filename, "w+");
    if(fichier == NULL)
        throw string("Can't open output file : " + string(filename));

    int size = output.size();

    for(int i = 0 ; i < size ; ++i)
    {
        fprintf(fichier, "Case #%d: %d\n", i+1, output[i]);
    }

    fclose(fichier);

}






