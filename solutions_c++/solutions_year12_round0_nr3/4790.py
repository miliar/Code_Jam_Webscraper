#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;

ifstream in("recycled0.in");
ofstream out("recycled0.out");

int main()

{
    string s, t, a, b, n, m;
    int A, B; 
    string temp;
    
    bool flag = false;
    int counter = 1, kase;

getline(in,s);
stringstream ss(s);
ss>>kase;

while(kase--)
{
     if(flag) out<<endl;
     flag = true;
 
      int n=0; 
      getline(in,s);
      stringstream st(s);
      st>>A>>B;
      st.clear();
      stringstream sa, sb;
      sa<<A; sb<<B;
      a = sa.str(); b = sb.str();
      
      for(int i = A; i<B; i++)
  //      for(int j = i+1 ; j<=b; j++)
        {
          stringstream str;
          str<<i;
          temp = str.str();
          temp+=temp; 
          for(int j= 0 ; j<b.size()-1; j++)
          {
              string sub = temp.substr (j+1, b.size());
              int sb = atoi(sub.c_str());
              stringstream cc;
              cc<<sb;
              string test = cc.str();
              
              if(sb<=B && b.size()==cc.str().size()&& sb>i )
              {
                          n++;  
                          //out<<i<<" "<<sub<<endl;      
                                  }    
                  
                  }
                        
                
                } 
                out<<"Case #"<<counter<<": "<<n;
                counter++;
                n=0;

             }
    
    
    }
