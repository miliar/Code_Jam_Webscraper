#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#define  f(x,y,i) for(int i=x;i<y;i++)
#define in(n,up) find(up,up+sizeof(up)/4,(n))-&up[0]!=sizeof(up)/4 
using namespace std;

vector<string> A;
string s,cad;
vector<string> B;

int main()
{
    bool aun=0,contar=1;
    int L,D,N,cnt=0;
    cin>>L>>D>>N;
    f(0,D,i){
        cin>>s;
        A.push_back(s);
    }
    f(0,N,i){
        cin>>s;
        cad="";
        cnt=0;
        B.clear();
        f(0,s.size(),j){
            if(s[j]=='('){ aun=1; continue;}
            if(s[j]==')'){ 
                aun=0; B.push_back(cad);
                cad=""; continue;
            }
            if(!aun) B.push_back(cad+s[j]);
            else cad+=s[j];
        }
//        f(0,B.size(),j) cout<<B[j]; cout<<endl;
        f(0,D,j){
            contar=1;
            f(0,L,k){
                if(B[k].find(A[j][k])==string::npos ) contar=0;
            }
            if(contar) cnt++;
        }
        
        printf("Case #%d: %d\n",i+1,cnt);
    }
    
}
