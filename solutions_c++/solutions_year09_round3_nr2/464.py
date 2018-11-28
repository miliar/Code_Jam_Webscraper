#include <iostream>
#include <cmath>
#include <limits>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct vec
{
    double x, y, z;
};

int main()
{
    ifstream cin("B-large.in");
    //ifstream cin("B.txt");
   // ofstream cout("B-out.txt");

    vec point[1000];
    vec speed[1000];
    int N;
    cin >> N;
    int nFire;
    for (int i = 0; i < N; i++)
    {
        cin >> nFire;
        double sumX = 0.0;
        double sumY = 0.0;
        double sumZ = 0.0;
        double sumVX = 0.0;
        double sumVY = 0.0;
        double sumVZ = 0.0;
        /*unsigned double sumVX2 = 0.0;
        unsigned double sumVY2 = 0.0;
        unsigned double sumVZ2 = 0.0;*/
        for (int j = 0; j < nFire; j++)
        {
            cin >> point[j].x >> point[j].y >> point[j].z >> speed[j].x >> speed[j].y >> speed[j].z;
            sumX += point[j].x;  sumY += point[j].y;  sumZ += point[j].z;
            sumVX += speed[j].x; sumVY += speed[j].y; sumVZ += speed[j].z;
            //sumVX2 += speed[j].x*speed[j].x; sumVY2 += speed[j].y*speed[j].y; sumVZ2 += speed[j].z*speed[j].z;
        }
        //cout << endl << sumX << " " << sumY << " " << sumZ << endl << endl;
        //cout << endl << sumVX << " " << sumVY << " " << sumVZ << endl << endl;
        //bool aminx = false, aminy = false, aminz = false;
        double tminx = 2147483647.0, tminy = 2147483647.0, tminz= 2147483647.0;
        //if (sumVX != 0.0){
        
        double sumsq = (sumVX*sumVX + sumVY*sumVY + sumVZ*sumVZ);
        double sum1 = (sumVX*sumVY*sumVY*sumVZ*sumVZ);
        double sum2 = (sumVX*sumVX*sumVY*sumVZ*sumVZ);
        double sum3 = (sumVX*sumVX*sumVY*sumVY*sumVZ);
        double sum4 = (sumVX/(sumVY*sumVY*sumVZ*sumVZ) + sumVY/(sumVX*sumVX*sumVZ*sumVZ) + sumVZ/(sumVX*sumVZ*sumVY*sumVY));

       /* if (-0.000001 <= sum1 && sum1 <= 0.000001)
            tminx = 0.0;
        else if (-0.000001 <= sum2 && sum2 <= 0.000001)
            tminx = 0.0;
        else if (-0.000001 <= sum3 && sum3 <= 0.000001)
            tminx = 0.0;
        else if (-0.000001 <= sum4 && sum4 <= 0.000001)
            tminx = 0.0;
        else if (-0.000001<=sumVX*sumVY*sumVZ && sumVX*sumVY*sumVZ <= 0.000001)
            tminx = -(sumX*sumVX + sumY*sumVY + sumZ*sumVZ )/ (sumVX*sumVX + sumVY*sumVY + sumVZ*sumVZ);
        else if (sumsq != 0.0)
            tminx = -(sumX/(sumVX*sumVY*sumVY*sumVZ*sumVZ) + sumY/(sumVX*sumVX*sumVY*sumVZ*sumVZ) + sumZ/(sumVX*sumVX*sumVY*sumVY*sumVZ) )/ (sumVX/(sumVY*sumVY*sumVZ*sumVZ) + sumVY/(sumVX*sumVX*sumVZ*sumVZ) + sumVZ/(sumVX*sumVZ*sumVY*sumVY));
        else
            tminx = 0.0;
*/
        
        tminx = -((sumX*sumVX + sumY*sumVY + sumZ*sumVZ )/ (sumVX*sumVX + sumVY*sumVY + sumVZ*sumVZ));
        if (tminx <0.00001)
            tminx = 0.0;
        if ((fabs(tminx) == numeric_limits<double>::infinity()))
        {
            tminx = 0.0;
        }
        if (tminx != tminx)
        {
            tminx = 0.0;
        }
            /*if (tminx <= 0.0)
                aminx = false;
            else
            aminx = true;*/
        //}
            /*
        if (sumVY != 0.0){
            tminy = -(sumY / sumVY);
            if (tminy <= 0.0)
                aminy = false;
            else
            aminy = true;
        }
        if (sumVZ != 0.0){
            tminz = -(sumZ / sumVZ);
            if (tminz <= 0.0)
                aminz = false;
            else
            aminz = true;
        }*/

        double mint = tminx;
        /*bool foundmin = false;
        if (aminx){
            mint = tminx;
            foundmin = true;
        }
        if (aminy){
            if (foundmin && tminy != mint)
                cout << "Error: tminy=" << tminy << "!=mint=" << mint << endl;
            else{
                mint = tminy;
                foundmin=true;
            }
        }
        if (aminz)
        {
            if (foundmin && tminy != mint)
                cout << "Error: tminz=" << tminz<< "!=mint=" << mint << endl;
            else{
                mint = tminz;
                foundmin = true;
            }
        }

        if (!foundmin)
        {
            cout << "Errro: non foundmin\n";
        }*/

        double mindt = sqrt(((sumX+sumVX*mint) / nFire)*((sumX+sumVX*mint) / nFire)+((sumY+sumVY*mint) / nFire)*((sumY+sumVY*mint) / nFire)+((sumZ+sumVZ*mint) / nFire)*((sumZ+sumVZ*mint) / nFire));
        printf("Case #%d: %.8lf %.8lf\n", i+1, mindt , mint);

    }
    
}