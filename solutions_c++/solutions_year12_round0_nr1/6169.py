#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>

using namespace std;
string dic = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
    string a,b;
    int n,k,i;
    while(cin>>n)
    {
        getline(cin,b);
        for(k =1 ; k<=n; k++)
        {
            getline(cin,a);
            cout<<"Case #"<<k<<": ";
            for(i = 0 ; i< a.length(); i++)
            {
                if(a[i]!=' ')
                {
                    cout<<dic[a[i]-'a'];
                }
                else
                {
                    cout<<a[i];
                }
            }
            cout<<endl;
        }
    }


return 0;
}
