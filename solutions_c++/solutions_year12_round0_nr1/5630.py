#include<iostream>
#include<string>
#include<stdio.h>

using namespace std;

int main()
{
    string orig="abcdefghijklmnopqrstuvwxyz";
    string replace ="yhesocvxduiglbkrztnwjpfmaq";
    char arr[26];
    char replace_arr[26];
    for(int i =0;i<26;i++)
    {
            arr[i] =orig[i];
            replace_arr[i]=replace[i]; 
    }
    /*for(int i =0;i<26;i++)
    {
            cout<<arr[i];
    }
    cout<<"\n";
    for(int i =0;i<26;i++)
    {
            cout<<replace_arr[i];
    }*/
    
    int n;
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    char ch;
    string str;
    char conv[200];
    cin>>n;
    scanf("%d",&ch);
    for(int i=0;i<n;i++)
    {
            getline(cin,str);
            int j;
            for(j=0;j<str.length();j++)
            {
                    char ch = char(str[j]);
                    int index = ch -97;
                    char replace_char = replace_arr[index];
                    if(index>=0)
                    conv[j] = replace_char;
                    else
                    conv[j] = ' ';
            }
            conv[j++]='\0';
            cout<<"Case #"<<i+1<<": "<<conv<<"\n";
    }
}
