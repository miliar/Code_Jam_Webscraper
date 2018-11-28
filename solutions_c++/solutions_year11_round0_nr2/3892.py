#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <map>
#include <algorithm>
#include <string>

using namespace std;

int MAXN = 1000;

int char_to_int(char x){
  return int(x) - int('A');
}

int main(){
  map<string,string> comb;
  map<char,char>   opp;
  map<char,int>   kartai;
  
   freopen("magica.in", "r", stdin);
   freopen("magica.out", "w", stdout);
   
   int testcases, pries, kartu, ilgis;
   string s, galutine, s1, s2, last;
   
   scanf("%d\n", &testcases);
   
   for(int test = 0; test < testcases; test++){
     comb.clear();
     kartai.clear();
     opp.clear();
     scanf("%d", &kartu);
     for(int i = 0; i < kartu; i++){
       cin >> s;
       s1 = "";
       s1 += s[0];
       s1 += s[1];
       s2 = "";
       s2 += s[1];
       s2 += s[0];
       comb[s1 ] = s[2];
       comb[s2] = s[2];
       }
       scanf("%d", &pries);
     for(int i = 0; i < pries; i++){
       cin >> s;
       opp[s[0]] = s[1];
       opp[s[1]] = s[0];
       }
     
     cin >> ilgis >> s;
     galutine = s[0];
     kartai[ s[0] ]++;
     
     for(int i = 1; i < ilgis; i++){
       kartai[s[i]]++;
       galutine += s[i];
       
       //cout << "Ta prasme: " << galutine << endl;
       
       last = "";
       last += galutine[galutine.length()-2];
       last += galutine[galutine.length()-1];
       while( comb[ last ] != ""){
	  kartai[galutine[galutine.length()-2]]--;
	  kartai[galutine[galutine.length()-1]]--;
	  galutine.erase(galutine.length()-2, 2);
	  galutine += comb[ last ];
	  
       last = "";
       last += galutine[galutine.length()-2];
       last += galutine[galutine.length()-1];
       
       if( kartai[ opp[ comb[ last ][0] ] ] > 0){	//B - buvo
	    kartai.clear();
	    galutine = "";
	    } 
      }
	 //cout << "Ta: " << galutine << " " << galutine[galutine.length()-1] << endl;
       if( kartai[ opp[ galutine[galutine.length()-1] ] ] > 0){	//B - buvo
	    kartai.clear();
	    galutine = "";
	    }
       }
     printf("Case #%d: [", test+1);  
     for(int j = 0; j < galutine.length(); j++)
       if(j + 1 != galutine.length())
	  printf("%c, ", galutine[j]);
       else
	  printf("%c", galutine[j]);
    printf("]\n");
  }
   
   return 0;
}