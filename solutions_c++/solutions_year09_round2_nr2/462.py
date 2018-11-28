#include <iostream>
#include <string>
using namespace std;
int main()
{
    int n;
    cin>>n;
    string str;
    getline(cin,str);
    
    for (int i=0; i<n; ++i){
        getline(cin,str);
        int j;
        for (j=str.length()-1;j>=1;--j)
            if (str[j]>str[j-1])
                break;
        if (j==0)
        {
            str = "0"+str;
            j = 1;
        }
        int l = str.length();
        string t = str;
        for (int k = j;k<str.length();++k)
            t[k] = str[j + l - k -1];
        for (int k = j;k<str.length();++k)
            if (t[k]>t[j-1])
            {
                char tmp = t[k];
                t[k] = t[j-1];
                t[j-1] = tmp;
                break;
            }
        cout<<"Case #"<<i+1<<": "<<t<<endl;
    }
    
}
