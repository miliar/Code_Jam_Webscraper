#include<iostream>
#include<stdio.h>
#define SIZE 500
using namespace std;

void convert(char *str,char *cvt)
{
int i;
char ref[30] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
for(i=0;str[i]!='\0';i++)
if(str[i] == ' ') cvt[i] = ' ';
else cvt[i] = ref[(str[i] - 97)];
cvt[i] = '\0';
}

int main()
{
    int t;
    char str[SIZE],cvt[SIZE];
    cin>>t;
    cin.getline(str,SIZE);
    for(int tc=0;tc<t;tc++)
    {
        cin.getline(str,SIZE);
        convert(str,cvt);
        cout<<"Case #"<<tc+1<<':'<<' '<<cvt<<'\n';
    }
    return 0;
}