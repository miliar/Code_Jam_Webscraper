#include <string> 
#include <vector> 
#include <map> 
#include <utility> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <queue> 
#include <stack> 
#include <set> 
#include <sstream> 
#include <algorithm> 
#include <iostream> 
#include <iomanip> 
using namespace std; 
  
#define INF 0x3f3f3f3f
#define ALL(v) v.begin(),v.end() 
typedef pair<char,int> pci; 
char buff[1005];
char comb[256][256];
bool oppose[256][256];

int main(){
    int test;
    scanf("%d",&test);
    
    for(int tt=1;tt<=test;tt++){
        printf("Case #%d: ",tt);
        int c,d,n;
        
        memset(oppose,0,sizeof(oppose));
        memset(comb,-1,sizeof(comb));
        
        scanf("%d",&c);
        for(int i=0;i<c;i++){
            scanf("%s",buff);
            comb[buff[0]][buff[1]]=comb[buff[1]][buff[0]]=buff[2];
        }
        
        scanf("%d",&d);
        for(int i=0;i<d;i++){
            scanf("%s",buff);
            oppose[buff[0]][buff[1]]=oppose[buff[1]][buff[0]]=true;
        }
        
        scanf("%d",&n);
        scanf("%s",buff);
        string s;
        
        for(int i=0;i<n;i++){
            
            int l=s.size();
            if(!l){
                s+=buff[i];                
            }else{
                bool change=true;
                int ncomb=0;
                char add=buff[i];
                
                while(change){
                    change=false;
                    l=s.size();
                                        
                    if(l&&comb[s[l-1]][add]!=-1){
                        char ct=s[l-1];
                        s=s.substr(0,l-1);
                        add=comb[ct][add];
                        ncomb++;
                        change=true;                 
                    }
                }
                if(ncomb) s+=add;
                else{
                    bool clear=false;
                    for(char cc='A';cc<='Z'&&!clear;cc++)
                    if(s.find(cc)!=string::npos&&oppose[cc][buff[i]]){
                        s="";
                        clear=true;
                    }
                    if(!clear) s+=buff[i];
                }
            }
        }
        
        printf("[");
        for(int i=0;i<s.size();i++){
            if(i!=0) printf(", ");
            printf("%c",s[i]);
        }
        printf("]\n");
    }

    return 0;
}
