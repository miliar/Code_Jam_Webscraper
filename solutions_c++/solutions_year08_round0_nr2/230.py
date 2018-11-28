#include<iostream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>

using namespace std;

#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
#define MP make_pair

int date2int(string time)
{
  int hh,mm;
  sscanf(time.c_str() , "%d:%d" , &hh , &mm);
  return 60 * hh + mm ; 
}
int backA[60*30],backB[60*30];
int main()
{
  int n , case_no=1; 
  cin>>n;
  while(n--)
    {
      int ansA = 0 , ansB = 0 , T , NA , NB;
      cin>>T;
      cin>>NA>>NB;
      vector<pair<int,int> > A(NA) , B(NB);
      FOR(i,NA)
        {
          string from , to ;
          cin>>from>>to;
          A[i] = MP(date2int(from) , date2int(to) + T);
        }
      FOR(i,NB)
        {
          string from , to ;
          cin>>from>>to;
          B[i] = MP(date2int(from) , date2int(to) + T);
        }
      memset(backA , 0 , sizeof(backA));
      memset(backB , 0 , sizeof(backB));
      int stockA=0 , stockB=0;
      FOR(t,24*60)
        {
          stockA += backA[t];
          stockB += backB[t];
          FOR(i,NA) if(A[i].first == t) {
            if(stockA==0){
              stockA++ ; 
              ansA++;
            }
            stockA-- ; 
            backB[A[i].second]++;
          }

          FOR(i,NB) if(B[i].first == t) {
            if(stockB==0){
              stockB++ ; 
              ansB++;
            }
            stockB-- ; 
            backA[B[i].second]++;
          }
        }
      printf("Case #%d: %d %d\n" , case_no++ , ansA , ansB);
    }
  return 0 ;
}
