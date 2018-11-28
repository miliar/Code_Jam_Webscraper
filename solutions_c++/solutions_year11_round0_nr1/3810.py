#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

typedef enum
{
    BLUE = 0,
    ORANGE = 1
} ROBOT;

typedef struct
{
    int button;
    ROBOT robot;
} T_INSTR;

vector<string>& tokenize(string& str, vector<string>& vec)
{
    unsigned int startpos = 0;
    unsigned int endpos = 0;
    string token;

    while(1)
    {
        endpos = str.find_first_of(" ", startpos);
        if(endpos == string::npos) endpos = str.size();

        token = str.substr(startpos, endpos-startpos);

        if(!token.empty())
        {
            vec.push_back(token);
        }

        if(endpos == str.size()) break;
        startpos = endpos+1;
        endpos = str.find_first_of(" ", startpos);
    }

    return vec;
}

int& string2int(string& str, int& i)
{
    i = atoi(str.c_str());
    return i;
}

string& int2string(int& i, string& str)
{
     char conv[50];
     sprintf(conv,"%d",i);
     str = conv;
     return str;
}

int main(int , char *[])
{
    fstream input;
    fstream output;

    input.open("A-large.in", ios::in);
    if(!input.is_open())
    {
        cerr << "Could not open input file!" << endl;
        abort();
    }

    output.open("A-large.out", ios::out | ios::trunc);
    if(!output.is_open())
    {
        cerr << "Could not open output file!" << endl;
        abort();
    }

    string linein;

    getline(input, linein);
    int cases = string2int(linein, cases);

    int totaltime;

    for(int casenr=1; casenr<=cases; casenr++)
    {
        getline(input, linein);

        vector<string> tokens;
        tokens.clear();
        tokenize(linein, tokens);

        int buttons = string2int(tokens[0], buttons);

        for(int buttonnr=0; buttonnr<buttons; buttonnr++)
        {
            vector<T_INSTR> instructions;
            instructions.clear();

            for(unsigned int index=1; index<tokens.size(); index+=2)
            {
                T_INSTR instr;

                if(tokens[index] == "O") instr.robot = ORANGE;
                else instr.robot = BLUE;

                string2int(tokens[index+1], instr.button);

                instructions.push_back(instr);
            }

            int bluepos=1;
            int orangepos=1;
            int bluetime=0;
            int orangetime=0;

            for(unsigned int idx=0; idx<instructions.size(); idx++)
            {
                T_INSTR instr = instructions[idx];

                if(instr.robot == BLUE)
                {
                    bluetime += abs((instr.button - bluepos)) + 1;
                    if(orangetime >= bluetime) bluetime = orangetime + 1;
                    bluepos = instr.button;
                }
                else if(instr.robot == ORANGE)
                {
                    orangetime += abs((instr.button - orangepos)) + 1;
                    if(bluetime >= orangetime) orangetime = bluetime + 1;
                    orangepos = instr.button;
                }
            }
            if(bluetime > orangetime) totaltime = bluetime;
            else totaltime = orangetime;
        }

        string casenrstr;
        string timestr;

        int2string(casenr, casenrstr);
        int2string(totaltime, timestr);

        string lineout = "Case #";
        lineout += casenrstr;
        lineout += ": ";
        lineout += timestr;
        lineout += "\n";
        output.write(lineout.c_str(), lineout.size());
    }

    input.close();
    output.close();

    return 0;
}
