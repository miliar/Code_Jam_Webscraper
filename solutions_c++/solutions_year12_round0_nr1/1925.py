#include<iostream>
#include <string.h>
using namespace std; 

int main(){
	/*char* a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
	char* b = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";*/
	char * c = "yhesocvxduiglbkrztnwjpfmaq";
	char map[30];
	/*for (int i = 0; i < strlen(a); i++){
		map[a[i]-'a'] = b[i];
	}
	map[25] = 'q';
	map['q'-'a'] = 'z';
	for (int i = 0; i < 26; i++) {
		printf("%c", map[i]);
	}
	printf("\n");*/
	freopen("C:\\Documents and Settings\\mqiao\\My Documents\\Downloads\\A-small-attempt1.in", "r", stdin); 
	freopen("C:\\Documents and Settings\\mqiao\\My Documents\\Downloads\\aout.txt","w",stdout); 
	int n;
	char a[19999]; 
	cin >> n; 
	cin.getline(a,19999,'\n');
	for (int i =0; i < n; i++) {
		cin.getline(a,19999,'\n');
		cout <<"Case #"<<i+1<<": ";
		for (int j = 0; j < strlen(a); j++) {
			if (a[j] == ' ') cout <<" "; 
			else cout<< c[a[j]-'a']; 
		}
		cout << endl;
	}
	fclose(stdin); 
	fclose(stdout); 
}