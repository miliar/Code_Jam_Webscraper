#include <iostream>
#define TASK "B"
#define Small "-small-attempt"
#define NUM "1"
#include <string>
#include <map>
#include <set>

using namespace std;

int test;
int n;
int c,d;
int answer;
map<string,char> Comb;
set<string> Rem;

char ans[1000];
int len;

void readinput(){
    Comb.clear();
    Rem.clear();
    cin>>c;
    string s;
    for (int i=0;i<c;i++){
        cin>>s;
        string ss = s.substr(0,2);        
        Comb[ss]=s[2];
        ss = s[1];
        ss=ss+(s[0]);
        Comb[ss]=s[2];
    }               
    cin>>d;
    for (int i=0;i<d;i++){
        cin>>s;        
        Rem.insert(s);
        string ss = "";
        ss=ss+s[1];
        ss=ss+s[0];
        Rem.insert(ss);    
    }
}

void solve(){
    cin>>n;
    string s;
    cin>>s;
    len = 0;
    for (int i=0;i<n;i++){
        ans[len++]=s[i];
        while (len>=2){
            string s = "";
            s = s + ans[len-2]+""+ans[len-1];
            bool flag = 0;
            if (Comb.find(s)!=Comb.end()){
                ans[len-2]=Comb[s];
                len--;    
                flag = 1;
            }else{
                for (int i=len-2;i>=0;i--){
                    string ss = "";
                    ss=ss+ans[i]+""+ans[len-1];
                    if (Rem.find(ss)!=Rem.end()){
                        len=0;
                        flag = 1;
                        break;    
                    }    
                }    
            }
            if (!flag) break;    
        }                
    }    
}

void writeoutput(int t){
    printf("Case #%i: ",t+1);        
    printf("[");
    for (int i=0;i<len-1;i++){
        cout<<ans[i]<<", ";    
    }
    if (len>0){
        cout<<ans[len-1];
    }
    cout<<"]";    
    printf("\n");
}

int main(void){
    //freopen("input.txt","r",stdin);    
    //freopen(TASK""Small""NUM".in","r",stdin);
    freopen(TASK"-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%i\n",&test);
    for (int i=0;i<test;i++){
        readinput();
        solve();
        writeoutput(i);
    }
    
    return 0;    
}
