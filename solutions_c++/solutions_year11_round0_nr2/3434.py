#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iterator>


using namespace std;

template <class T>
bool from_string(T& t,
                 const string& s,
                 ios_base& (*f)(ios_base&))
{
  istringstream iss(s);
  return !(iss >> f >> t).fail();
}

char combine(char elemBefore,char thenew,vector<string> &baseelements)
{
    for(unsigned int i = 0 ; i < baseelements.size(); i++)
    {
        string formula = baseelements[i];

        if(formula[0] == elemBefore && formula[1] == thenew)
        {
            return formula[2];
        } else if(formula[1] == elemBefore && formula[0] == thenew)
        {
            return formula[2];
        }
    }
    cout << "ERROR while combine!!";
    return elemBefore;
}

bool dooppose(string allelems,char theNew,vector<string> &opposeelements)
{
    string loc = allelems + theNew;
    // user ITERATOR HERE
    for(unsigned int i = 0 ; i < opposeelements.size(); i++)
    {
        string formula = opposeelements[i];
        if(loc.find(formula[0]) != -1 && loc.find(formula[1]) != -1 )
        {
            return true;
        }

    }
    return false;
}
bool cancombine(char elemBefore,char theNew,vector<string> &baseelements)
{
    // user ITERATOR HERE
    for(unsigned int i = 0 ; i < baseelements.size(); i++)
    {
        string formula = baseelements[i];

        if(formula[0] == elemBefore && formula[1] == theNew)
        {
            return true;
        } else if(formula[1] == elemBefore && formula[0] == theNew)
        {
            return true;
        }
    }
    return false;
}


void runTest(int iCase, string sNoteTests, vector<string> &results)
{
    unsigned int iResultIter = 0;

    // first build base elems:
    vector<string> baseelements;
    unsigned int iNoBaseElems =0;
    if (!from_string<unsigned int>(iNoBaseElems,results[iResultIter++], dec))
    {
           cout << " Could not read number of base elems... " << endl;
           return;
    }
    for(unsigned int i = 0; i < iNoBaseElems; i++)
    {
            baseelements.push_back(results[iResultIter++]);
         //   cout << "Base:" << baseelements[i] << endl;
    }
    // Now opposed elements. I would like to hack that nicer, but TODAY IS MY BIRTHDAY
    vector<string> opposeelements;
    unsigned int iNoOpposeElems =0;
    if (!from_string<unsigned int>(iNoOpposeElems,results[iResultIter++], dec))
    {
           cout << " Could not read number of oppose elems... " << endl;
           return;
    }
    for(unsigned int i = 0; i < iNoOpposeElems; i++)
    {
            opposeelements.push_back(results[iResultIter++]);
       //     cout << "Oppose:" << opposeelements[i] << endl;
    }

    // now to the spellcasting
    unsigned int iKeyspressed =0;
    if (!from_string<unsigned int>(iKeyspressed,results[iResultIter++], dec))
    {
           cout << " Could not read number of oppose elems... " << endl;
           return;
    }
    string thecast = results[iResultIter++];

//    cout << "The Cast " << thecast << endl;

    string resultstring = "";
    char elemBefore = ' ';

    for(unsigned int i = 0; i < iKeyspressed; i++)
    {
//        cout << elemBefore << "und" << thecast[i] << endl;
        if (cancombine(elemBefore,thecast[i],baseelements))
        {
//            cout << " CAN COMBINE!!" << endl;
            resultstring.push_back(combine(elemBefore,thecast[i],baseelements));
            elemBefore = ' ';
        }
        else {
            if(elemBefore != ' ')
            {
                resultstring.push_back(elemBefore);
            }
            elemBefore = thecast[i];

            if(dooppose(resultstring,elemBefore,opposeelements))
            {
                    resultstring.clear();
                    elemBefore = ' ';
            }
        }


    }
    if(elemBefore != ' ')
    {
        resultstring.push_back(elemBefore);
    }

    stringstream ss;//create a stringstream
    ss << iCase << ": [";// << iTime;//add number to the stream

    for (int j = 0; j < resultstring.size();j++)
    {
        ss << resultstring[j];
        if (j != resultstring.size() -1)
        {
            ss << ", ";
        }
    }

    cout << "Case #" << ss.str() << "]" << endl;

}

int main()
{
    ifstream readFile;
    readFile.open("input.txt");
    string sNotests;
    if (readFile.is_open()) {

        getline(readFile,sNotests);

        unsigned int iNotests = 0;

        if (!from_string<unsigned int>(iNotests,sNotests, dec))
            cout << " Could not read number of tests... " << endl;

        for(unsigned int iCase = 1; iCase <= iNotests; iCase++) {
            getline(readFile,sNotests);

            // boost in codeblocks : STATUS = FAIL!!!
            stringstream strstream(sNotests);

            istream_iterator<string> it(strstream);
            istream_iterator<string> end;
            vector<string> results(it, end);

            runTest(iCase,sNotests,results);
        }
    }

    readFile.close();
    return 0;
}
