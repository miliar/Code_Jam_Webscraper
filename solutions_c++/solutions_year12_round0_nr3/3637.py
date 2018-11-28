#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

#define forn(i,n) for(int i=0; i<n; i++)
#define dbg(n) cout<<#n<<": "<<n<<endl;
#define mp make_pair

int T, A, B;
vector<int> As, Bs;

long long tenPowered[] =
{
 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000    
};

vector<pair<int,int> > pairs[55];
int pairsCount[55];

void input()
{
     ifstream input("C.in");
     input>>T;
     As.resize(T);
     Bs.resize(T);
     forn(i, T)
     {
          input>>As[i];
          input>>Bs[i];   
     }
     input.close();
}

int totalDigits(int n)
{
 int answer = 0;
 while(n!=0)
 {
  answer++;
  n/=10;           
 }
 return answer;
}
bool inRange(int m, int a, int b)
{
 return (m>a && m<=b);    
}
int shifted(int n, int shift)
{
 return n/tenPowered[shift]+(n%tenPowered[shift])*tenPowered[totalDigits(n/tenPowered[shift])];   
}
void output()
{
     ofstream output("C.out");
     forn(t, T)
     {
      output<<"Case #"<<t+1<<": "<<pairsCount[t]<<endl;
     }
     output.close();
}
void calc()
{
     forn(t, T)
     {
      int a = As[t];
      int b = Bs[t];
      
      for(int n=a; n<b; n++)
      {
       int digits = totalDigits(n);
       vector<int> ms;
       for(int shift=1; shift<digits; shift++)
       {
        int m = shifted(n, shift);
        if(inRange(m, a, b))
        {
         if(a<=n && n<m && m<=b && find(ms.begin(), ms.end(), m) == ms.end())
         {
          pairs[t].push_back(make_pair(n, m));
          pairsCount[t]++;  
         }       
        } 
        ms.push_back(m);      
       }       
      }        
     }
}

int main()
{
 input();
 calc();
 output();   
}
