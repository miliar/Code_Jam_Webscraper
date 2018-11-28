#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <map>

using namespace std;

int main()
{
    ifstream is;
    ofstream rs;
    is.open("./C-large.in");
    rs.open("./res.out");
    int num_of_test;
    is >>  num_of_test;
    for(int num=0; num<num_of_test; num++)
    {
        int A, B;
        int res=0;
        is >> A;
        is >> B;
        for (int N=A;N<B;N++)
        {
            int n=N;
            vector<int> used;
            vector<int> numbers;
            do
            {
                div_t divresult;
                divresult = div (n,10);
                n = divresult.quot;
                numbers.push_back(divresult.rem);
            }
           while(n>0);
           for(int i=0;i<numbers.size()-1;i++)
           {
                int new_n=0;
                for(int j=i;j>=0;j--)
                    new_n=new_n*10+numbers[j];
                for(int j=numbers.size()-1;j>i;j--)
                    new_n=new_n*10+numbers[j];
                bool find=false;
                for(int k=0;k<used.size();k++)
                {
                    if(used[k]==new_n) find=true;
                }
                if(!find&&(new_n>N)&&(new_n<=B))
                {
                    used.push_back(new_n);
                    res=res+1;
                }
            }
        }
        rs << "Case #" << num+1 << ": " << res << endl;
    }
    return 0;
}


