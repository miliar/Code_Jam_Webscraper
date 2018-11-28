#include<iostream>
#include<string>
#include<cctype>
using namespace std;

int main(){
   int T;
   cin >> T;
   string dummy;
   getline(cin,dummy);
   for(int k = 1 ; k <= T ; k++){
      string s;
      getline(cin,s);

      string ans = "";
      for(int i = 0 ; i < s.size() ; i++){ 
	 if(isspace(s[i]))ans+=" ";
	 else{
	    if(s[i]=='a')ans+="y";
	    if(s[i]=='b')ans+="h";
	    if(s[i]=='c')ans+="e";
	    if(s[i]=='d')ans+="s";
	    if(s[i]=='e')ans+="o";
	    if(s[i]=='f')ans+="c";
	    if(s[i]=='g')ans+="v";
	    if(s[i]=='h')ans+="x";
	    if(s[i]=='i')ans+="d";
	    if(s[i]=='j')ans+="u";
	    if(s[i]=='k')ans+="i";
	    if(s[i]=='l')ans+="g";
	    if(s[i]=='m')ans+="l";
	    if(s[i]=='n')ans+="b";
	    if(s[i]=='o')ans+="k";
	    if(s[i]=='p')ans+="r";
	    if(s[i]=='q')ans+="z";
	    if(s[i]=='r')ans+="t";
	    if(s[i]=='s')ans+="n";
	    if(s[i]=='t')ans+="w";
	    if(s[i]=='u')ans+="j";
	    if(s[i]=='v')ans+="p";
	    if(s[i]=='w')ans+="f";
	    if(s[i]=='x')ans+="m";
	    if(s[i]=='y')ans+="a";
	    if(s[i]=='z')ans+="q";
	 }
      }
      cout << "Case #" << k << ": " << ans << endl;
   }
   return 0;
}
