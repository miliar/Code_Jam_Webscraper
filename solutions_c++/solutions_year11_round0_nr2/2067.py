#include<iostream>
#include<fstream>
#include<cstdlib>
#include<string>
#include<vector>
#include<set>
using namespace std;

struct Conflict{
       char a;
       char b;
}temp_cf;

struct Combine{
       char a;
       char b;
       char c;
}temp_cb;

bool equal(char a,char b,char c,char d)
{
     if(a==c&&b==d) return true;
     if(a==d&&b==c) return true;
     
     return false;
}

int main()
{
    fstream input,output;
    input.open("1.txt",ios::in);    
    output.open("2.txt",ios::out);    
    
    vector<Combine> combine;
    vector<Conflict> conflict;
    int t,T,C,D,N,i,j,k;
    char ch;
    string s;
    char ans[101],inv[101]; 
    int count;
      
    bool u;
    input>>T;
    for(t=1;t<=T;t++) {
      for(i=0;i<101;i++) ans[i]=0;
      input>>C;
      for(i=1;i<=C;i++) {
         input>>s;
         temp_cb.a=s[0];  temp_cb.b=s[1];   temp_cb.c=s[2];
         combine.push_back(temp_cb);
      }
      input>>D;
      for(i=1;i<=D;i++) {
         input>>s;
         temp_cf.a=s[0]; temp_cf.b=s[1];
         conflict.push_back(temp_cf);
      }
      input>>N;
      input>>inv;


      count=0;
      for(j=0;j<N;j++) {
         ans[count]=inv[j];
         if(count!=0)
         {  u=false;
            for(i=0;i<C;i++) {
               if(equal(ans[count],ans[count-1],combine[i].a,combine[i].b)) {
                  ans[count]=0;
                  ans[--count]=combine[i].c;
                  u=true;
               }
               if(u) break;
            }
            for(i=0;i<D;i++) {
               if(u) break;
               for(k=0;k<count;k++) {
                 if(equal(ans[count],ans[k],conflict[i].a,conflict[i].b)) {
                    for(k=0;k<=100;k++) ans[k]=0;
                    u=true;
                    count=-1;
                    break;
                 }
               }
            }
         }
         count++;
      }
            
//      cout<<"Case #"<<t<<": "<<ans<<endl;
      output<<"Case #"<<t<<": [";
      for(i=0;ans[i]!=0;i++) {
         if(i!=0) output<<", ";
         output<<ans[i];
      }
      output<<"]"<<endl;
      conflict.clear(); combine.clear();
    }
    
    system("pause");
    return 0;
    
}
