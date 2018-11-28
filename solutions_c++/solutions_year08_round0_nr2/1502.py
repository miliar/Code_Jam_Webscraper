// B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

typedef pair<int,int> pairint;

int _tmain(int argc, _TCHAR* argv[])
{
	int n, ncases, z, i, j, k, t, nAB, nBA, nA, nB, h1, h2, m1, m2, current, na, nb;
	map<pairint,int> AB, BA;
	map<pairint,int>::iterator it, it2;
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	char c;
	fin>>ncases;
	for(z=0;z<ncases;z++){
		AB.clear(); BA.clear();
		fin>>t>>nAB>>nBA;
		na=0; nb=0;
		for(i=0;i<nAB;i++){
			fin>>h1;
			h1*=60;
			fin>>c>>m1;
			h1+=m1;

			fin>>h2;
			h2*=60;
			fin>>c>>m2;
			h2+=m2;
			AB[pairint(h1,h2)]++;
			na++;
			//AB.insert(pairint(h1,h2));
			//if(z<5) cout<<h1<<" "<<h2<<endl;
			//cout<<AB[i].first<<" "<<AB[i].second<<endl;
		}

		for(i=0;i<nBA;i++){
			fin>>h1;
			h1*=60;
			fin>>c>>m1;
			h1+=m1;

			fin>>h2;
			h2*=60;
			fin>>c>>m2;
			h2+=m2;
			nb++;
			//if(z<5) cout<<h1<<" "<<h2<<endl;
			BA[pairint(h1,h2)]++;
		//	BA.insert(pairint(h1,h2));
		}
		nA=0;
		nB=0;
		while(na+nb>0){
			if(na==0){
				nB+=nb;
				break;
			}else if(nb==0){
				nA+=na;
				break;
			}
			//cout<<"one";
			if(AB.begin()->first<BA.begin()->first){
				current=0;
				it=AB.begin();
				nA++;
				//cout<<"A";
				//if(it!=AB.end()) AB.erase(it);
			}else{
				current=1;
				it=BA.begin();
				nB++;
				//cout<<"B";
				//if(it!=BA.end()) BA.erase(it);
			}
			/*if(current==1){
				if(it!=BA.end()) BA.erase(it);
			}else{
				if(it!=AB.end()) AB.erase(it);
			}*/
			
			while(1){
		//		if(AB.size()==0||BA.size()==0) break;
				cout<<na<<" "<<nb<<endl;
				
				if(current==0){
					//cout<<"three";
					if(nb>0) it2=BA.lower_bound(pairint(it->first.second+t,0));
					//it2=BA.end();
					it->second--;
					if(it->second==0) AB.erase(it);
					na--;
					if(nb==0) break;
					if(it2==BA.end()){
						break;
					}else{
						it=it2;
						current=1;
					}
				}else{
				//	cout<<"four";

					if(na>0) it2=AB.lower_bound(pairint(it->first.second+t,0));
					//it2=AB.end();
					it->second--;
					if(it->second==0) BA.erase(it);
					nb--;
					//cout<<"four";
					if(na==0) break;
					if(it2==AB.end()){
						break;
					}else{
						it=it2;
						current=0;
					}
					//cout<<"four";
				}
				//cout<<"two";
			}
		}
		fout<<"Case #"<<z+1<<": "<<nA<<" "<<nB<<endl;
		
		cout<<"Case #"<<z+1<<": "<<nA<<" "<<nB<<endl;
					
		

//		for(it=AB.begin();it!=AB.end();it++){
//			cout<<it->first<<" "<<it->second<<endl;
//		}


	}
	return 0;
}

