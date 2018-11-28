#include <cstdio>
#include <cstring>
#include <cctype>
#include <map>
#include <sstream>
#include <iostream>
#include <string>

using namespace std;

struct node{
    string feature;
    double w;
}tree[100005];

char buff[505];

void parse(int n, istringstream &in){
    string tizq,tder;
    tree[n].feature="";
    in>>tizq;
    in>>tree[n].w;
    in>>tder;
    //cout<<n<<" "<<tree[n].feature<<" "<<" "<<tizq<<" "<<tree[n].w<<" "<<tder<<" "<<endl;
    if(tder!=")"){
        tree[n].feature=tder;
        parse(2*n,in);
        parse(2*n+1,in);
        in>>tder;
    }
}

void add_space(string &s){
    string s2;
    for(int i=0;i<s.size();i++){
        if(s[i]==')')
            s2+=' ';
        s2+=s[i];
        if(s[i]=='(')
            s2+=' ';
    }
    s=s2;
}

void solve(int n, double &res, map<string,int> &fs){
    res*=tree[n].w;
    if(tree[n].feature.size()){
        if(fs.count(tree[n].feature))
            solve(2*n,res,fs);
        else
            solve(2*n+1,res,fs);
    }
}

int main(){
    int test;
    gets(buff);
    sscanf(buff,"%d",&test);
    
    for(int t=1;t<=test;t++){
        printf("Case #%d:\n",t);
        
        gets(buff);
        int line;
        sscanf(buff,"%d",&line);
        string s;
        for(int i=0;i<line;i++){    
            gets(buff);
            s+=string(buff);
            s+=' ';
        }
        add_space(s);
        //cout<<s<<endl;
        istringstream in(s);        
        parse(1,in);
        
        gets(buff);
        int a;
        sscanf(buff,"%d",&a);
        
        for(int i=0;i<a;i++){
            
            map<string,int> fs;
            gets(buff);
            string s(buff);
            istringstream in2(s);
            in2>>s;
            int nf;
            in2>>nf;
            for(int j=0;j<nf;j++){
                in2>>s;
                fs[s]=1;
            }
            
            double res=1.0;
            solve(1,res,fs);
            
            printf("%.7lf\n",res);
        }
    }
    
    return 0;
}
