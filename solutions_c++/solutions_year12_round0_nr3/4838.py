#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;
ofstream out; 

bool are_recy_pairs(int aa, int bb)
{
     string s1, s2; 
     stringstream ss; 
     ss << aa;
     ss >> s1;
    
     for(int i=0; i<s1.length(); i++)
     {
         string temp =  s1.substr(i,s1.length()-i) + s1.substr(0,i);
         stringstream sss; 
         sss << temp;
         int t;
         sss >> t;
        
         if(bb == t)
           return true;
     }
return false;
}

int rep(int A, int B)
{
 //out<<A<<"$$$"<<B<<endl;
 int cnt = 0;
 for(int i=A; i<=B; i++)
  for(int j=i+1; j<=B; j++)
   if(are_recy_pairs(i, j))
    cnt++;
   
 return cnt;   
}

int main()
{
    ifstream cinn; cinn.open("C-small-attempt1.in");
    out.open("C-small-attempt1.out");
    int cas = 1, A, B;
    int n;
    
    cin>>n;
    
    while(cas<=n)
    {
              cin >> A >> B;
              
              if(cas==n)
               cout<<"Case #"<<cas++<<": "<<rep(A,B);
              else
               cout<<"Case #"<<cas++<<": "<<rep(A,B)<<endl;
    }
    
    system("pause");
    return 0;                  
}
