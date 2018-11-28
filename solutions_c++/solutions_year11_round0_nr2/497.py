#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<math.h>
#include<string>

using namespace std;
char h[100][100];
bool op[100][100];
int tot;
int n;
int f(char c){
      return c-'A'+1;
}

int main(){
      freopen("B-large.in","r",stdin);
      freopen("out.txt","w",stdout);
      cin>>tot;
      for (int ca=1;ca<=tot;ca++){
            memset(h,0,sizeof(h));
            memset(op,0,sizeof(op));
            string s;
            cin>>n;
            for (int i=1;i<=n;i++){
                  cin>>s;
                  h[f(s[0])][f(s[1])]=s[2];
                  h[f(s[1])][f(s[0])]=s[2];
            }
            cin>>n;
            for (int i=1;i<=n;i++){
                  cin>>s;
                  op[f(s[0])][f(s[1])]=1;
                  op[f(s[1])][f(s[0])]=1;
            }
            cin>>n;
            cin>>s;
            string ans;
            for (int i=0;i<s.size();i++){
                  ans+=s[i];
                  int l=ans.size();
                  while (l>1&&h[f(ans[l-1])][f(ans[l-2])]){
                        char c=h[f(ans[l-1])][f(ans[l-2])];
                        ans.erase(l-2,2);
                        ans+=c;
                        l=ans.size();
                  }
                  for (int i=0;i<l-1;i++) if (op[f(ans[i])][f(ans[l-1])]){
                        ans.clear();
                        l=0;
                        break;
                  }
            }
            cout<<"Case #"<<ca<<": [";
            if (!ans.empty()) cout<<ans[0];
            if (!ans.empty()) for (int i=1;i<=ans.size()-1;i++) cout<<", "<<ans[i];
            cout<<"]"<<endl;
      }
}
      
            
                        

                        
            
            
                  
            
                  
                  
                  
      
      
