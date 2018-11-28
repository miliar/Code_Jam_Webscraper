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
#define maxint 2147483647
#define minint -2147483648


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

string formstring(string original,int spw0asfirst,int ep)
{
       string ret;
       rep(i,spw0asfirst,ep+1)
           ret=ret+original[i];
       return ret;
}

//Input : string of tokens separted by delim. 1st char and last char SHOULD NOT BE DELIM
//output : vector<string> of tokens
vector<string> tokenize(string str,char delim){
               vector<string> answer;
               int i=0;               
               string temp="";
               while(i < str.length()){
                       char c=str[i];
                       if(c==delim){                                                                    
                                  answer.push_back(temp);
                                  temp = "";           
                       }
                       else{
                            temp += c;      
                       }
                       i++;                                             
               }               
               answer.push_back(temp);
               return answer;
}
/************************************************************************************************/



bool intersect(int a1,int a2,int b1,int b2){
     return !((a1>a2 && b1>b2) || (a1<a2 && b1<b2));
}

int main(void)
{    
    fstream inp("c-large.in",ios::in);
    fstream out("c-large.out",ios::out);
    /*#define inp cin
    #define out cout*/
    int T;
    inp>>T;    
    for(int i=1;i<=T;i++){ 
            int N;
            inp>>N;
            vector< pair<int,int> > wires(N);
            for(int j=0;j<N;j++){
                    int a,b;
                    inp>>a>>b;
                    wires[j] = std::pair<int,int>(a,b);
            }
            
            long int answer=0L;
            if(N==1) answer = 0;
            else{             
                for(int j=0;j<N;j++){
                        pair<int,int> wire1 = wires[j];
                        for(int k=0;k<N;k++){
                                pair<int,int> wire2 = wires[k];
                                if(j!=k){
                                         int a1=wire1.first,b1=wire1.second,a2=wire2.first,b2=wire2.second;                         
                                         if(intersect(a1,a2,b1,b2)) answer++;
                                }
                        }
                }
                answer /= 2;            
            }
            out<<"Case #"<<i<<": "<<answer<<endl;                         
    }
    getch();
    return 0;
}


