/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) Albert Bendicho 2011 <albert.codejam@mailinator.com>
 * 
 */

#include<fstream>
#include<stack>
#include<set>
#include<map>
#include<string>
using namespace std;

int main()
{
	fstream fin ("B-large.in", fstream::in);
	fstream fout ("B-large.out", fstream::out);
	int t;
	
	fin>>t;
	for (int it=0; it<t ; it++) {
		int c,d,n;
		stack<char> elems;
		map<string,char> combine;
		set<string> destroy;
		map<char,int> appears;
		fin>>c;
		for (int ic=0; ic<c; ic++) {
			string comb;
			char c[2],r;
			fin>>comb;
			c[0]=comb[0];
			c[1]=comb[1];
			r=comb[2];
			combine[c]=r;
			c[0]=comb[1];
			c[1]=comb[0];
			r=comb[2];
			combine[c]=r;
		}
		fin>>d;
		for (int id=0; id<d; id++) {
			string dest;
			fin>>dest;
			destroy.insert(dest);
			char t;
			t=dest[0];
			dest[0]=dest[1];
			dest[1]=t;
			destroy.insert(dest);
		}
		fin>>n;
		string s;
		fin>>s;
		for (int in=0; in<n; in++) {
			if (elems.empty()) {
				elems.push(s[in]);
				appears[s[in]]++;
			} else {
				map<string,char>::iterator combit;
				char last2[2];
				last2[0]=elems.top();
				last2[1]=s[in];
				combit=combine.find(last2);
				if (combit!=combine.end()) {
					appears[elems.top()]--;
					if (appears[elems.top()]==0) appears.erase(elems.top());
					elems.pop();
					elems.push(combit->second);
					appears[elems.top()]++;
				} else {
					map<char,int>::iterator ite;
					set<string>::iterator destit;
					bool found=false;
					for ( ite=appears.begin() ; (ite != appears.end()) && (!found); ite++ ) {
						string ls;
						ls.push_back(ite->first);
						ls.push_back(s[in]);
						destit=destroy.find(ls);
						if (destit==destroy.end()) found=false; else found=true;
						}
					if (found) {
						appears.clear();
						while (!elems.empty()) elems.pop();
					} else {
						elems.push(s[in]);
						appears[s[in]]++;
					}
				}
			}
		}	
		fout<<"Case #"<<it+1<<": [";
		stack<char> relems;
		while (!elems.empty()) {
			relems.push(elems.top());
			elems.pop();
		}
		while (relems.size()>1) {
		    fout<<relems.top()<<", ";
			relems.pop();
		};
		if (!relems.empty()) {
			fout<<relems.top();
		}
		fout<<"]"<<endl;
	}
	return 0;
}