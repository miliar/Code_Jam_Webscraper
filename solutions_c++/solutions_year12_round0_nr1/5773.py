using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

# define PI 3.14159265
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)

int main()
{
//	freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
     int t;
     char str[200];
     char arr[]="yhesocvxduiglbkrztnwjpfmaq";
     cin>>t;
     cin.ignore();
     for(int j=0;j<t;j++)
     {
        cin.getline(str,200);
        int len=strlen(str);
        cout<<"Case #"<<j+1<<": ";
        for(int i=0;i<len;i++)
        {
                if(str[i]==' ')
                cout<<" ";
                else
                cout<<arr[str[i]-97];
        }
        cout<<endl;
     }


   // int o;cin>>o;

   	return 0;
}
