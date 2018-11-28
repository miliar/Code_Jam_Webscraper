#include <iostream>
#include <fstream>
using namespace std;
#define forn(i,n) for(int i=0; i<(int)(n); i++)

char let[30];
string inpu;
string oupu;


int main(){
    ifstream in("gcj.in");
    ofstream out("gcj.out");

    inpu="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    oupu="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    int x = inpu.size();
    forn(i,x)if(inpu[i]!=' ')let[inpu[i]-'a']=oupu[i];
    let['q'-'a']='z';
    let['e'-'a']='o';
    let['y'-'a']='a';
    let['z'-'a']='q';
    
    int g; in>>g;
    string s;
    getline(in,s);
    int t;
    forn(t,g) {	
      out<<"Case #"<<t+1<<": ";
      getline(in,s);
      int y = s.size();
      forn(i,y)if(s[i]!=' ')s[i]=let[s[i]-'a'];
      out<<s<<endl;
      //forn(i,y)if((s[i]>'z' || s[i]<'a') && s[i]!=' ')out<<"!!!!!!!!!!!!!!";
    }
    }
