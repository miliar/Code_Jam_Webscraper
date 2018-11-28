
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> chars;
int Size = 0;

void parse(string str) {
    string newstr="";
    int i=0;
    Size=0;
    chars.clear();
    while(true)

    {
        if(i>=str.size()) break;
        if (str[i] == '(') {
            i++;
            while (str[i] != ')') {
                newstr.push_back(str[i]);
                i++;
            }
            i++;
            Size++;
            chars.push_back(newstr);
            newstr="";
        }
        if (str[i] != '(')
        {
            newstr.push_back(str[i]);
            Size++;
            chars.push_back(newstr);
            newstr="";
            i++;
        }      
    }
}
bool Contain(char c,string str2)
{
    for(int i=0;i<str2.size();i++)
    {
        if(c==str2[i]) return true;
    }
    return false;
}

int main() {
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int L, D, N,count=0,l;
    bool Invalid;
    cin >> L >> D >> N;
    vector<string> In;
    string temp;
    
    
    
    for (int i = 0; i < D; i++) {
        cin >> temp;
        In.push_back(temp);
    }
    for (int i = 0; i < N; i++) {

        cin >> temp;
        parse(temp);

        for (int j = 0; j < D; j++) {
            Invalid = false;
          //  vector<string> selected;
            for(l=0;l<In[j].size();l++)
            {
                
                    if(!Contain(In[j][l],chars[l]))
                    {
                        Invalid=true;
                        break;
                    }
            }
            if(!Invalid) count++;
            
        }
        cout<<"Case #"<<i+1<<": "<<count<<endl;
        count=0;
        

    }
    




    return 0;
}
