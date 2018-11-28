#include<fstream>
#include<algorithm>
#include<map>
#include<iostream>
#include<string>
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
ofstream f2out("A2.out");
string word[5005];
bool m[17][28];
int main()
{
    int L,D,N;
    fin>>L>>D>>N;
    for(int i=0;i<D;i++)
    fin>>word[i];
    for(int k=0;k<N;k++)
    {
        string msg;
        fin>>msg;
        int poi=0,s,e;
        for(int i=0;i<msg.size();i++)
        {
           string put="";
           if(msg[i]=='(')
           {
             for(int j=i+1;j<msg.size();j++)
             {
               
               if(msg[j]==')')
               {i=j;break;}
               m[poi][msg[j]-'a']=1;
             }
           }
           else
           m[poi][msg[i]-'a']=1;
           poi++;
        }
        for(int i=0;i<poi;i++)
        {
           for(int j=0;j<26;j++)
           if(m[i][j])f2out<<char(j+'a');
           f2out<<" ";
        }
        f2out<<endl;
        int res=0;
        for(int i=0;i<D;i++)
        {
            int j;
            for(j=0;j<L;j++)
            {
                if(!m[j][word[i][j]-'a'])break;
            }
            if(j==L)res++;
        }
        fout<<"Case #"<<k+1<<": "<<res<<endl;
        for(int i=0;i<poi;i++)
        
           for(int j=0;j<26;j++)
           m[i][j]=0;
    }
    return 0;
}
