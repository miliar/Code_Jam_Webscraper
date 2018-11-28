#include<cstdio>
#include<fstream>
#include<iostream>
#include<vector>
#include<cstring>
#include<map>
#define MAX 101
using namespace std;
map<string,bool> MAP;
int main()
{
    ifstream in;
    in.open("in.txt",ios::in);
    FILE *out;
    out=fopen("out-large.txt","w");
    int T;
    in>>T;
    for(int cases=1;cases<=T;cases++)
    {
        int N,M;
        MAP.clear();
        in>>N>>M;
        //take the already existing ones
        string s;
        while(N--)
        {
            in>>s;
            int l=s.length();
            string dir="/";
            for(int i=1;i<l;)
            {
                //find next /
                while(i<l && s[i]!='/')
                {
                    dir=dir+s[i];
                    i++;
                }
                //push into 0
                if(MAP[dir]==0)
                {
                    MAP[dir]=1;
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
                //find next /
                while(i<l && s[i]!='/')
                {
                    dir=dir+s[i];
                    i++;
                }
                //push into 0
                if(MAP[dir]==0)
                {
                    MAP[dir]=1;
                    ans++;
                }
                dir=dir+s[i++];
            }
        }
        fprintf(out,"Case #%d: %d\n",cases,ans);
    }
}
