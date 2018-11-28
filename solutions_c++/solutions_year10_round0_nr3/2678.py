#include <iostream>
#include <fstream>
#include <string>
#include<vector>
#include<queue>
#include<cmath>
#include<algorithm>
#include<cstdio>


using namespace std;


vector<long int> arr;
int ch[1005];


int main()
{

    ofstream fout ("testop.out");
    ifstream fin ("C-small.in");


    long int cas,x,r,k,n,res,i,j,a,pre,te;
    while(fin>>cas)
    {
        for(x=1;x<=cas;x++)
        {

            res=0;
            fin>>r>>k>>n;

            for(i=0;i<n;i++)
            {
                fin>>a;
                arr.push_back(a);
            }


            pre=0;
            for(i=0;i<r;i++)
            {
                te=0;
                memset(ch,0,sizeof(ch));
                while((te+arr[(pre%n)]<=k)&&ch[(pre%n)]==0)
                {
                    ch[(pre%n)]=1;
                    te+=arr[(pre%n)];
                    pre++;
                }

                res+=te;
            }

            fout<<"Case #"<<x<<": "<<res<<endl;

            arr.clear();
        }
    }
    return 0;
}
