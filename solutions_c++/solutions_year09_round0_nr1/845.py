#include<iostream>
#include<string>
using namespace std;
char ch[6000][16];
bool b[16][300];
int n,l,d,ans;
void init(){
     memset(b,0,sizeof(b));
     int i=0,le=0;
     while (i<l){
           char chs;
           cin>>chs;
           if (chs=='(') {le=1;continue;}
           if (chs==')') {le=0;i++;continue;}
           b[i][chs]=1;
           if (le==0) i++;
     }
}
void work(){
     ans=0;
     for (int i=0;i<d;i++){
         int j;
         for (j=0;j<l;j++)
         if (!b[j][ch[i][j]]) break;
         if (j<l) continue;
         ans++;
     }
}
int main(){
  //  freopen("1.in","r",stdin);
  //  freopen("1.out","w",stdout);
    cin>>l>>d>>n;
    for (int i=0;i<d;i++)
    for (int j=0;j<l;j++)
    cin>>ch[i][j];
    for (int i=0;i<n;i++){
        init();
        work();
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
   // return 0;
}
