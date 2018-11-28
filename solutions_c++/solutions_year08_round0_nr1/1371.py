#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;

int main()
{
    int cases;
    cin >> cases;
    int cnt = 1;
    int switches = 0;
    int nose, q;
    map<string, int> se; 
    char arr[100];
    string s;
    int counter;
    int ans;
    while(cases--)
    {
        cin >> nose;
        //cout << nose;
        se.clear();
        getline(cin, s, '\n');
        for(int i = 0; i < nose; i++)
        {
                getline(cin, s, '\n');
                se[s] = 0;                
                //cout<<endl<<s;                
        }
        
        cin >> q;
        getline(cin, s, '\n');
        counter = 0;
        ans = 0;
        for(int i = 0; i < q; i++)
        {
            //cin >> s;
            getline(cin, s, '\n');
            se[s]++;
            if(se[s] == 1) counter++; 
            //cout<<endl<<s<<" : ";
            //tr(se, itr) cout<<endl<<itr->first<<" "<<itr->second; 
            //cout<<endl<<"Counter : "<<counter;        
            if(counter == nose)         
            {
                tr(se, itr) itr->second = 0;
                counter = 0;
                //cout<<"after reset : ";
                //tr(se, itr) cout<<endl<<itr->first<<" "<<itr->second; 
                ans++;
                se[s]++;
                counter++;                 
            }
        }
        cout<<"Case #"<<cnt<<": "<<ans<<endl;
        cnt++;
        
        //tr(se, itr) cout<<endl<<itr->first<<" "<<itr->second;
            
        
    }
    //cin >> arr;
    return 0;
}

