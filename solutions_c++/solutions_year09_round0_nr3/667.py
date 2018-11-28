#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>
#include <stack>

using namespace std;
int array_result[20][501]={0};
char str_judge[]="maj edoc ot emoclew";
int main()
{
 ifstream in("a.in");
    ofstream out("a.out");
int array_result[20][501]={0};

    int N=0;
    in>>N;

    string str_input;
    getline(in,str_input);
    for(int i=1;i<=N;i++)
    {
        memset(array_result,0,sizeof(array_result));
        str_input.clear();
        getline(in,str_input);
        int n_size=str_input.length();
        for(int j=0;j<n_size;j++)
        {
            array_result[0][j]=1;
        }
        for(int k=1;k<=19;k++)
        {
            array_result[k][0]=0;
        }
        for(int k=1;k<=19;k++)
        {
            char c_check=str_judge[k-1];
            for(int j=1;j<=n_size;j++)
            {
                if(str_input[n_size-j]==c_check)
                    array_result[k][j]=array_result[k][j-1]+array_result[k-1][j-1];
                else
                    array_result[k][j]=array_result[k][j-1];
                if(array_result[k][j]>=10000)
                    array_result[k][j]%=10000;
            }
        }

        out<<"Case #"<<i<<": ";
        int n_temp=array_result[19][n_size];
        int n_base=1000;
        while(n_base>0)
        {
            out<<n_temp/n_base;
            n_temp%=n_base;
            n_base/=10;
        }
        out<<endl;

    }
    return 0;
}
