#include <iostream>
#include <vector>
#include <string>
using namespace std;

int n;
char maping[200];

void initialize() {
     int i;
     string 
            stre = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq",
            strg = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz";
     for (i = 0; i< strg.length(); i++) {
         maping[strg[i]] = stre[i];
     }
     //maping['z'+1] = 0;
     //cout<<maping + 'a'<<endl;
}

void input(int k) {
    string str;
     getline(cin, str);
	int i;
	for (i = 0; i<str.length(); i++) {
        if (str[i] == ' ') continue;
        str[i] = maping[str[i]];
    }
    cout<<"Case #"<<k<<": "<<str<<endl;
}

void process() {
	
}

void output() {

}

int main() {
	int i, t;
	initialize();
	cin >>t;string str;getline(cin, str);
	for (i = 0; i <t; i++) {
		input(i+1);
		process();
		output();
	}
	return 0;
}
