#include <cstdio>
#include <string>
#include <vector>
using namespace std;

string naukaSzyfr[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
 
string naukaRozszyfr[] = {"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"}; 

char mapka[30];	
char amapka[30];	

int main() {
	for(int i=0;i<30;i++) {mapka[i] = -1;amapka[i]=-1;}
	mapka['z'-'a'] = 'q';
	amapka['q'-'a'] = 'z';
	mapka['q'-'a'] = 'z';
	amapka['z'-'a'] = 'q';
	for(int i=0;i<3;i++) {
		for(int i2=0;i2<naukaSzyfr[i].size();i2++) if(naukaSzyfr[i][i2]!= ' ') {
			//printf("%c %d %c %d, ", naukaSzyfr[i][i2] , (int)naukaSzyfr[i][i2]-'a', naukaRozszyfr[i][i2],(int)naukaRozszyfr[i][i2]-'a');
			mapka[(int)naukaSzyfr[i][i2]-'a'] = naukaRozszyfr[i][i2];
			amapka[(int)naukaRozszyfr[i][i2]-'a'] = naukaSzyfr[i][i2];
		}
	}
	//for(int i=0;i<='z'-'a';i++) if(mapka[i] == -1) printf("%c",i+'a');
	//for(int i=0;i<='z'-'a';i++) if(amapka[i] == -1) printf("Bez wchodz¹cej %c",i+'a');
	
	int t,d;scanf("%d\n",&t);
	for(int d=1;d<=t;d++) {
		char text[1000];
		string s;
		gets(text);
		//scanf("%s",text);
		s = text;
		for(int i=0;i<s.size();i++) if(s[i]!=' ') s[i] = mapka[s[i]-'a'];
		printf("Case #%d: %s\n",d,s.c_str());
	}
	return 0;
}
