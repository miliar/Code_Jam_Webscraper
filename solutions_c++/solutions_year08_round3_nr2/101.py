#include <iostream>
#include <fstream>
using namespace std;
#include "string.h"

__int64 StrToNum(string s)
{
    __int64 k=0;
    for (int i=0;i<strlen(s.c_str());i++)
        k=k*10+(int)(s[i]-'0');
    return k;
}

string AddSign(string s, __int64 sign)
{
     int t,i=1;
     string ss(s);
     while (sign!=0)
     {
         t=sign%3;
         sign=sign/3;
         if (t==1){
             ss.insert(i,1,'+');
             i++;
         }
         else if (t==2){
             ss.insert(i,1,'-');
             i++;
         }
         i++;
     }
     return ss;
}

int parse7(string s, __int64 j)
{
     int t,q=0;
     int sign=1;
     int begin=0,value=0;
     string ss(s);
     while (j!=0)
     {
         t=j%3;
         j=j/3;
         if (t>0)
         {
             value+=sign*StrToNum(s.substr(begin,q-begin+1))%7;
             begin=q+1;
             sign=((t==1)?1:-1);   
         }
         q++;
     }
     value+=sign*StrToNum(s.substr(begin,strlen(s.c_str())-begin))%7;
     return value;
}


__int64 power3(int a)
{
    __int64 q=1;
    for (int i=0;i<a;i++)
        q*=3;
    return q;
}

int main()
{
    int n;
    string s;
    int len;
    __int64 total; 
    __int64 tmp;
    __int64 ret;
    ifstream fin("input.txt");
    ofstream fout("output2.txt");
    fin>>n;
    for (int i=1;i<=n;i++)
    {
        ret=0;
        fin>>s;
        len=strlen(s.c_str());
        total=power3(len-1);
        for (int j=0;j<total;j++)
        {
           
            int jj=j,t,q=0,w=0,sign=1,w3=0;
            while (jj>0)
            {
                t=jj%3;  
                jj=jj/3;
                w3+=sign*(int)(s[q]-'0');
                if (t>0) 
                {
                    w+=sign*(int)(s[q]-'0');
                    sign=((t==1)?1:-1);
                }
                q++;
            }
            w+=sign*(int)(s[len-1]-'0');
//            cout<<"w="<<w<<endl;
            if (w%2==0||w%5==0) {ret++; continue;}
            for (int qq=q;qq<len;qq++) w3+=sign*(int)(s[qq]-'0');
            if (w3%3==0) {ret++; continue;}
            
            tmp = parse7(s,j);
            if (tmp%7==0) 
            {
//                cout<<AddSign(s,j)<<"="<<tmp<<endl;
                ret++;
            }
        }
    //    cout<<"Case #"<<i<<": "<<ret<<endl;
        fout<<"Case #"<<i<<": "<<ret<<endl;
    }
    system("pause");
    return 0;
}

