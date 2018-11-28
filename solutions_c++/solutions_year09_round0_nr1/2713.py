# include <iostream>
# include <vector>
# include <fstream>
# include <algorithm>
# include <map>
# include <queue>

using namespace std;

ifstream in("A-large.in");
ofstream out("out.txt");

int main()
{
    int L,D,N,cas=0;
    in>>L>>D>>N;
    
    vector<string> dict;
    string s;
    
    for(int i = 0;i<D;i++)
    {
        in>>s;
        dict.push_back(s);        
    }
    
    while(N--){

    in>>s;
    
    string str;
    
    int ret = 0;
    for(int i = 0;i<dict.size();i++)
    {
        int f = 0,k=0;
        for(int j = 0;j<s.size();)
        {
            if(s[j]=='(')   {j++;f=1;continue;}
            if(s[j]==')')   {j++;f=0;continue;}
            
            if(f){    
             while(s[j]!=dict[i][k] && j<s.size()){
                     j++;
                    }
                if(j<s.size() && s[j]==dict[i][k]){
                    while(s[j]!=')')    j++;
                    k++;
                    continue;   
                }    
                else if(j<s.size() && s[j]==')')  {j++;f=0;continue;}
            }
            else if(s[j]!=dict[i][k])   break;
            else j++,k++;
        }    
        
        if(k == dict[i].size()) {ret++;/*out<<dict[i]<<endl;*/}
    }
            
    out<<"Case #"<<++cas<<": "<<ret<<endl;
        
    }
    
    return 0;
}
 
