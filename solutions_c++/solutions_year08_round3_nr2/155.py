#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;

int ans=0;

bool isugly(string &s){
    long long num=0;
    long long tmp=0;
    int i=0;
    int c=1;
    while(1){
        if(i>=s.length())break;
        if(s[i]=='+'){
            num=num+(c*tmp);
            tmp=0;
            c=1;
        }
        else if(s[i]=='-'){
            num=num+(c*tmp);
            tmp=0;
            c=-1;
        }
        else{
            tmp=(tmp*10)+(s[i]-'0');
        }
        i++;
    }
    num=num+(c*tmp);
    if(num==0)return true;
    if(num%2==0)return true;
    if(num%3==0)return true;
    if(num%5==0)return true;
    if(num%7==0)return true;
    return false;
}

void fun(string &a, string &b, int c, int l){
    if(c==l){
        if(isugly(b))ans++;
        return;
    }
    string temp;
    for(int i=0;i<3;i++){
        if(i==0){
            temp=b+"+"+a[c];
        }
        else if(i==1){
            temp=b+"-"+a[c];
        }
        else{
            temp=b+a[c];
        }
        fun(a,temp,c+1,l);
    }
}

int main(){
    int t;
    scanf("%d",&t);
    int cs=0;
    long long num;
    
    while(t--){
        cs++;
        ans=0;
        char str[100];
        string s;
        scanf(" %s",str);
        s=str;


        int l=s.length();
        string t="";
        t=t+s[0];
        fun(s,t,1,l);

        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}
