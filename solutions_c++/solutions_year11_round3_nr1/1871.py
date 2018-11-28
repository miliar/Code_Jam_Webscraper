#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
using namespace std;

int& string2int(string& str, int& i)
{
    i = atoi(str.c_str());
    return i;
}

string& int2string(int& i, string& str)
{
     char conv[100];
     sprintf(conv,"%d",i);
     str = conv;
     return str;
}

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

int index(int col, int row, int cols)
{
    return col + row*cols;
}

int main(int argc, char *argv[])
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

    for (int ncase=0; ncase<cases; ncase++)
    {
        getline(input, linein);
        vector<string> tokens;
        tokenize(linein, tokens);

        int rows = string2int(tokens[0], rows);
        int cols = string2int(tokens[1], cols);

        char* data = new char[rows*cols];

        for (int nrow=0; nrow<rows; nrow++)
        {
            getline(input, linein);
            for (int ncol=0; ncol<cols; ncol++)
            {
                data[index(ncol, nrow, cols)] = linein[ncol];
            } //ncol
        }//nrow


        for (int nrow=0; nrow<rows; nrow++)
        {
            for (int ncol=0; ncol<cols; ncol++)
            {
                if(data[index(ncol,nrow, cols)] == '#')
                {
                    if(ncol!=cols-1 && nrow!=rows-1)
                    {
                        if(data[index(ncol+1,nrow,cols)] == '#' &&
                           data[index(ncol,nrow+1,cols)] == '#' &&
                           data[index(ncol+1,nrow+1,cols)] == '#')
                        {
                            data[index(ncol,nrow,cols)] = '/';
                            data[index(ncol+1,nrow,cols)] = '\\';
                            data[index(ncol,nrow+1,cols)] = '\\';
                            data[index(ncol+1,nrow+1,cols)] = '/';
                        }// if ####
                    }//if not edge
                }//if #
            }//ncol
        }//nrow

        bool hashfound=false;
        for (int nrow=0; nrow<rows; nrow++)
        {
            for (int ncol=0; ncol<cols; ncol++)
            {
                if(data[index(ncol,nrow, cols)] == '#')
                {
                    hashfound=true;
                    break;
                }//if #
            }//ncol
            if(hashfound)break;
        }//nrow

        string lineout = "Case #";

        string casestr;
        int casenr = ncase+1;
        int2string(casenr, casestr);

        lineout += casestr;
        lineout += ":";
        lineout += "\n";

        output.write(lineout.c_str(), lineout.size());

        if(hashfound)
        {
            lineout = "Impossible\n";
            output.write(lineout.c_str(), lineout.size());
        }
        else
        {
            lineout="";
            for (int nrow=0; nrow<rows; nrow++)
            {
                for (int ncol=0; ncol<cols; ncol++)
                {
                    lineout += data[index(ncol,nrow, cols)];
                }//ncol
                lineout += "\n";
            }//nrow
            output.write(lineout.c_str(), lineout.size());
        }

        delete data;
    }//ncase

    return 0;
}


