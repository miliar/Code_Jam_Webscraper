#include <iostream>
#include <cstring>
using namespace std;

int k;
char s[50000];
int len;

void input() {
	cin >> k >> s;
	len = strlen(s);
}



bool v[16];
int his[16];

int minr;

char ns[50000];

void change() {
	for(int i=0;i<len;i++)
		ns[i] = s[(i/k)*k + his[i%k]];
}

int count() {
	int r = 1;
	for(int i=1;i<len;i++) {
		if(ns[i] != ns[i-1])
			r++;
	}
	return r;
}

void go(int cnt) {
	if(cnt == k) {
		change();
		minr = min(minr , count());
		
	} else {
		for(int i=0;i<k;i++) {
			if(!v[i]) {
				v[i] = true;
				his[cnt] = i;
				go(cnt+1);				
				v[i] = false;
			}
		}		
	}
}



int main() {
	int casen;
	cin >> casen;
	for(int casei=1;casei<=casen;casei++) {
		input();
		
		fill(v, v+k, false);
		
		minr = 1000000000;
		
		go(0);
		
		cout << "Case #" << casei << ": " << minr << endl;			
		
		
	}
	return 0;
}
