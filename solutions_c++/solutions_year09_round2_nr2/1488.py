#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    string s,s1;
    int ntc,cnt=1,i;
    cin>>ntc;
    while(ntc--)
    {
                cin>>s;
                s1 = s; 
                cout<<"Case #"<<cnt++<<": ";
                next_permutation(s.begin(),s.end());
                if(s<=s1) 
                {
                    /*cout<<s1[0]<<"0";
                    for(i=1;s1[i];i++)
                    cout<<s1[i];       */
                    s =   "0"+s;
                    while(s[0]=='0') next_permutation(s.begin(),s.end());
                }
               //else
                cout<<s;
                cout<<endl;
    }
    return 0;
}
