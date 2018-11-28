#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
int main()
{
  //  ifstream cin("A-small-attempt0.in");
 //   ifstream cin("in.in");
    ifstream cin("A-large.in");
    
    ofstream cout("out.txt");
    int n;
    char yy[105];
    cin>>n;
    for(int u=1;u<=n;u++){
       int s;
       cin>>s;
       cin.getline(yy,105); 
       int se[105];
       char sse[105][105];
       for(int i=0;i<s;i++){
          cin.getline(sse[i], 105);
          se[i]=0;
       }
       int que[1003];
       char x[105];
       int q;
       cin>>q;
       cin.getline(yy,105); 
       for(int i=0;i<q;i++){
          cin.getline(x, 105);
          for(int j=0;j<s;j++){
             if(strcmp(x, sse[j])==0){
                que[i]=j;
                break;
             }
          }
       }

       int t=0;
       int w=0;
       int z=0;
       while(t<q){ 
          if(se[que[t]]==0){
             se[que[t]]=1;
             z++;
          }
          if(z==s){
             w++;
             for(int i=0;i<s;i++)
                se[i]=0;
             se[que[t]]=1;
             z = 1;
          }
          t++;
       }
       cout<<"Case #"<<u<<": "<<w<<endl;
    }
       
}
