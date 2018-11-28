#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
    int test,c=1;
    
    freopen("A.txt", "r", stdin);
    freopen("Aanswer.txt", "w", stdout);
    
    
    cin>>test;
    while(test--){
    char a[5][5];
    int empty=0,answer=0;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++){
            cin>>a[i][j];
            if(a[i][j]=='.') empty++;
        }
    }
    
    
    string p;
   for(int i=0;i<4;i++)
   {
       if(answer==1) break;
       p.clear();
       for(int j=0;j<4;j++){
       p+=a[i][j];
       if(p=="XXXX" || p=="XXXT" || p=="XXTX" || p=="XTXX" || p=="TXXX")
       {
           answer=1;i++;
           cout<<"Case #"<<c<<": "<<"X won"<<endl;
           break;
       }
       
       else if(p=="OOOO" || p=="OOOT" || p=="OOTO" || p=="OTOO" || p=="TOOO")
       {
           answer=1;
           cout<<"Case #"<<c<<": "<<"O won"<<endl;
           break;
       }
       
   }
   }
   if(answer==0){
   
     for(int i=0;i<4;i++)
   {
       if(answer==1) break;
       p.clear();
       for(int j=0;j<4;j++){
       p+=a[j][i];
       if(p=="XXXX" || p=="XXXT" || p=="XXTX" || p=="XTXX" || p=="TXXX")
       {
           answer=1;
           cout<<"Case #"<<c<<": "<<"X won"<<endl;
           break;
       }
        else if(p=="OOOO" || p=="OOOt" || p=="OOTO" || p=="OTOO" || p=="TOOO")
       {
           answer=1;
          cout<<"Case #"<<c<<": "<<"O won"<<endl;
           break;
       }
       
   }
   }
   
   if(answer==0){
       p.clear();
       for(int i=0;i<4;i++)
       {
           
           p+=a[i][i];
           if(p=="XXXX" || p=="XXXT" || p=="XXTX" || p=="XTXX" || p=="TXXX")
       {
           answer=1;
           cout<<"Case #"<<c<<": "<<"X won"<<endl;
           
       }
        else if(p=="OOOO" || p=="OOOt" || p=="OOTO" || p=="OTOO" || p=="TOOO")
       {
           answer=1;
           cout<<"Case #"<<c<<": "<<"O won"<<endl;
           
       }
       }
       
       if(answer==0){
          p.clear();
          for(int i=0;i<4;i++) 
          p += a[i][4-i-1];
          //cout<<p<<endl;
           if(p=="XXXX" || p=="XXXT" || p=="XXTX" || p=="XTXX" || p=="TXXX")
       {
           answer=1;
          cout<<"Case #"<<c<<": "<<"X won"<<endl;
           
       }
        else if(p=="OOOO" || p=="OOOT" || p=="OOTO" || p=="OTOO" || p=="TOOO")
       {
           answer=1;
          cout<<"Case #"<<c<<": "<<"O won"<<endl;
           
       }
       }
   }
   }
   if(answer==0 && empty==0) cout<<"Case #"<<c<<": "<<"Draw"<<endl;
   else if(answer==0 && empty!=0)
    cout<<"Case #"<<c<<": "<<"Game has not completed"<<endl;
   
    
   /* for(int i=0;i<4;i++){
    for(int j=0;j<4;j++)
    cout<<a[i][j];
    cout<<endl;
    
    }*/
    c++;
    
    }
}
