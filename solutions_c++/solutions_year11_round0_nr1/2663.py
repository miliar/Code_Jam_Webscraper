#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <cstdlib>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <stack>
#include <set>
#include <functional>
#include <map>
#define eps 1e-3
using namespace std;


int main ()
{
    freopen ("A-large.in","r",stdin);
    freopen ("out.txt","w",stdout);
    
    int T;
    while (cin>>T)
    {
        for (int Case = 1; Case<=T; Case++)
        {
            int N;
            cin>>N;
            int Pos_O=1,Pos_B=1;
            int Time = 0;
            int Time_O=0,Time_B=0;
            for (int i=0; i<N; i++)
            {
                char Rob;
                int Pos;
                cin>>Rob>>Pos;
                
                //cout<<Time_O<<" "<<Time_B<<endl;
                
                if (Rob=='O')
                {
                    Time= max(Time_O+abs(Pos_O-Pos)+1,Time_B+1);
                    Time_O = Time;
                    Pos_O = Pos;
                }    
                else
                {
                    Time= max(Time_B+abs(Pos_B-Pos)+1,Time_O+1);
                    Time_B = Time;
                    Pos_B = Pos;    
                }
               
            }    
            cout<<"Case #"<<Case<<": "<<Time<<endl;
        }    
    }
    
    
    
    return 0;
}



