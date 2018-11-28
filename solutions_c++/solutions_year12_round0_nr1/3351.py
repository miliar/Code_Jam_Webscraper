#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main ()
{
    freopen("A-small-attempt2.in","r",stdin);   
    freopen("A-small-attempt2.out","w",stdout);
    
    string goog = "qzejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string eng = "zqour language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    int t;
    cin>>t;
    string input;
    string output;
    int googLen = goog.length();
    getline (cin,input); //Gets the line containing t, which is now unnecessary
    for (int i=1;i<=t;++i)
    {
        cout<<"Case #"<<i<<": ";
        getline (cin,input);
        int len = input.length();
        for (int j=0;j<len;j++)
        {
            char c = input[j];
            for (int k=0;k<googLen;k++)
            {
                if (c==goog[k])
                {
                   c = eng[k];
                   break;               
                }    
            } 
            
            cout<<c;  
        }
        cout<<"\n";
    }
    return 0;
}
