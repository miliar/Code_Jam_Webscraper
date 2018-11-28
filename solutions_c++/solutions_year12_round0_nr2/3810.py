#include <fstream>
#include <iostream>
#include <string>
#include <string.h>
#include <stdlib.h>

#define PROB_B

using namespace std;


int main ()
{

    ifstream inputFile;
    inputFile.open("input.txt");
    ofstream outputFile;
    outputFile.open("output.txt");

    if (!inputFile.is_open())
    {
        cout << "Couldn't open the input file. Hope the timer isn't running!" << endl;
        return -1;
    }
    else if (!outputFile.is_open())
    {
        cout << "This isn't even possible =(" << endl;
    }

    string input;

    getline(inputFile, input);

    int i, j, cases = atoi(input.c_str());
    const char delim[1] = {' '};

    int N, S, P;
    int *points;
    char *str;

    int num;

    for (i = 0; i < cases; i++) {

        int total = 0;

        getline(inputFile, input);
        char *temp = new char[sizeof(char) * input.length() + 1];
        strcpy (temp, input.c_str());

        str = strtok(temp, delim);
        N = atoi(str);
        str = strtok(NULL, delim);
        S = atoi(str);
        str = strtok(NULL, delim);
        P = atoi(str);

        points = new int[sizeof(int) * N];

        //Initialize everything
        for (j = 0; j < N; j++) {
            str = strtok(NULL, delim);
            if (str == NULL) {
                cout << "Disaster" << endl;
                return -1;
            }
            points[j] = atoi(str);
        }

        for (j = 0; j < N; j++) {
            if (points[j] >= P) {
                switch (points[j] % 3) {
                    case 0:
                        num = points[j]/3;
                        if (num >= P) {
                            total++;
                        } else if ((num + 1) >= P && S > 0) {
                            S--;
                            total++;
                        }
                        break;
                    case 1:
                        num = points[j]/3;
                        num++;
                        if (num >= P) {
                            total++;
                        }
                        break;
                    case 2:
                        num = points[j]/3;
                        num++;
                        if (num >= P) {
                            total++;
                        } else if ((num + 1) >= P && S > 0) {
                            S--;
                            total++;
                        }
                        break;
                    default:
                        cout << "Shenanigans" << endl;
                        return -1;
                }
            }
        }
        outputFile << "Case #" << (i + 1) << ": " << total << endl;
    }

    return 0;
}


















#ifdef PROB_A

int main()
{
    ifstream inputFile;
    inputFile.open("input.txt");
    ofstream outputFile;
    outputFile.open("output.txt");

    if (!inputFile.is_open())
    {
        cout << "Couldn't open the input file. Hope the timer isn't running!" << endl;
        return -1;
    }
    else if (!outputFile.is_open())
    {
        cout << "This isn't even possible =(" << endl;
    }

    //ascii - 97 indexed, ascii value of translation
    int matched[26] = {-1};
    int wasMapped[26] = {0};

    //Given
    matched[0] = (int)'y';
    matched[25] = (int)'q';
    matched[14] = (int)'e';
    wasMapped[24] = 1;
    wasMapped[16] = 1;
    wasMapped[4] = 1;

    ifstream auxInput;
    auxInput.open("example.txt");

    string input, aux;
    int i, j, cases;

    //Populate the rest, hopefully
    for (i = 0; i < 3; i++)
    {
        getline(auxInput, input);
        getline(auxInput, aux);
        if (input.length() != aux.length())
        {
            cout << "Clearly I misunderstood the instructions" << endl;
            return -1;
        }
        for (j = 0; j < input.length(); j++)
        {
            if (input[j] != ' ')
            {
                matched[(int)input[j] - 97] = (int)aux[j];
                wasMapped[(int)aux[j] - 97] = 1;
            }
        }
    }

    matched[16] = (int)'z';

    //Actual stuff starts here
    getline(inputFile, input);

    cases = atoi(input.c_str());

    for (i = 0; i < cases; i++)
    {
        getline(inputFile, input);
        outputFile << "Case #" << (i + 1) << ": ";
        for (j = 0; j < input.length(); j++)
        {
            if (input[j] == ' ')
            {
                outputFile << ' ';
            }
            else
            {
                outputFile << (char)matched[(int)input[j] - 97];
            }
        }
        outputFile << endl;
    }

    return 0;
}

#endif
