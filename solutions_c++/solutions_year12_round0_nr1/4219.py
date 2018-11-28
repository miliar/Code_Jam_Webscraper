/*
#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

char a[30];
bool v[30];
char s[150];
char t[150];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	memset(v, false, sizeof(v));
	memset(a, 0, sizeof(a));
	for (int i = 0; i < 26; i++) a[i] = 'X';

	int n;
	scanf("%d\n", &n);
	while (n--){
		memset(s, 0, sizeof(s));
		memset(t, 0, sizeof(t));
		gets(s); gets(t);

		for (int i = 0; i < (int)strlen(s); i++){
			if ('a' <= s[i] && s[i] <= 'z'){
				a[s[i] - 'a'] = t[i];
				v[t[i] - 'a'] = true;
			}
		}
	}

	for (int i = 0; i < 26; i++){
		if (!v[i]) cout << (char)(i + 'a') << endl;
	}

	cout << "abcdefghijklmnopqrstuvwxyz" << endl;
	for (int i = 0; i < 26; i++){
		//printf("%c", a[i]);
		cout << (char)a[i];
	}
	cout << endl;


	return 0;
}*/

//#pragma warning(disable:4996)
#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

char a[30] = "yhesocvxduiglbkrztnwjpfmaq";
char s[10000];
int n;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	scanf("%d\n", &n);
	for (int i = 0; i < n; i++){
		gets(s);

		for (int j = 0; j < (int)strlen(s); j++){
			if ('a' <= s[j] && s[j] <= 'z'){
				s[j] = a[s[j] - 'a'];
			}
		}

		printf("Case #%d: %s\n", i + 1, s);
	}


	return 0;
}