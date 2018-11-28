#include <iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
#define pb push_back

int abs(int n)
{
    if(n<0)
    return n*-1;
    else
    return n;
}

int main()
{
    ifstream in("D:\\inp.txt");
    ofstream out("D:\\out.txt");
    int t,r,c;
    in>>t;
    for(int ii=1;ii<=t;ii++)
    {
        in>>r>>c;
        vector<string> inp(r);
        for(int i=0;i<r;i++)
        {
            in>>inp[i];
        }
        int flag=0;
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                if(inp[i][j]=='#')
                {
                    if(inp[i][j+1]=='#' && inp[i+1][j]=='#' && inp[i+1][j+1]=='#')
                    {
                        inp[i][j]='/';
                        inp[i][j+1]='\\';
                        inp[i+1][j]='\\';
                        inp[i+1][j+1]='/';
                    }
                    else
                    {
                        flag=1;
                    }

                }
            }
            if(flag==1)
            {
                break;
            }
        }
        if(flag==1)
        {
            out<<"Case #"<<ii<<":\nImpossible"<<endl;
        }
        else
        {
            out<<"Case #"<<ii<<":"<<endl;
            for(int i=0;i<r;i++)
            out<<inp[i]<<endl;
        }
    }
    return 0;
}
