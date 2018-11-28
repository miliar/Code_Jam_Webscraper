#include<iostream>
#include <fstream>
#include<algorithm>
#include<string>
using namespace std;
    ofstream fout ("file.out");
    ifstream fin ("file.in");
    void pri(int i,int a[],int l){
         fout<<"Case #"<<i+1<<": ";
         for(int k=0;k<l;k++)
           fout<<a[l-1-k];
         fout<<endl;
    }
    bool aa(int i,int j){
         return i>=j;
    }
int main(){
    int n;
    fin>>n;
    string s;
    getline(fin,s);
    for(int i=0;i<n;i++){
            int k;
            getline(fin,s);
            int a[40],l=0;
            for(int j=0;j<s.length();j++)
              if(s[s.length()-1-j]>='0'&&s[s.length()-1-j]<='9'){
              a[l]=s[s.length()-1-j]-'0';
              l++;
            }
            int t=1;
            while(t<=l-1&&a[t-1]<=a[t])
              t++;
            if(t==l){
              int min=10,kk;
              for(int j=0;j<l;j++)
                if(a[j]<min&&a[j]!=0){
                  kk=j;
                  min=a[j];
                }
              a[l]=a[kk];
              a[kk]=0;
              sort(a,a+l,aa);
              l++;
              pri(i,a,l);
            }
            else{
                 int temp,max=10,kk;
                 for(int j=t;j>=0;j--)
                   if(a[j]>a[t]&&a[j]<max){
                     max=a[j];
                     kk=j;
                   }
                 temp=a[t];
                 a[t]=a[kk];
                 a[kk]=temp;
                 sort(a,a+t,aa);
                 pri(i,a,l);
                 }
    }
    return 0;
}                 
            
