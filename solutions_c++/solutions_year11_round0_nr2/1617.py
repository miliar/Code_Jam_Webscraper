#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#pragma comment (linker, "/STACK:256000000")
using namespace std;
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,q,x,y,i,j;
	cin >> t;
	for (q=1;q<=t;++q) {
		map <string, char> rep;
		set <string> er;
		cin >> x;
		string str;
		for (i=1;i<=x;++i) {
			cin >> str;
			string tmp(str.substr(0,2));
			rep[tmp] = str[2];
			tmp = str[1];
			tmp += str[0];
			rep[tmp] = str[2];
		}
		cin >> y;
		for (i=1;i<=y;++i) {
			cin >> str;
			er.insert(str);
			swap(str[0],str[1]);
			er.insert(str);
		}
		int m;
		cin >> m;
		str="";
		for (i=0;i<m;++i) {
			char ch;
			cin >> ch;
			str += ch;
		}
		char ret[1000]={0};
		int len = 0;
		for (i=0;i<m;++i) {
			ret[len++] = str[i];
			if (len > 1) {
				string tmp;
				tmp += ret[len-1];
				tmp += ret[len-2];
				if (rep.find(tmp)!=rep.end()) {
					ret[len-2] = rep[tmp];
					--len;
				}
				else {
					for (int j = 0; j < len; ++j) {
						string tmp;
						tmp += ret[j];
						tmp += ret[len-1];
						if (er.find(tmp)!=er.end()) {
							len = 0;
							break;
						}
					}
				}
			}
		}
		printf("Case #%d: [",q);
		for (i=0;i<len;++i) {
			printf("%c",ret[i]);
			if (i!=len-1)
				printf(", ");
		}
		printf("]\n");
	}
	
	return 0;
}