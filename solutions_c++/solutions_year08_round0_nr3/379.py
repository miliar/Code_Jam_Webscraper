
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>

#define PI 3.14159265

using namespace std;

double LengthOfTwoPoints(double x1, double y1, double x2, double y2)
{
    return sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

// two points on circle
double getSpecialArea(double r, double x1, double y1, double x2, double y2)
{
    if (x1 > x2)
    {
        double xTmp = x1, yTmp = y1;
        x1 = x1; y1 = y2;
        x2 = xTmp; y2 = yTmp;
    }

    double angle1 = atan(y1/x1); // bigger
    double angle2 = atan(y2/x2);

    double areaShanXin = PI*r*r * (angle1 - angle2) / (2*PI);

    double halfStringLength = LengthOfTwoPoints(x1, y1, x2, y2) / 2;

    double areaArc = areaShanXin - halfStringLength * sqrt(r*r-halfStringLength*halfStringLength);

    double areaSmallTriangle = (x2-x1)*(y1-y2)/2;

    double area = areaSmallTriangle + areaArc;
    return area;
}

// get the area of a square in a circle.
// the bottom-left point of the square is (x, y)
// g is the length of the square.
// center of the circle is (0,0)
double SquareAreaInCircle( double x, double y, double g, double r )
{
    // make sure (x, y) to circle angle < 45 degree. (x >= y)
    if ( x < y )
    {
        double dTemp = x;
        x = y;
        y = dTemp;
    }
    // (x1, y1)  (x2, y2)
    // (x3, y3)  (x4, y4)
    double x1,x2,x3,x4,y1,y2,y3,y4;
    x1 = x;     y1 = y + g;
    x2 = x + g; y2 = y + g;
    x3 = x;     y3 = y;
    x4 = x + g; y4 = y;

    double L1 = LengthOfTwoPoints( x1, y1, 0, 0 );
    double L2 = LengthOfTwoPoints( x2, y2, 0, 0 );
    double L3 = LengthOfTwoPoints( x3, y3, 0, 0 );
    double L4 = LengthOfTwoPoints( x4, y4, 0, 0 );

    double dArea;

    // square is completely in circle
    if ( L2 <= r )
        return g*g;

    // square is out of circle
    if ( L3 >= r )
        return 0;

    if ( L3 < r && L1 >= r && L4 >= r )
    {
        double xInt13 = x1;
        double yInt13 = sqrt(r*r - x1*x1);
        double xInt34 = sqrt(r*r - y3*y3);
        double yInt34 = y3;

        dArea = getSpecialArea(r, xInt13, yInt13, xInt34, yInt34);
        return dArea;
    }

    if ( L1 <= r && L4 <= r && L2 > r )
    {
        double xInt12 = sqrt(r*r - y1*y1);
        double yInt12 = y1;
        double xInt24 = x2;
        double yInt24 = sqrt(r*r - x2*x2);

        double dSpecialArea = getSpecialArea(r, xInt12, yInt12, xInt24, yInt24);

        dArea = g*(xInt12-x1) +  (xInt24-xInt12)*(yInt24-y4) + dSpecialArea;
        return dArea;
    }

    if ( L1 <= r && L4 >= r )
    {
        double xInt12 = sqrt(r*r - y1*y1);
        double yInt12 = y1;
        double xInt34 = sqrt(r*r - y3*y3);
        double yInt34 = y3;

        double dSpecialArea = getSpecialArea(r, xInt12, yInt12, xInt34, yInt34);

        dArea = g*(xInt12-x1) + dSpecialArea;
        return dArea;
    }

    cout << "error" << endl;
    return -1000;
}

int main( int argc, char *argv[]) 
{

    bool bFromFile = false;
    int nCount = 0;
    string strInputFile, strOutputFile;
    ifstream fsInput;
    ofstream fsOutput;
    int nIndex = 0;

    if ( argc == 1 )
    {
        cout << "Input count:";
        cin >> nCount;
        bFromFile = false;
    }
    else if ( argc == 3)
    {
        strInputFile = argv[1];
        strOutputFile = argv[2];
        cout << "Input file: " << strInputFile << "  Out file:" << strOutputFile << endl;
        bFromFile = true;
        fsInput.open(strInputFile.c_str());
        fsInput >> nCount;
        fsOutput.open(strOutputFile.c_str());
    }
    else
    {
        cout << "Wrong input paramters." << endl;
        return 0;
    }

    while( nCount-- > 0 )
    {
        nIndex++;

        double f = 0.0, R = 0.0, t = 0.0, r = 0.0, g = 0.0;

        if ( bFromFile )
        {
            fsInput >> f >> R >> t >> r >> g;
        }
        else
        {
            cin >> f >> R >> t >> r >> g;
        }

        double g2 = g - 2.0 * f;
        double r2 = r + f;
        double RInner2 = R - t - f;

        double dTotalArea = 0.0;

        int nSquare = (int)(RInner2/(g2 + 2*r2)) + 1;
        for ( int i = 1; i <= nSquare; i++)
        {
            for ( int j = 1; j <= nSquare; j++)
            {
                double dTempArea = 0;
                double dTempX = (g2 + 2*r2) * (i - 1) + r2;
                double dTempY = (g2 + 2*r2) * (j - 1) + r2;
                dTempArea = SquareAreaInCircle(dTempX, dTempY, g2, RInner2);
                dTotalArea += dTempArea;
            }
        }

        dTotalArea *= 4;

        double dProp = 0.0;
        dProp = 1.0 - dTotalArea / (PI*R*R);

        char charbuf[20];
        sprintf(charbuf, "%0.6f", dProp);

        stringstream sMsg;
        sMsg << "Case #" << nIndex << ": " << charbuf;
        sMsg.flush();
        cout << sMsg.str() << endl;
    
        if (bFromFile)
            fsOutput << sMsg.str() << endl;
    }

    if (bFromFile)
    {
        fsInput.close();
        fsOutput.flush();
        fsOutput.close();
    }
    cout << "End" << endl;
}