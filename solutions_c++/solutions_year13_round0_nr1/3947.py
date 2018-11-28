#include<iostream>
#include<fstream>
#include<cstdio>
//#define inp cin
//#define out cout
using namespace std;
string arr[6];
int main()
{
    ifstream inp("input.txt");
    ofstream out("output.txt");
    int t;
    inp>>t;
    for(int T=1;T<=t;++T)
    {
        for(int i=0;i<4;++i)
        {
            inp>>arr[i];
        }
        //for(int i=0;i<4;++i)cout<<arr[i]<<endl;
        bool x=0,o=0,dash=0;
        for(int i=0;i<4;++i)
        {
            int countx=0,countt=0,counto=0;
            for(int j=0;j<4;++j)
            {
                if(arr[i][j]=='X')++countx;
                else if(arr[i][j]=='T')++countt;
                else if(arr[i][j]=='O')++counto;
                else dash = 1;
            }
            if(countx==4 || (countx==3 && countt==1)){x = 1;break;}
            else if(counto==4 || (counto==3 && countt==1)){o = 1;break;}
        }
        for(int i=0;i<4;++i)
        {
            int countx=0,countt=0,counto=0;
            for(int j=0;j<4;++j)
            {
                if(arr[j][i]=='X')++countx;
                else if(arr[j][i]=='T')++countt;
                else if(arr[j][i]=='O')++counto;
            }
            if(countx==4 || (countx==3 && countt==1)){x = 1;break;}
            else if(counto==4 || (counto==3 && countt==1)){o = 1;break;}
        }
        int countx=0,countt=0,counto=0;
        for(int i=0;i<4;++i)
        {
            if(arr[i][i]=='X')++countx;
            else if(arr[i][i]=='O')++counto;
            else if(arr[i][i]=='T')++countt;
        }
        if(countx==4 || (countx==3 && countt==1)){x = 1;}
            else if(counto==4 || (counto==3 && countt==1)){o = 1;}
        countx=0;counto=0;countt=0;
        for(int i=0;i<4;++i)
        {
            if(arr[i][3-i]=='X')++countx;
            else if(arr[i][3-i]=='O')++counto;
            else if(arr[i][3-i]=='T')++countt;
        }
        if(countx==4 || (countx==3 && countt==1)){x = 1;}
            else if(counto==4 || (counto==3 && countt==1)){o = 1;}
        if(o==1){out<<"Case #"<<T<<": O won\n";}
        else if(x==1){out<<"Case #"<<T<<": X won\n";}
        else if(dash==1){out<<"Case #"<<T<<": Game has not completed\n";}
        else {out<<"Case #"<<T<<": Draw\n";}
    }
    return 0;
}
