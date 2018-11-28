#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)


int main()
{
    int cases;
    cin >> cases;
    cin >> ws;
    REP(i,cases)
    {

        string str;
        getline(cin,str);
        istringstream iss(str, istringstream::in);
        int R, C;
        iss >> R;
        iss >> C;

        //cout << "R " << R << " C " << C << endl;

        vector<string> picture;
        REP(j,R)
        {
            string str2;
            getline(cin,str2);
            picture.push_back(str2);
        }

        bool impossible = false;
        if(R*C < 4)
        {
            REP(j,R)REP(k,C){

                if(picture[j][k] != '.'){

                    impossible = true;
                    j= R;
                    k = C;

                }

            }

        }else{
            REP(j,R)
            {
               REP(k,C)
               {
                   if(picture[j][k] == '#')
                   {

                       if((j+1) < R && (k+1) < C)
                       {
                        if(picture[j+1][k] == '#' &&
                           picture[j][k+1] == '#' &&
                           picture[j+1][k+1] == '#')
                           {
                            // change
                            picture[j][k] ='/';
                            picture[j+1][k] = '\\';
                            picture[j][k+1] = '\\';
                            picture[j+1][k+1] = '/';

                           }
                       }

                   }
               }
            }
        }

         REP(j,R)REP(k,C){
            if(picture[j][k] == '#') impossible = true;
         }


        if(impossible)
        {
            cout << "Case #" << i+1 << ":"<< endl;
            cout << "Impossible" << endl;

        }else{

            cout << "Case #" << i+1 << ":"<< endl;
            REP(j,R){

                    cout << picture[j] << endl;
            }
        }

    }



    return 0;
}
