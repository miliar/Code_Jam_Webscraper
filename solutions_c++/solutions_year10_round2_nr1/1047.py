#include<iostream>
#include<vector>
#include<queue>
using namespace std;
struct node{
string name;
vector<node> li;
int insert(queue<string> tkn){
    if(tkn.size() == 0)
    return 0;
    string first=tkn.front();
    tkn.pop();
    int ind=-1;
    for(int i=0;i<li.size();i++){
        if(li[i].name == first)
                {
                                ind=i;
                                break;
                }
    }
    int c=0;
    if(ind == -1)
     {
          node temp;
          temp.name=first;
          li.push_back(temp);
          ind=li.size()-1;
          c++;
     }
     return c+li[ind].insert(tkn);
     
}
};
queue<string> getTokens(string str){
    queue<string> ret;
    string temp="";
    for(int i=1;i<str.size();i++){
        if(str[i]=='/'){
                ret.push(temp);
                temp="";
        }
        else
        temp+=str[i];
    }
    ret.push(temp);
    return ret;
}

int main(){
int t;
cin>>t;
for(int p=1;p<=t;p++){
    int n,m;
    cin>>n>>m;
    node root;
    root.name="/";
    int nc=0,mc=0;
    for(int i=0;i<n;i++){
        string s;
        cin>>s;
        queue<string> tokens=getTokens(s);
        nc+=root.insert(tokens);
    }
    for(int i=0;i<m;i++){
        string s;
        cin>>s;
        queue<string> tokens=getTokens(s);
        mc+=root.insert(tokens);
    }
    cout<<"Case #"<<p<<": "<<mc<<"\n";
}
}
