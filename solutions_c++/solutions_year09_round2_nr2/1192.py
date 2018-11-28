/*
OS: Microsoft Windows XP Professional
Compiler: Bloodshed Dev-C++ 4.9.9.2
*/
#include <iostream>
#include <string>
#include <stdlib.h>
using namespace std;
int cmp(const void *elem1, const void *elem2)
{
    return *((int*)elem1)-*((int*)elem2);
}
int main()
{
    freopen("nn.in", "r", stdin);
    freopen("nn.out", "w", stdout);
    int t;
    string num;
    int k, i, j;
    bool key;
    char tmp;
    int s[30];
    cin>>t;
    for (k=1; k<=t; k++)
    {
        cin>>num;
        key=false;
        for (i=num.length()-2; i>=0; i--)
        {
            if (num[i]<num[i+1])
            {
                for (j=i+1; j<num.length(); j++)
                    s[j-(i+1)]=num[j]-'0';
                qsort(s, num.length()-(i+1), sizeof(int), cmp);
                for (j=i+1; j<num.length(); j++)
                    num[j]=s[j-(i+1)]+'0';
                for (j=i+1; j<num.length(); j++)
                {
                    if (num[i]<num[j])
                    {
                        tmp=num[i];
                        num[i]=num[j];
                        num[j]=tmp;
                        break;
                    }
                }
                key=true;
                break;
            }
        }
        if (key)
        {
            cout<<"Case #"<<k<<": "<<num<<endl;
        }
        else
        {
            for (i=0; i<num.length(); i++)
                s[i]=num[i]-'0';
            qsort(s, num.length(), sizeof(int), cmp);
            cout<<"Case #"<<k<<": ";
            for (i=0; i<num.length(); i++)
            {
                if (s[i]>0)
                {
                    cout<<s[i];
                    for (j=1; j<=i+1; j++)
                        cout<<0;
                    for (j=i+1; j<num.length(); j++)
                        cout<<s[j];
                    cout<<endl;
                    break;
                }
            }
        }
    }
    fclose(stdin);
    fclose(stdout);   
    return 0;
}
