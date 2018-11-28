#include<cstdio>
#include<fstream>
#include<iostream>
#include<vector>
#include<cstring>
#include<map>
#define MAX 101
using namespace std;
map<string,bool> mapme;
int main()
{
    ifstream in;
    in.open("in.txt",ios::in);
    FILE *out;
    out=fopen("out.txt","w");
    int T;
    in>>T;
    for(int cases=1;cases<=T;cases++)
    {
        int N,M;
        mapme.clear();
        in>>N>>M;
        string s;
        while(N--)
        {
            in>>s;
            int l=s.length();
            string dir="/";
            for(int i=1;i<l;)
            {
                while(i<l && s[i]!='/')
                {
                    dir=dir+s[i];
                    i++;
                }
                if(mapme[dir]==0)
                {
                    mapme[dir]=1;
                }
                dir=dir+s[i++];
            }
        }
        int ans=0;
        while(M--)
        {
            in>>s;
            int l=s.length();
            string dir="/";
            for(int i=1;i<l;)
            {
                while(i<l && s[i]!='/')
                {
                    dir=dir+s[i];
                    i++;
                }
                if(mapme[dir]==0)
                {
                    mapme[dir]=1;
                    ans++;
                }
                dir=dir+s[i++];
            }
        }
        fprintf(out,"Case #%d: %d\n",cases,ans);
    }
}
