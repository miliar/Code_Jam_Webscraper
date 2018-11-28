#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream cin("B-large.in");
    ofstream cout("B-large.out");
    
    int n,g,s,p,c,z;
    int v;
    
    cin >> n;
   // cout<<"n = " << n<<endl;
    for (int i=0;i<n;i++)
    {
        c=0;
        cin >> g >> s>>p;
        //cout << "g = " << g<<" s  = " << s<< " p = " <<p<<endl;
        //v = new int[g];
        z = 3*p - 4;
        //cout<<"z = " << z << endl;;
        for (int j =0;j<g;j++)
        {
                 cin>>v;
                 //cout<<  " v = "<<v;
                 if (v ==0)
                 {
                       if (p==0) c++;
                       continue;
                 }
                 if (v==1)
                 {
                      if (p<=1) c++;  
                      continue;  
                 }
                 if (v >= z+2) 
                 {
                       c++;
                       continue;
                    }
                    if (v==z || v==z+1)
                    {
                             if (s>0)
                             {
                                     s--;
                                     c++;
                             }
                             continue;
                    }
                 
        }
        cout << "Case #"<<i+1<<": "<<c<<endl;
        //sort(v,v+g);
        //delete []v;
        
        
    }
    
    
    //fclose(cin);
    //fclose(cout);
    cin.close();
    cout.close();
    return 1;
}
