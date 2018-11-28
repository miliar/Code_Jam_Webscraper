#include <iostream> 
#include <vector>
#include <string>
#include <string.h>
#include <algorithm> 
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cfloat>
#include <bitset> 

using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()

int main()
{
    int n;
    string cad;
    cin>>n;
    for(int ii=0;ii<n;ii++)
    {
        cin>>cad;
        string dos=cad;
        string ten="";
            int ceros=0;
        next_permutation(all(cad));
        if(cad<=dos)
        {
            
            for(int j=0;j<cad.size();j++)
            {
                if(cad[j]!='0')
                    ten+=cad[j];
                    else
                    ceros++;
            }
            string otro=string(ceros+1,'0');
            ten.insert(1,otro);
                cout<<"Case #"<<ii+1<<": "<<ten<<endl;
        }
        else
            cout<<"Case #"<<ii+1<<": "<<cad<<endl;
    
        
        
    }
return 0;
}
