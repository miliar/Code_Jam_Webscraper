#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>

using namespace std;

typedef struct
{
    string reactor;
    string result;
} T_REACTOR;


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

int main(int , char *[])
{
    fstream input;
    fstream output;

    input.open("B-large.in", ios::in);
    if(!input.is_open())
    {
        cerr << "Could not open input file!" << endl;
        abort();
    }

    output.open("B-large.out", ios::out | ios::trunc);
    if(!output.is_open())
    {
        cerr << "Could not open output file!" << endl;
        abort();
    }

    string linein;

    getline(input, linein);
    int cases = string2int(linein, cases);

    for(int casenr=1; casenr<=cases; casenr++)
    {
        getline(input, linein);

        vector<string> tokens;
        tokens.clear();
        tokenize(linein, tokens);

        multimap<string, T_REACTOR> combinations;
        multimap<string, string> oppositions;

        int start = 1;
        int len = string2int(tokens[0], len);
        for(int index=0; index<len; index++)
        {
            string in = tokens[index+start];

            string variant1 = in.substr(0,1);

            T_REACTOR reactor1;
            reactor1.reactor = in.substr(1,1);
            reactor1.result = in.substr(2,1);

            string variant2 = in.substr(1,1);

            T_REACTOR reactor2;
            reactor2.reactor = in.substr(0,1);
            reactor2.result = in.substr(2,1);

            combinations.insert(pair<string,T_REACTOR>(variant1, reactor1));
            combinations.insert(pair<string,T_REACTOR>(variant2, reactor2));
        }

        start = start + len;
        len  = string2int(tokens[start], len);
        start++;
        for(int index=0; index<len; index++)
        {
            string in = tokens[index+start];

            string variant1 = in.substr(0,1);
            string other1 = in.substr(1,1);
            string variant2 = other1;
            string other2 = variant1;

            oppositions.insert(pair<string,string>(variant1, other1));
            oppositions.insert(pair<string,string>(variant2, other2));
        }

        start = start + len + 1;
        string elements = tokens[start];

        string out;

        for (unsigned int index=0; index<elements.size(); index++)
        {
            string chr1 = elements.substr(index,1);

            bool combined=false;
            bool opposed=false;

            if(!out.empty())
            {
                string chr2 = out.substr(out.length()-1,1);

                pair<multimap<string,T_REACTOR>::iterator,multimap<string,T_REACTOR>::iterator> reactives = combinations.equal_range(chr1);

                for (multimap<string,T_REACTOR>::iterator reactive=reactives.first; reactive!=reactives.second; ++reactive)
                {
                    if((*reactive).second.reactor == chr2)
                    {
                        out[out.length()-1] = ((*reactive).second.result.c_str()[0]);
                        combined = true;
                        break;
                    }
                }
            }

            if(!combined)
            {
                pair<multimap<string,string>::iterator, multimap<string,string>::iterator> reactives;
                reactives = oppositions.equal_range(chr1);

                for(multimap<string,string>::iterator reactive=reactives.first; reactive!=reactives.second; ++reactive)
                {
                    if(out.find((*reactive).second) != string::npos)
                    {
                        out.clear();
                        opposed = true;
                        break;
                    }
                }
            }

            if(!combined && !opposed)
            {
                out.append(chr1);
            }
        }

        string casenrstr;
        int2string(casenr, casenrstr);

        string lineout = "Case #";
        lineout += casenrstr;
        lineout += ": [";

        for (unsigned int i=0; i<out.size(); i++)
        {
            lineout += out.substr(i,1);
            if (i+1<out.size()) lineout += ", ";
        }

        lineout += "]\n";
        output.write(lineout.c_str(), lineout.size());
    }

    input.close();
    output.close();

    return 0;
}
