#include <iostream>
#include <string>
#include <sstream>
using namespace std;
 int main()
 {
    int testCases;
    string temp;
    getline(cin,temp);
    stringstream t1(temp);
    t1>> testCases;
    string inputString;
   // string outputString;
    char mppng[26];
    mppng[0] = 'y';
    mppng[1] = 'h';
    mppng[2] = 'e';
    mppng[3] = 's';
    mppng[4] = 'o';
    mppng[5] = 'c';
    mppng[6] = 'v';
    mppng[7] = 'x';
    mppng[8] = 'd';
    mppng[9] = 'u';
    mppng[10] = 'i';
    mppng[11] = 'g';
    mppng[12] = 'l';
    mppng[13] = 'b';
    mppng[14] = 'k';
    mppng[15] = 'r';
    mppng[16] = 'z';
    mppng[17] = 't';
    mppng[18] = 'n';
    mppng[19] = 'w';
    mppng[20] = 'j';
    mppng[21] = 'p';
    mppng[22] = 'f';
    mppng[23] = 'm';
    mppng[24] = 'a';
    mppng[25] = 'q';
    for(int i = 0; i< testCases;i++)
    {
      string outputString;
      getline(cin,inputString);
       // cout << inputString<<endl;
        int l = inputString.length();
        int k =0;
        for(k =0; k<l;k++)
        {
            if(inputString[k]== ' ')
                outputString.push_back(' ');
            else
            {
                char temp =mppng[inputString[k]-97];
                outputString.push_back(temp);
            }
        }
       // outputString[k] = '\0';
        cout<<"Case #"<<i+1<<": "<<outputString<<endl;
    }
     return 0;
 }
