#include <iostream>
#include <string>
#include <vector>

using namespace std;

int i,j,k,l,m,n,t,tt,cc,dd,ii,jj;
char c[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
char sim;
int index(char cc){
    int i;
    if (cc<'A' || cc>'Z') cout<<"Sig xo ara gaq"<<endl;
    for (i=0;i<8;i++)
        if (c[i]==cc)
           return i;
    return i;
}
string s;
char combine[9][9];
int opposed[9][9];
vector <char> ans;

int main(){
    freopen("c:/input.txt","r",stdin);
    freopen("c:/output.txt","w",stdout);
    cin>>t;
    while (t--){
          for (i=0;i<9;i++)
              for (j=0;j<9;j++){
                  combine[i][j]=' ';
                  opposed[i][j]=0;
              }
          tt++;
          cout<<"Case #"<<tt<<": ";
          cin>>cc;
          for (i=0;i<cc;i++){
              cin>>s;
              combine[index(s[0])][index(s[1])]=s[2];
              combine[index(s[1])][index(s[0])]=s[2];
          }
          cin>>dd;
          for (i=0;i<dd;i++){
              cin>>s;
              opposed[index(s[0])][index(s[1])]=1;
              opposed[index(s[1])][index(s[0])]=1;  
          }
          cin>>n;
          for (i=0;i<n;i++){
              cin>>sim;
              ans.push_back(sim);
              l=ans.size();
              if (l>1){
                 if (combine[index(ans[l-1])][index(ans[l-2])]!=' '){
                    char ttt=combine[index(ans[l-1])][index(ans[l-2])];
                    ans[l-2]=ttt;
                    ans.pop_back();
                 } else
                 {
                       int d=0;
                       for (ii=0;ii<l;ii++){
                           if (d) break;
                           for (jj=ii+1;jj<l;jj++)
                               if (opposed[index(ans[ii])][index(ans[jj])]){
                                  ans.erase(ans.begin(),ans.end());
                                  d=1;
                                  break;
                               }
                       }
                 }
              }
          }
          l=ans.size();
          cout<<'[';
          for (i=0;i<l-1;i++){
              cout<<ans[i]<<", ";
          }
          if (l>0)
          cout<<ans[l-1];
          cout<<"]"<<endl;
          ans.erase(ans.begin(),ans.end());
    }
    //system("pause");
    return 0;    
}
