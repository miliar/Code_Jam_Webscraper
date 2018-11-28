#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>

using namespace std;

string k="welcome to code jam";

int main()
{
    int n;
    freopen("inputb.txt","r",stdin);
    scanf("%d\n",&n);
    freopen("output.txt","w",stdout);
    for(int asd=0;asd<n;asd++)
    {
        char xx[510];
        cin.getline(xx,510);
        string x=xx;
        int s[510][19]={0};   
        for(int i=x.size()-1;i>=0;i--)
        {
            for(int j=k.size()-1;j>=0;j--)
            {
                if(x[i]==k[j])
                {
                    if(j==18)
                        s[i][j]=1;
                    else
                    for(int ij=i+1;ij<x.size();ij++)
                        if(x[ij]==k[j+1])
                            s[i][j]+=s[ij][j+1],s[i][j]%=10000;
                }   
            }   
        }
        int res=0;
        for(int i=0;i<x.size();i++)
            res+=s[i][0]%10000,res%=10000;
        printf("Case #%d: ",asd+1);
        if(res<1000)
            printf("0");
        if(res<100)
            printf("0");
        if(res<10)
            printf("0");
        printf("%d\n",res);
    }
    return 0;   
}
