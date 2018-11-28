#include <iostream>
#include <sstream>

using namespace std;

bool func(int a,int b)
{
     stringstream ss1,ss2;
     string s1,s2;
     ss1 << a;
     ss2 << b;
     s1=ss1.str();
     s2=ss2.str();
     s2=s2+s2;
     if(s2.find(s1)!=string::npos)
     {
                                  return true;
     }
     return false;
}

int main()
{
    int t;
    cin >> t;
    int a,b;
    for(int i=0; i<t; i++)
    {
            cin >> a >> b;
            int ans=0;
            for(int j=a; j<=b; j++)
            {
                    for(int k=j+1; k<=b; k++)
                    {
                            if(func(j,k))
                            {
                                        ans++;
                            }
                    }
            }
            cout << "Case #" << i+1 << ": " << ans << endl;
    }
}
