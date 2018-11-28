#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main(void)
{
   string s;
   getline(cin,s);
   stringstream ss(s);
   int n;
   ss >> n;
   for (int x=1; x<=n; x++)
   {
        int list[102];
        int p, q;
        int arr[102][102];        
        getline(cin,s);
        stringstream sss(s);
        sss>> p >> q;
        for (int j=0;j<102;j++)
        {   list[j] = -1;
            for (int k=0;k<102;k++)        
            {    arr[j][k] = 0;   }
        }
        list[0] = 0;
            getline(cin,s);
            stringstream ssss(s);        
        for (int j=1;j<=q;j++)
        {
            ssss >> list[j];
        }
        list[q+1] = p+1;    //!
    //    for (int i=0; i<=q+1;i++)
    //    {cout << list[i] << endl;}
        
        for ( int i=2;i<=q+1; i++)
        {
            for (int j=0;(j+i)<=q+1;j++)
            {
                int smallest = 2000000000;
                int smallind = 0;
                for(int k=j+1; k<(j+i);k++)
                {
                    if ((arr[j][k]+arr[k][j+i])<smallest)
                    { smallest = arr[j][k]+arr[k][j+i]; 
                      smallind = k;
                    }
                }
//                cout << "smallest" << smallest << endl;
                arr[j][j+i]= smallest + list[j+i] - list[j] -2;
            }
        }
  //      cout << arr[0][2] <<" " << arr[1][3] << " " << arr[2][4] << endl;
        cout << "Case #" << x << ": " << arr[0][q+1] << endl;
    }
}
