#include<iostream>
#include<string>
#include<fstream>
#include<sstream>
using namespace std;
string reorder(string str)
{
       string str1;
       int n=str.length();
       str1=str[n-1];
       str[n-1]='\0';
       str1+=str;
       return str1;
       }
void split(string &s1,string &s2)
{
     unsigned int i;
     i=s1.find(' ',0);
     s2=s1.substr(i+1);
     s1=s1.substr(0,i);
     }
string tostr(int num)
{
       ostringstream oss;
       oss<<num;
       return oss.str();
       }

int findnum(string str1,string str2)
{
    string rstr;
    int low,high,temp1,temp2,rodr,count=0,n,i;
    low=atoi(str1.c_str());
    high=atoi(str2.c_str());
    temp1=low;
    while(temp1<=high)
    {
                     temp2=temp1;
                     rstr=tostr(temp1);
                     n=rstr.length();
                     for(i=0;i<n;i++)
                     {
                                                   rstr=tostr(temp2);
                                                   if(low/10>9)
                                                   {
                                                   if(temp2/10<10)
                                                   {
                                                                  rstr='0'+rstr;
                                                                  //cout<<rstr<<endl;
                                                                  }
                                                                  }
                                                   rstr=reorder(rstr);
                                                   //cout<<rstr<<endl;
                                                   temp2=atoi(rstr.c_str());
                                                   if(temp2>temp1 && temp2<=high)
                                                   {
                                                                //cout<<temp2<<endl;
                                                                count++;
                                                   }
                                                   }
                                                   temp1++;
                                                   }
    return count;
}   
int main()
{
    int cn;
    string str,str1,str2;
    ifstream file1;
    file1.open("b.in",ios::in);
    getline(file1,str);
    int n=atoi(str.c_str());
    for(int i=0;i<n;i++)
    {
          getline(file1,str1);
          split(str1,str2);
          cn=findnum(str1,str2);
          cout<<"Case #"<<i+1<<": "<<cn<<endl;
          }
          system("pause");
          }  
