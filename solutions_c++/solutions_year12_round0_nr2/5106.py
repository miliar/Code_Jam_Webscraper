#include<vector>
#include<algorithm>
#include<cstdio>
#include<iostream>
#include<string>
#include<cstdlib>
#include<sstream>
using namespace std;

string convertInt(int number)
{
   std::stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}


int main()
{
    int T,i,j,N,S,p,count,t;
    string ans="";
    char temp[3];
    cin>>T;
    for(i=0;i<T;++i)
    {
        count=0;
        cin>>temp;
        N=atoi(temp);
        cin>>temp;
        S=atoi(temp);
        cin>>temp;
        p=atoi(temp);
        for(j=0;j<N;++j)
        {
            cin>>temp;
            t=atoi(temp);
            switch(t%3)
            {
                case 0:
                if(p<=t/3)
                ++count;
                else if(S&&(p==t/3+1)&&t)
                {
                    ++count;
                    --S;
                }
                break;
                case 1:
                if(p<=t/3+1)
                    ++count;
                break;
                case 2:
                if(p<=t/3+1)
                    ++count;
                else if(S&&(p==t/3+2))
                {
                    --S;
                    ++count;
                }
                break;
            }
        }
        ans+="Case #";
        ans+=convertInt(i+1);
        ans+=": ";
        ans+=convertInt(count);
        ans+="\n";
    }
    system("cls");
    cout<<ans;
    return 0;
}
