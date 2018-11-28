/*
 * Tongue2012A.cpp
 *
 *  Created on: Apr 14, 2012
 *      Author: batchunag
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <map>
#include <utility>
#include <stdio.h>
#include <string.h>
#include <list>
#define FOR(i,a,b) for (int i=a; i<b; i++)
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define mp make_pair
#define pb push_back

using namespace std;
typedef vector<int> VI;
typedef pair <int,int> PII;

int main(){
	FILE *out=fopen("answer.txt","w");
	ifstream in ("input.txt");
	string a[3],c[3];
	map <char, char> table;
	for (int i=0; i<26; i++)
		table.insert(make_pair<char, char>('a'+i,'a'+i));
	a[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	a[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	a[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	c[0]="our language is impossible to understand";
	c[1]="there are twenty six factorial possibilities";
	c[2]="so it is okay if you want to just give up";
	for (int i=0; i<3; i++){
		for (int j=0; j<a[i].length(); j++){
			table[a[i][j]]=c[i][j];
		}
	}
	table['q']='z';
	table['z']='q';
	int t;
	in>>t;
	getline (in,a[0]);
	for (int i=1; i<=t; i++){
		fprintf(out,"Case #%d: ",i);
		getline (in,a[0]);
		for (int j=0; j<a[0].length(); j++){
			if (a[0][j]!=' ') fprintf(out,"%c",table[a[0][j]]);
			else fprintf(out," ");
		}
		fprintf(out,"\n");
	}
	return 0;
}
