#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <conio.h>
#include <climits>
#include <queue>


using namespace std;

#define dv(vectName) for(int ii=0;ii<vectName.size();ii++) cout<<vectName[ii]<<' '; cout<<endl;
#define d1da(arrayName,size) for(int ii=0;ii<size;ii++) cout<<arrayName[ii]<<' '; cout<<endl;
#define d2da(arryName,row,col) for(int ii=0;ii<row;ii++){ for(int jj=0;jj<col;jj++) cout<<arryName[ii][jj]<<' '; cout<<endl; } cout<<endl; 

#define miii map<int,int>::iterator
#define mici map<int,char>::iterator
#define mcii map<char,int>::iterator
#define vii vector<int>::iteartor

#define pb(vectName,value) vectName.push_back(value);
#define mi(mapName,keyType,valType,key,val) mapName.insert(pair<keyType,valType>(key,val));



//fstream inp("a-small.in",ios::in);
fstream inp("a-large.in",ios::in);
fstream out("a-small.out",ios::out);

map<char,int> digmap;

vector<long long int> on;


long long int mypow(int base,int pos){
     long long int answer=1L;
     if(pos==0) return 1L;
     else{
          for(int i=1;i<=pos;i++)
                 answer*=(long long int)base;
          return answer;
     }
     
}


void solve(int testCaseNo){
     string an;     
     inp>>an;     
     digmap.clear();
     on.clear();
     int nc=2;     
     char ld=an[0];
     for(int i=0;i<an.length();i++){
             //cout<<"in"<<endl;
             char c=an[i];
             if(i==0){ digmap.insert(pair<char,int>(an[0],1)); }
             if(i>=1 && ld != '\0'){
                     if(c != ld){
                               digmap.insert(pair<char,int>(c,0));
                               ld='\0';
                     }
             }
             if( digmap.find(c)==digmap.end() ){
                                        digmap.insert(pair<char,int>(c,nc));             
                                        nc++;
                                        
             }
             on.push_back((long long int)digmap[c]);
             
     }     
     
     long long int ion=0L;
     reverse(on.begin(),on.end());
     //dv(on);
     for(int i=0;i<on.size();i++){
             ion+=(long long int)((long long int)on[i]*(long long)mypow(nc,i));
     }
     out<<"Case #"<<testCaseNo<<": "<<ion<<endl;
}


int main(void){
    int N;
    inp>>N;
    for(int i=1;i<=N;i++)
            solve(i);
    getch();
    return 0;
}
