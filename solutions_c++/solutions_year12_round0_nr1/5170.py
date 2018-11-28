#include<iostream>
#include<map>
#include<string>
using namespace std;

map<char,char>convert;

string alphabet = "abcdefghijklmnopqrstuvwxyz";

string ta = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";

string tb = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";

void make(){

   //cout << "alphabet = " << alphabet.size() << endl;
   bool f1[26];
   bool f2[26];
   for(int i = 0 ; i < 26 ; i++)f1[i] = f2[i] = false;

   convert['a'] = 'y';
   convert['o'] = 'e';
   convert['z'] = 'q';

   f1['a'-'a'] = f2['y' - 'a'] = true;
   f1['o'-'a'] = f2['e' - 'a'] = true;
   f1['z'-'a'] = f2['q' - 'a'] = true;
   

   for(int i = 0 ; i < ta.size() ; i++){
      if(!isalpha(ta[i]))continue;
      convert[ta[i]] = tb[i];
      f1[ta[i]-'a'] = f2[tb[i]-'a'] = true;
   }

   int a,b;
   for(int i = 0 ; i < alphabet.size() ; i++){
      if(!f1[i]){
	 a = i;
	 break;
      }
   }

   for(int i = 0 ; i < alphabet.size() ; i++){
      if(!f2[i]){
	 b = i;
	 break;
      }
   }

   convert[alphabet[a]] = alphabet[b];

   /*
   cout << convert.size() << endl;
   map<char,char>::iterator it = convert.begin();
   for( ;it != convert.end() ; it++){
      cout << it->first << ' ' << it->second << endl;
   }
   */
}

int main(){
   make();
   string str;
   int n;
   cin >> n;
   getline(cin,str);
   for(int i = 0 ; i < n ; i++){
      getline(cin,str);
      cout << "Case #" << i+1 << ": ";
      for(int j = 0 ; j < str.size() ; j++){
	 if(isalpha(str[j])){
	    cout << convert[str[j]];
	 }
	 else cout << str[j];
      }
      cout << endl;
   }
   return 0;
}
