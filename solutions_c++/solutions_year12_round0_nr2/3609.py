#include <iostream>
#include <fstream>
#include <vector>
#include <map>
using namespace std;

#define forn(i,n) for(int i=0; i<n; i++)
#define dbg(n) cout<<#n<<": "<<n<<endl;
#define mp make_pair

int getMin(int total)
{
 if(total==0) return 0;
 if(total==1) return 1;
 if(total==2) return 1;
 if(total==3) return 1;
 int n = total/3;
 int a = n;
 int b = n;
 if(a+b+n==total) return n;
 n++; 
 if(a+b+n==total) return n;
 b++;
 if(a+b+n==total) return n; 
}
int getMax(int total)
{
 if(total==0) return 0;
 if(total==1) return 1;
 if(total==2) return 2;
 int n = total/3 + 1;
 int a = n - 2;
 int b = n - 2;
 if(a+b+n==total) return n;
 a++;
 if(a+b+n==total) return n;
 b++;
 if(a+b+n==total) return n;  
 n++;
 if(a+b+n==total) return n;
}

int main()
{
 ifstream input("B.in"); 
 ofstream output("B.out");  
 int T;
 input>>T;
 
 forn(t, T)
 {
  int N,S,p;
  input>>N>>S>>p;
  int answer = 0;
  forn(i, N)
  {
   int ti;
   input>>ti; 
   int max = getMax(ti);
   int min = getMin(ti);
   if(max>=p && min<p)
   {
    if(S>0)
    {
     S--;
     answer++;
    }
   }else if(max>=p && min>=p)
   {
    answer++;      
   }
  }        
  output<<"Case #"<<t+1<<": "<<answer<<endl;
 }
}
