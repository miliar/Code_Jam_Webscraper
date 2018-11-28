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

int main()
{
    ifstream readFile;
    readFile.open("input.txt");
    string sNotests;
    if (readFile.is_open()) {

        getline(readFile,sNotests);

        unsigned long long iNotests = 0;

        if (!from_string<unsigned long long>(iNotests,sNotests, dec))
            cout << " Could not read number of tests... " << endl;

        for(unsigned long long iCase = 1; iCase <= iNotests; iCase++) {
            getline(readFile,sNotests);

            // boost in codeblocks : STATUS = FAIL!!!
            stringstream strstream(sNotests);

            istream_iterator<string> it(strstream);
            istream_iterator<string> end;
            vector<string> results(it, end);

            // here are the rows and columns coordinates
            unsigned long long iResultIter = 0;

            unsigned long long iNmbrOfOthers = 0;
            if (!from_string<unsigned long long>(iNmbrOfOthers,results[iResultIter++], dec))
            {
                cout << " Could not read iNmbrOfOthers... " << endl;
                return 0;
            }

            unsigned long long iLwstNote = 0;
            if (!from_string<unsigned long long>(iLwstNote,results[iResultIter++], dec))
            {
                cout << " Could not read iLwstNote... " << endl;
                return 0;
            }

            unsigned long long iHgstNote = 0;
            if (!from_string<unsigned long long>(iHgstNote,results[iResultIter++], dec))
            {
                cout << " Could not read iHgstNote... " << endl;
                return 0;
            }

            unsigned long long playArr[iNmbrOfOthers];

            string sNotes;
            getline(readFile,sNotes);


            // boost in codeblocks : STATUS = FAIL!!!
            stringstream strstreamNotes(sNotes);

            istream_iterator<string> itNotes(strstreamNotes);
            istream_iterator<string> endNotes;
            vector<string> Notes(itNotes, endNotes);

            for (unsigned long long iSpieler = 0 ; iSpieler < iNmbrOfOthers ; iSpieler++)
            {
                unsigned long long iNote = 0;
                if (!from_string<unsigned long long>(iNote,Notes[iSpieler], dec))
                {
                    cout << " Could not read Note... " << endl;
                    return 0;
                }
                     playArr[iSpieler]   =    iNote;
            }

            unsigned long long solution = 0;

            for(unsigned long long icurNote = iLwstNote ; icurNote <= iHgstNote && solution == 0 ; icurNote++ )
            {
                bool abbruch = false;
                for(unsigned long long icurPlayer = 0 ; icurPlayer < iNmbrOfOthers && !abbruch ; icurPlayer++)
                {
                    if(icurPlayer == 0 || solution != 0) {
                        if(((icurNote % playArr[icurPlayer]) == 0) ||
                            (( playArr[icurPlayer] % icurNote) == 0))
                            solution = icurNote;
                        else
                            solution = 0;
                    } else
                    {
                        abbruch = true;
                    }

//                    stringstream debug;
//                    debug << "Test:" << iCase << " curNote:" << icurNote << " plyrNote:"<<playArr[icurPlayer];
//                    cout << debug.str() << endl;
                }
            }




    stringstream ss;//create a stringstream
    if(solution)
    {
        ss << iCase << ": " << solution;
    } else {
        ss << iCase << ": " << "NO";
    }


    cout << "Case #" << ss.str() << endl;

    }
    }
    readFile.close();
    return 0;
}
