
#include<set>
#include<map>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<algorithm>
#define fr(i,n) for(int i=0;i<n;++i)
#define For(i,a,b) for(int i=a;i<b;++i)
#define Rev(i,a,b) for(int i=a;i>=b;--i)

using namespace std;

int total,n,m,t;
vector < map<string,int> > nei;

int getnxt(string rr){
    //cout<<"\n#############           "<<rr<<"\n";
    fr(i,rr.size()){
   //    cout<<rr[i];            
       if(rr[i]=='/'){
        //  cout<<rr.substr(0,i)<<endl; 
         return (i);
         }               
    }             
//    cout<<t<<endl;
    return rr.size();   

}

int parse(string g){
    int ct=0;  
    int ans=0;
    For(i,1,g.size()){
        //              cout<<" \n********* i is "<<i<<"*******";
                      string yy=g.substr(i,g.size());
       int k=getnxt(yy);
      // cout<<"\nk is "<<k;
       string ww=g.substr(i,k);  
       //cout<<"ww  is "<<ww;
       if(nei[ct].find(ww)==nei[ct].end()){
           ++ans;
           nei[ct].insert(make_pair(ww,total++));
           map<string, int> asd;
           asd.clear();
           nei.push_back(asd);        
           ct=total-1;                        
       }
       else{
           map<string,int> :: iterator cv=nei[ct].find(ww);
           ct=cv->second; 
       }
       i+=k; 
    } 
    //cout<<"init ct is "<<ct<<endl;
    return ans;
}

int main(){
    //clock_t clck1=clock();
    //	freopen("C.in","r",stdin);
	freopen("11in.in","r",stdin);freopen("11out.in","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin);freopen("C-small-attempt2.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);
    //clock_t clck2=clock();
    //cerr<<double(clck2-clck1)/CLOCKS_PER_SEC<<endl; 
    scanf("%d",&t);
    int count=1;
    while(t--){
               total=1;
       scanf("%d%d",&n,&m);   
       nei.clear();
       map<string , int> wer;
       wer.clear();
       nei.push_back(wer);
       fr(i,n){
          string temp;
          cin>>temp;
          int dd=parse(temp);     
       }   
       int ans=0;  
       fr(i,m){
           string temp;
           cin>>temp;
           ans+=parse(temp);    
       }
        printf("Case #%d: %d\n",count,ans);
        count++;
    } 
}
