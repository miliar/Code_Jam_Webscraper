#include <iostream>
#include <fstream>
#include <string>
#include<vector>
#include<queue>
#include<cmath>
#include<algorithm>
#include<cstdio>



using namespace std;


int main()
{

    ofstream fout ("telar123.out");
    ifstream fin ("A-large.in");


    long int n,a,cas,x;

    while(fin>>cas)
    {
        for(x=1;x<=cas;x++)
        {
            fin>>n>>a;



            for(;a>0&&n>0;)
            {
                if(a%2==1)
                {
                    n--;
                    a/=2;
                }
                else
                {
                     break;
                }
            }

            if(n>0) fout<<"Case #"<<x<<": OFF"<<endl;
            else fout<<"Case #"<<x<<": ON"<<endl;
        }
    }
    return 0;
}
