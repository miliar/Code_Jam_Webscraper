#include <iostream>
#include <vector>
#include <string>
#include <fstream>


using namespace std;

string answ;

void f(vector<string> comb, vector<string> op, string str)
{
    int t,tt;
    int q,a;
    int k,m,r;
    int i;
    
    for(t=0;t<str.length()-1;t++)
    {
        i=0;
        if(str[t]=='-') continue;
        
        for(tt=0;tt<comb.size();tt++)
        {
            if(comb[tt][0]==str[t])
            {        
                for(q=1;t+q<str.length();q++)
                {
                    if(str[t+q]=='-') continue;
                    else
                    {
                        if(comb[tt][1]==str[t+q])
                        {
                            str[t]=comb[tt][2];
                            str[t+q]='-';
                            i=1;
                            for(a=1;t-a>-1;a++)
                            {
                                if(str[t-a]!='-')
                                {
                                    t=t-a-1;
                                    break;
                                }
                            }
                        }
                        break;
                    }
                }
            }
        }
        
   if(i==0)
   {     
        for(q=1;t+q<str.length();q++)
        {
            if(str[t+q]=='-') continue;
            else break;
        }
       for(k=0;k<t+q+1;k++)
       {
            if(str[k]=='-') continue;
            for(tt=0;tt<op.size();tt++)
            {
                if(op[tt][0]==str[k])
                {
                    for(m=1;k+m<t+q+1;m++)
                    {
                        if(str[k+m]==op[tt][1])
                        {
                            for(r=0;r<=k+m;r++)
                            {
                                str[r]='-';
                            }
                            break;
                        }
                    }
                }
            }
       } 
   }    
        
        
    }
  //  cout<<str<<endl;
    
    answ="";
    
    for(t=0;t<str.length();t++)
    {
        if(str[t]!='-') answ+=str[t];
    }
 //   cout<<answ<<endl;
}


int main()
{
    int T,C,D,N;
    ifstream in("B-large.in");
    ofstream out("out.out");
    
    in>>T;
    string str;
    char ch;
    int t,tt,u;
    for(t=0;t<T;t++)
    {
        in>>C;
        
        vector<string> comb;
        vector<string> op;
       
        for(tt=0;tt<C;tt++)
        {
            str="";
            in>>str;
            comb.push_back(str);
            ch=str[0];
            str[0]=str[1];
            str[1]=ch;
            comb.push_back(str); 
        }
        
        in>>D;
        
        for(tt=0;tt<D;tt++)
        {
            str="";
            in>>str;
            op.push_back(str);
            ch=str[0];
            str[0]=str[1];
            str[1]=ch;
            op.push_back(str); 
        }
        
        in>>N;
        str="";
        in>>str;
        
        f(comb,op,str);
        
        out<<"Case #"<<t+1<<": [";
        
        for(u=0;u<answ.length();u++) 
        {
            out<<answ[u];
            if(u<answ.length()-1) out<<", ";
        }
        out<<"]"<<endl;
    }
    
   // system("PAUSE");
}
