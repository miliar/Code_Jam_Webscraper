#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iterator>


using namespace std;

//struct botneedstargetres {
//
//};

string blue = string("B");
string orange = string("O");

template <class T>
bool from_string(T& t,
                 const string& s,
                 ios_base& (*f)(ios_base&))
{
  istringstream iss(s);
  return !(iss >> f >> t).fail();
}

unsigned int nextTargetBot(unsigned int cur_pos, vector<string> &results)
{
    bool bSearchEnd = false;
    unsigned int result = 0;

    while(!bSearchEnd){
        if(cur_pos < results.size()) {
            if(results[cur_pos].compare(orange) == 0)
            {
                bSearchEnd = true;
                result = 1;
            }
            if(results[cur_pos].compare(blue) == 0)
            {
                bSearchEnd = true;
                result = 2;
            }
            cur_pos++;
        }
        else
        {
            bSearchEnd = true;
        }
    }
    return result;
}

unsigned int botNeedsTarget(int whichbot, unsigned int cur_pos, vector<string> &results)
{
    bool bSearchEnd = false;
    unsigned int result = 0;

    while(!bSearchEnd){
        if(cur_pos < results.size()) {
            switch(whichbot){
            case 1:
                if(results[cur_pos].compare(orange) == 0)
                {
                    bSearchEnd = true;
                    if (!from_string<unsigned int>(result,results[++cur_pos], dec))
                    {
                        cout << "Error in botneedstarget orange [" << results[cur_pos] << "]" << endl;
                    }
                }
                break;
            case 2:
                if(results[cur_pos].compare(blue) == 0)
                {
                    bSearchEnd = true;
                    if (!from_string<unsigned int>(result,results[++cur_pos], dec))
                    {
                        cout << "Error in botneedstarget blue [" << results[cur_pos] << "]" << endl;
                    }
                }
                break;


            default:
                cout << "ERROR botNeedsTarget" << endl;
                return 0;
            }
            cur_pos++;
        }
        else
        {
            bSearchEnd = true;
        }
    }
    return result;
}

void runTest(int iCase, string sNoteTests, vector<string> &results)
{
    unsigned int iTime = 1;
    unsigned int iPushes = 0;
    unsigned int iOTarget = 0;
    unsigned int iBTarget = 0;
    unsigned int iNextTargetBot = 0;
    unsigned int iOPos = 1, iBPos = 1;
    bool bONeedsTarget = true, bBNeedsTarget = true, bTestDone = false, bNeedNextTargetBot = true;

    unsigned int iNumberOfPushes = 0;
    unsigned int iResultIter = 0;

    if (!from_string<unsigned int>(iNumberOfPushes,results[iResultIter++], dec))
    {
           cout << " Could not read number of pushes... " << endl;
           return;
    }

    while(!bTestDone)
    {
        if (bONeedsTarget){
            iOTarget = botNeedsTarget(1,iResultIter,results);
            bONeedsTarget = false;
        }
        if (bBNeedsTarget){
            iBTarget = botNeedsTarget(2,iResultIter,results);
            bBNeedsTarget = false;
        }
        if (bNeedNextTargetBot){
            iNextTargetBot = nextTargetBot(iResultIter,results);
            bNeedNextTargetBot = false;
        }
        // What does orange do?
        // Should he move?
        if (iOTarget != iOPos){
            if(iOPos > iOTarget)
                iOPos--;
            else
                iOPos++;
        // Should he Push?
        } else if (iOTarget == iOPos && iNextTargetBot == 1) {
            iPushes++;
            bONeedsTarget = true;
            bNeedNextTargetBot = true;
            iResultIter += 2;
        }

        // Should he move?
        if (iBTarget != iBPos){
            if(iBPos > iBTarget)
                iBPos--;
            else
                iBPos++;
        // Should he Push?
        } else if (iBTarget == iBPos && iNextTargetBot == 2) {
            iPushes++;
            bBNeedsTarget = true;
            bNeedNextTargetBot = true;
            iResultIter += 2;
        }

        bTestDone = iPushes >=  iNumberOfPushes? true : false;
        if(bTestDone == false)
        {
            iTime++;
        }
    }
    stringstream ss;//create a stringstream
    ss << iCase << ": " << iTime;//add number to the stream

    cout << "Case #" << ss.str() << endl;

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

//            ostream_iterator<string> oit(cout);
//            copy(results.begin(), results.end(), oit);

           // cout << results[0];

         //   cout << results.pop_back();

            runTest(iCase,sNotests,results);
        }

//        while (!readFile.eof()) {
//            readFile >> output;
//            cout << output;
//        }
    }

    readFile.close();
    return 0;
}
