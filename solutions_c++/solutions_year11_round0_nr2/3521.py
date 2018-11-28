//      B.cpp
//      
//      Copyright 2011 Kushagra Gour a.k.a. Chin Chang <chinchang457@gmail.com>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int indexOf(vector<string> v, string s){
	int l=v.size(); //cout<<l;
	for(int i=0;i<l;i++){
		if(v[i]==s) return i;
	}
	return -1;
}

int combineCheck(vector<string> v, char a, char b){
	string s="";
	int p;
	s+=a; s+=b;
	p = indexOf(v,s);
	if(p==-1){
		s=""; s+=b; s+=a;
		p = indexOf(v,s);
	}
	return p;
}

bool opposeCheck(vector<string> v, vector<char> seq, char c){
	for(int i=0;i<seq.size();i++){
		int pos = combineCheck(v,c,seq[i]);
		if(pos!=-1) return true;
	}
	return false;
}

int main(int argc, char** argv)
{
	FILE *f,*fo;
	f=fopen("B-large.in","r");
	fo=fopen("B_large_out.text","w");
	int t,c,d,n;
	fscanf(f,"%d",&t);
	for(int test=0;test<t;test++){
		vector<string> combine;
		vector<char> form;
		vector<string> oppose;
		
		char str[4];
		string s="",seq;
		 
		fscanf(f,"%d ",&c); //cout<<c;
		for(int i=0;i<c;i++){
			fscanf(f,"%s ",str);
			s=""; s+=str[0]; s+=str[1]; //cout<<s<<" ";
			combine.push_back(s); form.push_back(str[2]);
		}
		
		
		
		fscanf(f,"%d ",&d);
		for(int i=0;i<d;i++){
			fscanf(f,"%s ",str); //cout<<str<<" ";
			s=""; s+=str[0]; s+=str[1]; //cout<<s<<" ";
			oppose.push_back(s);
		}
		
		fscanf(f,"%d ",&n);
		vector<char> st;
		char ch;
		for(int i=0;i<n;i++){
			fscanf(f,"%c",&ch); //cout<<ch;
			if(!st.empty()){
				int pos = combineCheck(combine,ch,st.back());
				if(pos!=-1){
					st.pop_back();
					st.push_back(form[pos]);
				}
				else if(opposeCheck(oppose,st,ch)){
					st.clear();
				}
				else{
					st.push_back(ch);
				}			
			}
			else{
				st.push_back(ch);
			}
			
			
		}
		
		fprintf(fo,"Case #%d: [",test+1);
		for(int i=0;i<st.size();i++){
			(i==(st.size()-1)) ? fprintf(fo,"%c",st[i]) : fprintf(fo,"%c, ",st[i]);
		}
		fprintf(fo,"]\n");
		
	}
	return 0;
}
