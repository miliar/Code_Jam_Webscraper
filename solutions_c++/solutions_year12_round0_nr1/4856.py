#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    string s="qz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string r="zq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    int t=0,i=0;
    cin>>t;
    for(i=0;i<=t;i++)
    {
        char arr[110];
        cin.getline(arr,110);
        if(i==0)
        continue;
        int j=0,k=0,len=0;
        len=strlen(arr);
        for(j=0;j<len;j++)
        {
            for(k=0;k<s.length();k++)
            {
                if(arr[j]==s[k])
                {
                    arr[j]=r[k];
                    break;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<arr;
        if(i!=t)
        cout<<endl;
    }
    return 0;
}
