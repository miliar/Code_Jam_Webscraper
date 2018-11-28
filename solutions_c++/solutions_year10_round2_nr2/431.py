#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int case_number;
#define gout case_number++, printf("Case #%d: ",case_number), cout
#define F(i,n) for((i)=0;(i)<(n);(i)++)

void repeat()
{
     int T,N,K,B;
     //long int B;
     vector <int> X,V,S;
     int i,j,c=0,swaps=0;
     
     cin>>N>>K>>B>>T;
     F(i,N)
     {
           cin>>j;
           X.push_back(j);
     }
     F(i,N)
     {
           cin>>j;
           V.push_back(j);
           if(T*j + X[i] >= B)
                  S.push_back(N-1-i);
           else
                  S.push_back(-1);
           //cout<<"S[j]="<<S[i]<<endl;
     }
     j=N-1;
     while(c<K && j>=0)
     {
               if(S[j] == -1)
               {
                       j--;
                       continue;
               }
               swaps = swaps + (S[j] - c) ;
               c++;
               //cout<<"swaps="<<swaps<<"c="<<c<<"S[j]="<<S[j];
               j--;
     }
     //printf("B=%d",B);
     if(c<K)
     {
            gout<<"IMPOSSIBLE"<<endl;
     }
     else
     {
            gout<<swaps<<endl;
     }
}

int main(int argc, char *argv[])
{
    int i,T;
    case_number = 0;
    cin>>T;
    F(i,T)
          repeat();
}
