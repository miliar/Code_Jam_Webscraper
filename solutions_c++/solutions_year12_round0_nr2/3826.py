#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int array_n[200]={0};
int main()
{
    ifstream cin("b.in");
    ofstream cout("b.out");
    int t=0;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        memset(array_n,0,sizeof(array_n));
        int n=0,s=0,p=0;
        int result=0;
        cin>>n>>s>>p;
        for(int j=0;j<n;j++)
          cin>>array_n[j];

        sort(&array_n[0],&array_n[n]);
        for(int j=n-1;j>=0;j--)
        {
            array_n[j]-=p;
            int check1=(p-1)>=0?p-1:0;
            if(array_n[j]>=2*check1)
            {
                result++;
                continue;
            }
            int check2=(p-2)>=0?p-2:0;
            if(array_n[j]>=2*check2)
            {
                if(s>0)
                {
                    s--;
                    result++;
                }else{
                    break;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<result<<endl;

    }
  //  cout << "Hello world!" << endl;
    return 0;
}
