#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<fstream>
typedef long long int int64;

using namespace std;

int main()
{
    int t;
    
    ifstream fin("input.txt");
    ofstream fout("ans.txt");
    if(!fin)
    {
            cout<<"Wrong Location";
            cin>>t;
            exit(1);
    }
    fin>>t;
    
    int n=t;
    while(t--)
    {
              int M,K,L,flag=0;
              fin>>M>>K>>L;
              vector<int> freq;
              for(int i=0;i<L;i++)
              {
                      int temp;
                      fin>>temp;
                      freq.push_back(temp);
              }
              sort(freq.begin(),freq.end());
              reverse(freq.begin(),freq.end());
              int sum=0;
              int pos=1;
              for(int i=0;i<freq.size();)
              {
                      if(freq[i]==0)
                        break;
                      if(pos>M)
                      {
                               flag=1;
                               break;
                      }
                      int j=i;
                      for( j=i;j<i+K&&j<freq.size();j++)
                         sum+=freq[j]*pos;
                      pos++;
                      i=j;
              }
              fout<<"Case #"<<n-t<<": ";
              if(!flag)
                 fout<<sum<<"\n";
              else fout<<"IMPOSSIBLE\n";
    }
    cin>>t;
}
                         

