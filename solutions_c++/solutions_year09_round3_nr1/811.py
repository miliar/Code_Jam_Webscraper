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
map<char, int> basemap;
map<char, int> repmap;

int getBase(string str)
{                  
        int len = sz(str);
        for(int i = 0; i < len; i++)
           basemap[str[i]]++;
           
        return sz(basemap);      
}

unsigned long long convertToTen(string str, int base)
{
      //cout << str <<" "<< base<<endl;
      unsigned long long int ans = 0;
      int len = sz(str);
      unsigned long long bb = 1;
      for(int i = len - 1; i >= 0; i--){
           ans += (str[i] - '0') * bb;
           bb *= base;
           //cout<<endl<<ans<< " " << bb;
      }
      
      return ans;
       
}

int main()
{
    int n;
    cin >> n;
    
    string str, ans;
    for(int i = 1; i <= n; i++){
            cin >> str;
            basemap.clear();
            repmap.clear();
            int base = getBase(str);
            if(base == 1) base = 2;
            repmap[str[0]] = 1;
            int avail = 0;
            for(int j = 1; j < sz(str); j++)
            {
                    if(!present(repmap, str[j])){
                        repmap[str[j]] = avail;                    
                        if(avail == 0) avail = 2;
                        else avail++;
                    }
            }
            ans = "";
            for(int j = 0; j < sz(str); j++)
               ans += ( repmap[str[j]] + '0');
               
            
           
            cout<<"Case #"<<i<<": "<<convertToTen(ans, base);
            //cout<<endl<<ans;
            cout<<endl;
    }
    return 0;    
}
