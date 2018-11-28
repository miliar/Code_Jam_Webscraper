#include <iostream>
#include <string>
using namespace std;

int s2t(string s) {
	return ((s[0]-'0')*10+(s[1]-'0'))*60 + ((s[3]-'0')*10+(s[4]-'0'));
}

void add(int t[], int n, int a[], int addt) {
	fill(a, a+1500, 0);
	for(int i=0;i<n;i++)
		a[t[i]+addt]++;
}

int na, nb;
int at1[100];
int at2[100];
int bt1[100];
int bt2[100];
int t;

void input() {
	cin >> t;
	cin >> na >> nb;
	for(int i=0;i<na;i++) {
		string t1,t2;
		cin >> t1 >> t2;
		at1[i] = s2t(t1);
		at2[i] = s2t(t2);
	}
	for(int i=0;i<nb;i++) {
		string t1,t2;
		cin >> t1 >> t2;
		bt1[i] = s2t(t1);
		bt2[i] = s2t(t2);
	}
}

int as[1500];
int bs[1500];

int ae[1500];
int be[1500];

int main() {
	int casen;
	cin >> casen;
	for(int casei=0;casei<casen;casei++) {
		input();
		add(at1,na, as, 0);
		add(at2,na, ae, t);
		add(bt1,nb, bs, 0);
		add(bt2,nb, be, t);
		
		int ra=0;
		int rb=0;
		
		int ca=0;
		int cb=0;
		for(int i=0;i<1500;i++) {
			cb += ae[i];
			ca += be[i];
			
			if(as[i] > ca) {
				ra += as[i] - ca;
				ca = as[i];
			}
			ca -= as[i];
			if(bs[i] > cb) {
				rb += bs[i] - cb;
				cb = bs[i];
			}
			cb -= bs[i];								
		}
		cout << "Case #" << casei+1 << ": " << ra << " " << rb << endl;
	}
	return 0;
}
