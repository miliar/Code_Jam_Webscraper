#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int dx[] = {0, -1, 1 , 0};
int dy[] = {-1, 0, 0, 1};

int main(void)
{
    string s;
    getline(cin,s);
    stringstream ss(s);
    int t;
    ss >> t;
    for (int i=1; i<=t; i++)
    {
        int h,w;
        char nextchar = 'a';
        getline(cin,s);
        stringstream sss(s);
        sss >> h >> w;
        int arr[h][w];
        char carr[h][w];
        for (int j=0; j< h; j++)
        {
            getline(cin,s);
            stringstream ssss(s);
            for (int k=0; k<w; k++)
            {
                ssss >> arr[j][k];
                carr[j][k] = '-';
            }
        }
        int nexth, nextw;
        for (int j=0; j< h; j++)
        {
            for (int k=0; k<w; k++)
            {
                int min = 0;
                int minx = k;
                int miny = j;                
                while (min!=1000000)
                {
                    min = 1000000;
                    if (carr[miny][minx]=='-')
                    {
                        carr[miny][minx]='.';
                        int nextx, nexty;
                        for (int l=0; l<4; l++)
                        {
                            int tempx = minx + dx[l];
                            int tempy = miny + dy[l];
                            if ((tempx>=w)||(tempx<0)||(tempy<0)||(tempy>=h)) {continue;}
                            if (arr[tempy][tempx]< arr[miny][minx])
                            {
                                if (arr[tempy][tempx]<min)
                                {   min = arr[tempy][tempx]; nextx = tempx; nexty = tempy;    }
                            }
                        }
                        minx = nextx;
                        miny = nexty;
                    }else
                    {
                        char temp = carr[miny][minx];
                        for (int j=0; j< h; j++)
                        {
                            for (int k=0; k<w; k++)
                            { if (carr[j][k]=='.') {carr[j][k]=temp;} }
                        }
                    }
                }
                bool change = false;
                for (int j=0; j< h; j++)
                {
                    for (int k=0; k<w; k++)
                    { if (carr[j][k]=='.') {carr[j][k]=nextchar; change = true;} }
                }
                if (change) {  nextchar++; }
//                                for (int j=0; j< h; j++)
//                                {
//                                 for (int k=0; k<w; k++)
//                                { cout << carr[j][k]; }
//                                 cout << endl;
//                                }                                
            }
        }        
        cout << "Case #" << i << ":" << endl;
        for (int j=0; j< h; j++)
        {
            for (int k=0; k<w; k++)
            { if (k!=0){ cout << " "; } cout << carr[j][k]; }
            cout << endl;
        }        
    }
}
