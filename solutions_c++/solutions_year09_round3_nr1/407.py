#include<iostream>
#include <fstream>
#include<string>
#include<map>
using namespace std;
    ofstream fout ("file.out");
    ifstream fin ("file.in");
    const int mm=1000;
    struct qq{
           int l;
           int a[mm];
    };
    void pri(int i,qq j){
         fout<<"Case #"<<i+1<<": ";
         for(int t=j.l-1;t>=0;t--)
           fout<<j.a[t];
         fout<<endl;
    }
    void init(qq &a){
         for(int i=0;i<mm;i++)
           a.a[i]=0;
         a.l=0;
    }
    void mul(qq &a,int k){
         a.a[0]=a.a[0]*k;
         int l=a.l;
         for(int i=1;i<=l;i++){
           a.a[i]=a.a[i]*k+a.a[i-1]/10;
           a.a[i-1]=a.a[i-1]%10;
         }
         while(a.a[l]>0){
           a.a[l+1]=a.a[l]/10;
           a.a[l]=a.a[l]%10;
           l++;
         }
         a.l=l;
    }
    void add(qq &a,qq b){
         int l;
         if(a.l>b.l)
           l=a.l;
         else l=b.l;
         for(int i=0;i<l;i++){
            a.a[i]=a.a[i]+b.a[i];
            a.a[i+1]+=a.a[i]/10;
            a.a[i]=a.a[i]%10;
         }
          while(a.a[l]>0){
           a.a[l+1]=a.a[l]/10;
           a.a[l]=a.a[l]%10;
           l++;
         }
         a.l=l;
    } 
    void cop(qq &a, qq b){
         for(int i=0;i<b.l;i++)
           a.a[i]=b.a[i];
         a.l=b.l;
    }                          
int main(){
    int n;
    fin>>n;
    string s;
    getline(fin,s);
    for(int i=0;i<n;i++){
            map<char,int> a;
            getline(fin,s);
            int l=0,t=1;
            for(int j=0;j<s.length();j++){
                    if(a.count(s[j])==0){
                      a[s[j]]=t;
                      l++;
                      if(t==1)
                        t=0;
                      else if(t==0)
                            t=2;
                            else t++;
                    }
            }
            if(l==1)
              l=2;
            qq p,o,tt;
            init(p);
            p.a[0]=1;
            p.l=1;
            init(o);
            for(int j=s.length()-1;j>=0;j--){
                    init(tt);
                    cop(tt,p);
                    mul(tt,a[s[j]]);
                    add(o,tt);
                    mul(p,l);
            }
            pri(i,o);
    }
    return 0;
}
            
