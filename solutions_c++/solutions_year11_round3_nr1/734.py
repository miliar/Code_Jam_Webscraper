#include<iostream>
#include<string>

using namespace std;

int tot,n,m;

string s[100];

bool in(int i,int j){
      return (i<n&&j<m);
}
int main(){
      freopen("D:\\A-large.in","r",stdin);
      freopen("D:\\out.txt","w",stdout);
      cin>>tot;
      for (int ca=1;ca<=tot;ca++){
            cin>>n>>m;
            for (int i=0;i<n;i++) cin>>s[i];
            bool can=1;
            for (int i=0;i<n;i++)
            for (int j=0;j<m;j++) if (s[i][j]=='#'){
                  if (!in(i+1,j+1)){
                        can=0;
                        break;
                  } else
                  if (s[i+1][j]!='#'||s[i+1][j+1]!='#'||s[i][j+1]!='#'){
                        can=0;
                        break;
                  } else{
                        s[i][j]=s[i+1][j+1]='/';
                        s[i+1][j]=s[i][j+1]='\\';
                  }
            }
            cout<<"Case #"<<ca<<":"<<endl;
            if (can) for (int i=0;i<n;i++) cout<<s[i]<<endl; else
            cout<<"Impossible"<<endl;
      }
}

                  
                  
                  
