#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	char arr[110];
    string str1="qz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string str2="zq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    int t=0,i=0;
    cin>>t;
    for(i=0;i<=t;i++)
    {
        cin.getline(arr,110);
        if(i==0)
        continue;
        int j=0,k=0,len=0,len2;
        len=strlen(arr);
        len2=str1.length();
        for(j=0;j<len;j++)
        {
            for(k=0;k<len2;k++)
            {
                if(arr[j]==str1[k])
                {
                    arr[j]=str2[k];
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
