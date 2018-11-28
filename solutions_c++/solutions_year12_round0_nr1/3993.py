#include <iostream>
#include <string>

using namespace std;

int main()
{
	freopen("A-small-attempt2.in" ,"r",stdin);
	freopen("A-small-attempt2.out" ,"w" ,stdout);
	string stri1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string stri2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    string stri3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    string stro1 = "our language is impossible to understand";
   	string stro2 = "there are twenty six factorial possibilities";
	string stro3 = "so it is okay if you want to just give up";
	char mmap[26];
	mmap['z'-'a'] = 'q';
	mmap['q'-'a'] = 'z';
	for (int i = 0 ;i < stri1.length() ;++i){
		if (stri1[i] != ' '){
			mmap[stri1[i] - 'a'] = stro1[i];
		}
	}
	for (int i = 0 ;i < stri2.length() ;++i){
		if (stri2[i] != ' '){
			mmap[stri2[i] - 'a'] = stro2[i];
		}
	}
	for (int i = 0 ;i < stri3.length() ;++i){
		if (stri3[i] != ' '){
			mmap[stri3[i] - 'a'] = stro3[i];
		}
	}
	int T;
	char ch;
	cin >> T;
	getchar();
	char buf[256];
	for (int i = 0 ;i < T ;i++){
		cin.getline(buf ,256);
		for (int l = 0 ;l < strlen(buf) ;++l){
			if ( 'a' <= buf[l] && buf[l] <= 'z')
				buf[l] = mmap[buf[l]-'a']; 
		}
		cout << "Case #" << i + 1 << ": "<< buf << endl;
	}
}
