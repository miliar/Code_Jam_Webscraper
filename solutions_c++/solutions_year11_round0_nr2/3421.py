#include <iostream>
#include <vector>
#include <map>
#include <string>

using namespace std;

char find(char a,char b,vector<string> v)
{
    for(int i=0;i<v.size();i++){
        if(v[i][0]==a && v[i][1]==b){
            return v[i][2];
        }
        if(v[i][1]==a && v[i][0]==b){
            return v[i][2];
        }
        
    }
    return 'a';
}

bool find1(char a,char b,vector<string> v)
{
    for(int i=0;i<v.size();i++){
        if(v[i][0]==a && v[i][1]==b){
            return true;
        }
        if(v[i][1]==a && v[i][0]==b){
            return true;
        }
        
    }
    return false;
}

void printString(string s)
{
    if(s.size()==0){
        cout<<"[]"<<endl;
    } else {
        cout<<"[";
        for(int j=0;j<s.size();j++){
            cout<<s[j];
            if(j<s.size()-1){
                cout<<", ";
            }
        }
        cout<<"]"<<endl;
    }
}

int main()
{
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++){
        vector<string> replacement;
        vector<string> removal;
        int n;
        cin>>n;
        for(int i=0;i<n;i++){
            string temp;
            cin>>temp;
            replacement.push_back(temp);
        }
        cin>>n;
        for(int i=0;i<n;i++){
            string temp;
            cin>>temp;
            removal.push_back(temp);
        }
        //cout<<removal.size()<<endl;
        cin>>n;
        string s;
        cin>>s;
        string s1="";
        for(int i=0;i<s.size();i++){
            s1=s1+" ";
            s1[s1.size()-1]=s[i];
        //    cout<<s1<<endl;
            if(s1.size()>1){
                char ch=find(s1[s1.size()-1],s1[s1.size()-2],replacement);
                if(ch!='a'){
                    s1.erase(s1.end()-1,s1.end());
                    s1[s1.size()-1]=ch;
         //           cout<<"replaced to "<<s1<<endl;
                }
            }
            for(int j=0;j<s1.size()-1;j++){
                if(find1(s1[s1.size()-1],s1[j],removal)){
                    s1="";
                    break;
                }
            }
        }
        
        cout<<"Case #"<<ii+1<<": ";
        printString(s1);
    }
    return 0;
}