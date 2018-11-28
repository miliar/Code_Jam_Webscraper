#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

int main(){
    int n;
    string line;
    getline(cin, line);
    istringstream iss2(line);
    iss2>>n;
    for(int i=0;i<n;i++)
    {
        int num;
        string line;
        getline(cin, line);
        istringstream iss(line);
        iss>>num;
        map<char,char> join[26];
        set<char> kill[26];
        for(int j=0;j<num;j++){
                string str;
                iss>>str;
                char a=str[0];
                char b=str[1];
                char c=str[2];
                join[(int)a - 65][b]=c;
                join[(int)b - 65][a]=c;
        }
        iss>>num;
        for(int j=0;j<num;j++){
                string str;
                iss>>str;
                char a=str[0];
                char b=str[1];
                kill[(int)a - 65].insert(b);
                kill[(int)b - 65].insert(a);
        }
        
        int exist[26];
        for(int q=0;q<26;q++) exist[q]=0;
        iss>>num;
        string str;
        iss>>str;
        vector<char> work;
        for(int j=0;j<num;j++){
                char c=str[j];
                int know=work.size();
                while(work.size()>0){
                        char d=work[work.size()-1];
                        if(join[(int)c - 65].count(d)>0)
                        {                    
                                  exist[(int)d -65] -=1;    
                                  work.pop_back();
                                  c=join[(int)c -65][d];
                        }
                        else
                        {
                                  break;
                        }
                }
                int kl=0;
                if(know==work.size()&&know>0)
                {
                        for (set<char>::iterator it=kill[(int)c-65].begin() ; it != kill[(int)c-65].end(); it++ )
                        {
                                if(exist[(int)(*it)-65]>0)
                                {
                                     kl=1;
                                     for(int l=0;l<work.size();l++) exist[(int) work[l] -65]=0;
                                     work.clear();
                                     break;
                                }
                        }
                }
                if(kl==0) 
                {
                     work.push_back(c);
                     exist[(int) c - 65]++;
                }
        }
        
        cout<<"Case #"<<i+1<<": [";
        for(int j=0;j<work.size();j++)
        {
                cout<<work[j];
                if(j!=work.size()-1) cout<<", ";
        }
        cout<<"]"<<endl;
    }
    return 0;
}
