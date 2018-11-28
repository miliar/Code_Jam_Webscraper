#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;
string s[6000];
string regex;
int a[100][256],l,n,d,k;

void buildMachine(){
    memset(a,-1,sizeof a);
    int l = regex.size();
    bool inB = false;
    k =0;
    for(int i=0;i<l;i++){
      if(regex[i]=='('){
        inB = !inB;
        k++;
      }else if(regex[i]==')'){
        inB = !inB;
      }else if(!inB){
        k++;
        a[k-1][regex[i]-'a'] = k;
      }
      else if(inB){
        a[k-1][regex[i]-'a'] = k;
      }
   }   
}

int matches()
{
    int cnt =0;
    for(int i=0;i<d;i++){
        int l = s[i].size();
        int pos = 0;
        for(int j=0;j<l;j++){
            pos = a[pos][s[i][j]-'a'];
            if(pos==-1)break;
        }
        if(pos==k)cnt++;
    }
    return cnt;
}

int main(int argc, char const* argv[])
{
    cin>>l>>d>>n;
    for(int i=0;i<d;i++)cin>>s[i];
    for(int i=0;i<n;i++){
      cin>>regex;
      buildMachine();
      cout<<"Case #"<<i+1<<": "<<matches()<<endl;
    }
    return 0;
}
