/**
    Google CodeJam 2011 qualification rounds, Bot Trust
    Heikki Ikäheimonen
    heikki.ikaheimonen@gmail.com
    07.05.2011
**/


#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int botTrust(string str);


int main()
{
  int n=0;
  string cases;
  getline(cin,cases);
  istringstream(cases) >> n;

  int i = 0;

  while(i<n)
  {
    string input;
    getline(cin,input);
    i++;
    cout << "Case #" << i << ": " << botTrust(input) << endl;
  }

    return 0;
}


int botTrust(string str)
{
    istringstream iss(str, istringstream::in);
    int buttons = 0;
    iss >> buttons;

    int oAt = 1;
    int oNext = 0;
    int bAt = 1;
    int bNext = 0;

    int bottime = 0;

    size_t ofound;
    size_t bfound;

    // whos button is next button
    bool oturn = true;

    ofound=str.find_first_of("O");
    bfound=str.find_first_of("B");

    iss.clear();
    iss.str(str.substr(ofound+1, str.find_first_of("OB",ofound+1)-(ofound+1)));
    iss >> oNext;
    iss.clear();
    iss.str(str.substr(bfound+1, str.find_first_of("OB",bfound+1)-(bfound+1)));
    iss >> bNext;

    //cout << "oNext: " << oNext << " bNext: " << bNext << endl;

    if(bfound < ofound) oturn = false;

    int pushes = 0;
    while(pushes < buttons)
    {

        if(oturn)
        {
            // B moves or waits
            if(bAt < bNext)
            {
                bAt++;
            }else if(bAt > bNext){
                bAt--;
            }

            // O moves or push
            if(oAt == oNext)
            {
                //cout << " O push " << "bAt: " << bAt << " oAt: " << oAt
                //   << " time: " << bottime << endl ;
                pushes++;
                ofound = str.find_first_of("O", ofound+1);
                string substr = str.substr(ofound+1, str.find_first_of("OB",ofound+1)-(ofound+1));
                iss.clear();
                iss.str(substr);
                iss >> oNext;

                // cout << "oNext: " << oNext << " bNext: " << bNext << endl;           

            }else if(oAt < oNext){
                oAt++;
            }else if(oAt > oNext){
                oAt--;
            }
        }

        if(!oturn)
        {
            // O moves or waits
            if(oAt < oNext)
            {
                oAt++;
            }else if(oAt > oNext){
                oAt--;
            }

            // B moves or push
            if(bAt == bNext)
            {
                //cout << " B push " << "bAt: " << bAt << " oAt: " << oAt <<
                //    " time: " << bottime << endl  ;
                pushes++;
                bfound = str.find_first_of("B", bfound+1);
                string substr = str.substr(bfound+1, str.find_first_of("OB",bfound+1)-(bfound+1));
                
                iss.clear();
                iss.str(substr);
                iss >> bNext;

                //cout << "oNext: " << oNext << " bNext: " << bNext << endl;          

            }else if(bAt < bNext){
                bAt++;
            }else if(bAt > bNext){
                bAt--;
            }
        }


        if(ofound < bfound){
             oturn = true;
        }else{
            oturn = false;
        }
        bottime++;


    }

    return bottime;
}
