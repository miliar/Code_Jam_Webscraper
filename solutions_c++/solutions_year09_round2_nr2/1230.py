#include<iostream>
#include<cmath>
#include<fstream>
#include<iomanip>
using namespace std;

string change(int n)
{
       string s="";
       while(n!=0)
       {
                  int rem=n%10;
                  n=n/10;
                  char c=rem+48;
                  s=c+s;
       }
       return s;
}
int check(string s,string t)
{
    int signal=0;
    for(int i=0;s[i]!='\0';i++)
    {
            signal=0;
            for(int j=0;t[j]!='\0';j++)
            {
                    if(s[i]==t[j])
                    {signal=1;t[j]=' ';
                    break;}
            }
            if(signal==0)
            break;
    }
    return signal;
}

int main()
{
    ifstream in;
    in.open("input.txt");
    ofstream out;
    out.open("output.txt");
    int n,t;
    in>>t;
    for(int prob=0;prob<t;prob++)
    {
            string s,t;
            in>>s;
            int sig=0;
            if(s[1]!='\0'){
            for(int i=1;s[i]!='\0';i++)
            {
                    sig=0;
                    if(s[i-1]>=s[i])
                    {
                                   sig=1;
                    }
                    else
                    break;
            }
            cout<<s<<endl;
            int signal=0;
            t="";
            cout<<t<<endl;
            if(sig==0){t=s;
            while(signal!=1)
            {
                            int i=0;
                            for(i=0;t[i]!='\0';i++);
                            i--;
                            
                            //cout<<t<<endl;
                            for(int j=i;j>=0;j--)
                            {
                                             if(t[j]=='9')
                                             t[j]='0';
                                             else
                                             {
                                                 int g=t[j];
                                                 g++;
                                                 char te=g;
                                                 t[j]=te;
                                                 break;
                                             }
                            }
                                             
                                             
                            
                            signal=check(s,t);
            }
            }
            else
            {
                int i=0,k;
                t="";
                for(i=0;s[i]!='\0';i++);
                i--;
                for(k=i;k>=0;k--)
                if(s[k]!='0')
                break;
                t=s[k];
                t=t+'0';
                //cout<<t<<endl;
                //system("pause");
                for(int j=0;j<i-k;j++)
                {t=t+'0';
                }
                
                for(int j=k-1;j>=0;j--)
                t=t+s[j];
                
            }
            }
            else
            {t=s[0];
            t=t+'0';}
            
            
            
            cout<<"Case #"<<prob+1<<": "<<t<<endl;
            out<<"Case #"<<prob+1<<": "<<t<<endl;;
    }
    
    in.close();
    out.close();
    system("pause");
    return 0;
}
