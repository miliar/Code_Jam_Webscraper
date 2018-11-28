#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;


map<pair<char,char>,char> trans;
set<string> oppos;

char resl;
char res[1000];

map<char,int> elcount;

int main() {
	int t,c,d,n;
	cin>>t;
	
	int casen=1;
	
	while(t--) {
		// read
		resl=0;
		trans.clear();
		oppos.clear();
		elcount.clear();
		cin>>c;
		string in;
		for (int i=0;i<c;i++) {
			cin>>in;
			trans[pair<char,char>(in[0],in[1])]=in[2];
			trans[pair<char,char>(in[1],in[0])]=in[2];
		}
		cin>>d;
		for (int i=0;i<d;i++) {
			cin>>in;
			char cc[3];cc[0]=in[1];cc[1]=in[0];cc[2]=0;
			string in2=cc;
			
			oppos.insert(in);
			oppos.insert(in2);
		}

		cin>>n;
		cin>>in;
		
		for (int i=0;i<n;i++) {
			if (resl>0) {
				pair<char,char> pcc=pair<char,char>(res[resl-1],in[i]);
				char t=trans[pcc];
				
				if (t!=0) {
					elcount[res[resl-1]]--;
					res[resl-1]=t;
				} else {
					// check oppose
					bool found=false;
					
					for (map<char,int>::iterator it=elcount.begin();it!=elcount.end();it++) {
						if (it->second>0) {
							
							char cc[3];cc[0]=it->first;cc[1]=in[i];cc[2]=0;
							string s=cc;
							
							if (oppos.find(s)!=oppos.end()) {
								found=true;
								break;
							}
						}
					}
					
					if (found) {
						resl=0;
						elcount.clear();
					} else {
						res[resl]=in[i];
						resl++;
						elcount[in[i]]++;
					}
				}
				
			} else {
				res[resl]=in[i];
				resl++;
				elcount[in[i]]++;
			}
		}
		
		//
		printf("Case #%d: ",casen);
		//print result
		cout<<"[";
		for (int i=0;i<resl;i++) {
			if (i!=0) cout<<", ";
			cout<<res[i];
		}
		cout<<"]";
		printf("\n");
		casen++;
	}
}
