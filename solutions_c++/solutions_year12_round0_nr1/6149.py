#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int main()
{
    int cases;
    
    ifstream ifs("A-small-attempt2.in");
    ofstream out("Output.in");
    
    ifs >> cases;
    
    string letters = "abcdefghijklmnopqrstuvwxyz";
    string dict = "yhesocvxduiglbkrztnwjpfmaq";
    
    string t,result="";
    getline(ifs,t);
    for(int i=0;i<cases;i++)
    {
            getline(ifs,t);
            result = "";
            for(int j=0;j<t.length();j++)
            {
                    if(t[j]!=' ')
                      result += dict[(int)(t[j])-97];
                    else
                      result += " ";
                    
            }
       out <<"Case #"<<(i+1)<<": " <<result <<endl;
    }
    
    
    system("pause");
    return 0;
}
