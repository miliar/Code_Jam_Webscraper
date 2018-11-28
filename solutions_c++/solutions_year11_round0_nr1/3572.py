#include<iostream>
#include <string >
#include <sstream>
#include <vector>
#include <stdlib.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,k=1;
    cin >> t>>ws;
    string s;
    while(t--)
    {
        getline(cin,s);
        stringstream st;
        int n ;
        st << s ;
        st >> n;
        vector <pair<char,int> > arr(n);
        for(int i=0;i<n;i++)
        {
                st >> arr[i].first;st >> arr[i].second ;
        }
        int p1=1,p2=1,t1=0,t2=0,t=0;
        for(int i=0;i<n;i++)
        {
                if(arr[i].first=='O')
                {

                    if ( abs(arr[i].second-p1)+t1 < t2 ) { t=t1=t2+1 ;  }
                    else t=t1+=abs(arr[i].second-p1)+1 ;
                    p1 = arr[i].second;
                }
                else
                {
                    if ( abs(arr[i].second-p2)+t2 < t1 ) { t=t2=t1+1 ; }
                    else t=t2+=abs(arr[i].second-p2)+1 ;
                    p2 = arr[i].second;
                }
        }
        cout << "Case #"<<k++<<": "<<t<< endl;
    }
}
