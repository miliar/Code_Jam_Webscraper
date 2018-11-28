#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>

using namespace std;

ifstream in("tongues0.in");
ofstream out("tongues1.out");

int main()
{

string s;
string temp;

//mapping
string map = "yhesocvxduiglbkrztnwjpfmaq";

bool flag  =false;
int counter =1;

getline(in,s);

while(!in.eof())
{
  
if(flag) out<<endl;
flag = true;
              
getline(in,s);

for(int i = 0; i<s.size(); i++)
{
        
        if((int)(s[i]-'a')>=0 && (int)(s[i]-'a')<= 25)
        {
          temp+=map[(int)(s[i]-'a')];
        }
        else temp+=s[i];
        
        }

        
        out<<"Case #"<<counter<<": "<<temp;
        temp.clear();
        counter++;
                        }

    
    }
