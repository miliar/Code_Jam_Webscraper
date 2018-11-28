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

            // here are the rows and columns coordinates
            unsigned int iResultIter = 0;

            unsigned int iR = 0;
            if (!from_string<unsigned int>(iR,results[iResultIter++], dec))
            {
                cout << " Could not read R... " << endl;
                return 0;
            }

            unsigned int iC = 0;
            if (!from_string<unsigned int>(iC,results[iResultIter++], dec))
            {
                cout << " Could not read C... " << endl;
                return 0;
            }

            unsigned short picture[iR][iC];
// READ THE INPUT
            for (unsigned int iZeile = 0 ; iZeile < iR ; iZeile++)
            {
                    string sRow;
                    getline(readFile,sRow);
                    for (unsigned int iSpalte = 0; iSpalte < iC; iSpalte++)
                    {
                        if(sRow[iSpalte] == '#')
                        {
                            picture[iZeile][iSpalte] = 1;
                        } else if (sRow[iSpalte] == '.')
                        {
                            picture[iZeile][iSpalte] = 0;
                        }
                    }
//                    cout << sRow << endl;
            }
  //          cout << "bla" << endl;


// FILL WITH SQUARES
            for (unsigned int iZeile = 0 ; iZeile < iR ; iZeile++)
            {
                    for (unsigned int iSpalte = 0; iSpalte < iC; iSpalte++)
                    {
                        if((picture[iZeile][iSpalte] == 1) &&
                            (picture[iZeile+1][iSpalte] == 1) &&
                            (picture[iZeile+1][iSpalte+1] == 1) &&
                            (picture[iZeile][iSpalte+1] == 1) )
                        {
                            picture[iZeile][iSpalte] = 2;
                            picture[iZeile+1][iSpalte] = 3;
                            picture[iZeile+1][iSpalte+1] = 4;
                            picture[iZeile][iSpalte+1] = 5;
                        }
                    }
            }


// IS IT IMPOSSIBLE?
            bool impossible = false;
            for (unsigned int iZeile = 0 ; iZeile < iR && !impossible ; iZeile++)
            {
                    for (unsigned int iSpalte = 0; iSpalte < iC && !impossible; iSpalte++)
                    {
                        if(picture[iZeile][iSpalte] == 1){
                            impossible = true;

                        }
                    }
            }



    stringstream ss;//create a stringstream
    ss << iCase << ": ";

    cout << "Case #" << ss.str() << endl;
// HOW THE FUCK ARE OVER 2000 PPL ALREADY FINISHED WITH THAT TASK???
            if (!impossible)
            for (unsigned int iZeile = 0 ; iZeile < iR ; iZeile++)
            {
                    for (unsigned int iSpalte = 0; iSpalte < iC; iSpalte++)
                    {
                        if(picture[iZeile][iSpalte] == 0)
                        {
                            cout << ".";
                        } else if (picture[iZeile][iSpalte] == 1)
                        {
                            cout << "#";
                        }
                        else if (picture[iZeile][iSpalte] == 2)
                        {
                            cout << "/";
                        }
                        else if (picture[iZeile][iSpalte] == 3)
                        {
                            cout << "\\";
                        }
                        else if (picture[iZeile][iSpalte] == 4)
                        {
                            cout << "/";
                        }
                        else if (picture[iZeile][iSpalte] == 5)
                        {
                            cout << "\\";
                        }

                    }
                    cout << endl;
            }
            else
            {
                cout << "Impossible" << endl;
            }

            //runTest(iCase,sNotests,results);
        }
    }

    readFile.close();
    return 0;
}
