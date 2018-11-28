/*
 * Author: NomadThanatos
 * Created Time:  2012/4/14 14:13:50
 * File Name: A.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <map>
#include <set>

using namespace std;

#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())

const int MAXINT = -1u>>1;

const int MAXN = 150;

const string f = "yhesocvxduiglbkrztnwjpfmaq";

char buff[MAXN];
char out[MAXN];

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,ca = 1;
	scanf("%d\n",&T);
	while(gets(buff)) {
		int len = strlen(buff);
		for(int i = 0 ; i < len ; i++) {
			if (buff[i] == ' ') {
				out[i] = ' ';
			}
			else {
				out[i] = f[buff[i] - 'a'];
			}
		}
		out[len] = '\0';
		printf("Case #%d: %s\n",ca,out);
		ca++;
	}

    return 0;
}

