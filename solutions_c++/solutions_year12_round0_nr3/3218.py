#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <list>
#include <utility>
#include <string>
#include <sstream>

class Found{};

using namespace std;

int toInt(string s){istringstream sin(s); int t; sin>>t; return t;}
string toStr(int t){stringstream sin; sin<<t; string s; sin>>s; return s;}

void shift(string& str)
{
    if(str.empty()) 
        return;
    char c=str[0];
    for(int i=0; i<str.size()-1; i++)
        str[i]=str[i+1];
    str.back()=c;
}

int main()
{
    ifstream in("C:\\Users\\Olexandr\\Desktop\\C-small-attempt0.in");
    ofstream out("C:\\Users\\Olexandr\\Desktop\\output.txt");
    int T;
    in>>T;


    for(int t=0; t<T; t++)
    {
        out<<"Case #"<<(t+1)<<": ";
        //code here:
        int A,B;
        in>>A>>B;
        int result=0;
        for(int i=A; i<=B; i++)
        {
            string s=toStr(i);
            int si;
            do
            {
                shift(s);
                si=toInt(s);
                if(si!=i &&  !s.empty() && s[0]!='0' && si>=A && si<=B)
                    result++;
            }while(si!=i);
        }
        out<<result/2<<endl;
    }
    //system("pause>nul");
    return 0;
}