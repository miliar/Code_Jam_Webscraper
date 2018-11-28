//A continuación, otra buena solución por andres.escobar
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <string>
#include <fstream>

using namespace std;

#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)


string uno = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
string dos = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
string S;
char convierte(char x){
     if(x=='q') return 'z';
     if(x=='z') return 'q';
     REP(i,105)if(x==uno[i]) return dos[i];
     }
int main(){
    freopen("A-small-attempt5.in","r",stdin);freopen("A-small-attempt5.out","w",stdout);
    //cout<<uno.size()<<endl;
    int T;
    cin>>T;
    cin.ignore();
    int c=1;
    REP(i,T){
             getline(cin,S);
             REP(i,S.size())if(S[i]!=' ') S[i]=convierte(S[i]);
             cout<<"Case #"<<c<<": "<<S<<endl;
             c++;
             }
}
