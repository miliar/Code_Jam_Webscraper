
//CODER: Adolfo Ccanto Ad...
#include<iostream>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<algorithm>
#include<sstream>
#include<stack>
#include<math.h>
#include<string>

#define F(i,a,b) for(int i=a;i<b;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define pii pair<int,int>

#define FE(it,sto) for(typeof(sto.begin())it=sto.begin();it!=sto.end();++it)


using namespace std;

int main(){
freopen("A-small-attempt0 (2).in","r",stdin);
freopen("salida.ou","w",stdout);

int k;
string ad="yhesocvxduiglbkrztnwjpfmaq";
cin>>k;
int test=1;
scanf("\n"); 
string s;
while(k--){
 getline(cin,s);
 string lesli="";
 F(i,0,s.size())if(s[i]!=' ')lesli+=ad[s[i]-'a'];else lesli+=" ";
 cout<<"Case #"<<test++<<": "<<lesli<<endl;
}                
}
