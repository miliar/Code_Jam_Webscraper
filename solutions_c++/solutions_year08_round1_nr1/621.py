#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <conio.h>
using namespace std;

#define all(v) v.begin(),v.end()
#define pb(v,d) v.push_back(d)
#define create2dmat(n,t,r,c) n=new t*[(r)]; for(int i=0;i<(r);i++) n[i]=new t[(c)]
#define rep(vn,init,lt) for(int vn=(init);vn<(lt);vn++)
#define mapins(mn,t1,t2,v1,v2) mn.insert(std::pair<t1,t2>(v1,v2))
#define getmapiter(t1,t2,vn) map<t1,t2>::iterator vn
#define getindex(vn,target,pos) for(pos=0;pos<vn.size();pos++) { if(vn[pos]==(target)) break; } if (pos==vn.size()) pb(vn,traget);
#define free2dmat(vn,r) for(int j=0;j<(r);j++) delete [] vn[j]; delete [] vn;
#define display2dmat(vn,r,c) rep(newi,0,r){ rep(newj,0,c) cout<<vn[newi][newj]<<" "; cout<<"\n"; }
#define init2dmat(vn,r,c,val) rep(newi,0,r) rep(newj,0,c) vn[newi][newj]=val;
#define insqueue(qname,val) qname.push(val)
#define delqueue(qname,var) var=qname.front(); qname.pop();
#define pushstack(stkname,val) stkname.push(val);
#define popstack(stkname,var) var=stkname.top();stkname.pop();
#define dispvect(vecname) rep(newi,0,vecname.size()) cout<<"\n"<<vecname[newi]


typedef long int li;
typedef long long int lli;
typedef long double ld;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<li> vli;
typedef vector<lli> vlli;
typedef vector<ld> vld;

int formnumber(string number)
{    
    int len = number.size(),num=0,sign=1;    
    int start=0;
    if(number[0]=='-'){
        sign=-1;
        start=1;        
    }    
    for(int i=start;i<len;i++)            
            num*=10,num+=number[i]-48;                                    
    return sign*num;            
}

double formnumber(string number,double dummy)
{
    int len = number.size(),sign=1; 
    double num=0.0;   
    int start=0;
    if(number[0]=='-'){
        sign=-1;
        start=1;        
    }
    int dec=0;    
    for(int i=start;i<len;i++){
            if(number[i]=='.'){                               
               dec++;
               continue;
            }
            if(dec==0) num*=10;
            num+=(number[i]-48)*(double)(1.0/pow(10.0,(double)dec)); 
            if(dec>0) dec++;
    }
    return sign*num;   
}

string formstring(fstream& inp,bool* end=NULL,char delim = ' ')
{
    string item;
    while(1)
    {
           char e;
           inp.get(e);
           if(e==delim || inp.eof() || e=='\n')
           {
                      if((e=='\n' || inp.eof()) && end!= NULL) *end=true;
                      break;
           }
           item=item+e;     
    }    
    return item;
}
/************************************************************************************************/

long int sp(vi x, vi y)
{
     long int result=0L;
     rep(i,0,x.size())       
           result+=x[i]*y[i];     
     return result;
}

/*
bool notmatching(vi x,vi y)
{
     bool result=false;
     rep()
}*/

int main(void)
{
    int N;
    //fstream inp("test.in",ios::in);
    fstream inp("A-large.in",ios::in);
    N=formnumber(formstring(inp));    
    //cout<<"\n N = "<<N;    
    rep(i,1,N+1)
    {
        int vecsz;
        inp>>vecsz;
        vi x,y;
        rep(j,0,vecsz){
            int xi;
            inp>>xi;
            pb(x,xi);
        }
        rep(j,0,vecsz){
            int yi;
            inp>>yi;
            pb(y,yi);
        }
        sort(all(x));
        sort(all(y));
        int xs=x.size();
        int ys=y.size();        
        lli minprod=0LL;
        rep(j,0,xs)
             minprod+=(lli)x[j]*(lli)y[ys-1-j];
        cout<<"\nCase #"<<i<<": "<<minprod;/*
                         
        vi tx(x),ty(y);
        li minprod=sp(x,y);
        while(1)
        {
                do
                {
                        li prod;
                        next_permutation(all(y));
                        prod=sp(x,y);
                        if(prod < minprod)
                         minprod=prod;
                        cout<<"\n\n the minprod is "<<minprod;
                        //getch();
                }while(y != ty);
                next_permutation(all(x));
        }while(x != tx);*/
        
    }
    inp.close();
    getch();
    return 0;
}


