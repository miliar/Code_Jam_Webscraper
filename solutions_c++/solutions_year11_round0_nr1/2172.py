#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;

struct S
{
   int pos;
   char robot;
};

int sign(int num)
{
    if(num>0) return 1;
    
    if(num<0) return -1;
    
    return 0;
}

int main()
{
    fstream input,output;
    input.open("1.txt",ios::in);    
    output.open("2.txt",ios::out);    
    
    int t,T,N,i,j;
    char ch;
    
    S s[101];
    
    int opos,bpos,ans,otask,btask,ttask;
    
    input>>T;
    for(t=1;t<=T;t++) {
      input>>N;
      for(i=1;i<=N;i++) input>>s[i].robot>>s[i].pos;
      
//      for(i=1;i<=N;i++) cout<<s[i].robot<<" "<<s[i].pos<<" ";      cout<<endl;
      opos=1;
      bpos=1;
      otask=btask=0; ttask=1;
      for(ans=1;1;ans++) 
      {
         if(ttask>otask) 
         {
             for(i=ttask;i<=N;i++) 
               if(s[i].robot=='O') {
                  otask=i;
                  break;
               }
             if(i==N+1) otask=200;
         }
         if(ttask>btask) 
         {
             for(i=ttask;i<=N;i++) 
               if(s[i].robot=='B') {
                  btask=i;
                  break;
               }
             if(i==N+1) btask=200;
         }
         ch=s[ttask].robot;
         if(ch=='O') {
            if(opos==s[otask].pos) ttask++;
            else opos= opos + sign(s[otask].pos-opos);
            
            if(btask!=200)
               bpos = bpos + sign(s[btask].pos-bpos);
         }
         else {
            if(bpos==s[btask].pos) ttask++;
            else bpos= bpos + sign(s[btask].pos-bpos);
            
            if(otask!=200)
              opos = opos + sign(s[otask].pos-opos);
         }
         if(ttask==N+1) break;
      }
      cout<<"Case #"<<t<<": "<<ans<<endl;
      output<<"Case #"<<t<<": "<<ans<<endl;
    }
    
    system("pause");
    return 0;
    
}
