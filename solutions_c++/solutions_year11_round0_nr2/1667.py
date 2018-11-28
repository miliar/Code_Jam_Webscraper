#include<iostream>
#include<string>
#include<string.h>
#include<stdio.h>
#include<map>

using namespace std;

map<string,char> form;
map<string,int> opp;
char res[105];
int e;

void process(){
     if(e==1) return ;
     int i;
     string s;
     while(e>1){
       s="";
       s+=res[e-1];s+=res[e-2];
       if(form.find(s)!=form.end()){
            res[e-2]=form[s];
            e--;
       }else{
           s="";
           s+=res[e-2];s+=res[e-1];
           if(form.find(s)!=form.end()){
              res[e-2]=form[s];
              e--;
           }
           else{break;}
       }
     }
     for(i=0;i<=e-2;i++){
        s="";
        s+=res[e-1];
        s+=res[i];
        if(opp.find(s)!=opp.end()){
            e=0;
            break;
        }
        s="";
        s+=res[i];
        s+=res[e-1];
        if(opp.find(s)!=opp.end()){
            e=0;
            break;
        }
     }
}

int main()
{
//    freopen("in.txt","r",stdin);
//    freopen("B-small-attempt0.out","w",stdout);
    
    int t;
    int cas=1;
    cin>>t;
    while(t--){
        int C,D,N;
        form.clear();
        opp.clear();
        
        string in;
        string tmp;
        cin>>C;
        int i;
        for(i=0;i<C;i++){
            cin>>in;
            tmp="";
            tmp+=in[0];
            tmp+=in[1];
            form[tmp]=in[2];
            tmp="";
            tmp+=in[1];
            tmp+=in[0];
            form[tmp]=in[2];
        }
        cin>>D;
        for(i=0;i<D;i++){
             cin>>in;
             tmp="";
             tmp+=in[0];
             tmp+=in[1];
             opp[tmp]=1;
             tmp="";
             tmp+=in[1];
             tmp+=in[0];
             opp[tmp]=1;
        }
        cin>>N;
        cin>>in;
        e=0;
        for(i=0;i<N;i++){
           res[e++]=in[i];
           process();
        }
        printf("Case #%d: [",cas++);
        for(i=0;i<=e-2;i++)
          printf("%c, ",res[i]);
        if(e>=1)
          printf("%c",res[e-1]);
        printf("]\n");
    }
}
