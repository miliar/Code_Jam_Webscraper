// A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
//#include <string>
#include <set>

using namespace std;

int a(int n){
	if(n<0) return -n;
	return n;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	set<int>::iterator it, tempit;
	int i, j, k, n, m, t, z, p, l;
	int malt[2001];
	int nreq[2001];
	int treq;
	set<int> S[2001];
	int nflav, ncust;

	fin>>z;
	for(k=1;k<=z;k++){
		fin>>nflav>>ncust;
		treq=0;
		for(i=1;i<=ncust;i++){
			S[i].clear();
			fin>>nreq[i];
			for(j=1;j<=nreq[i];j++){
				fin>>t;
				fin>>l;
				if(l) t=-t;
				S[i].insert(t);
				treq++;
			}
		}

		for(i=1;i<=nflav;i++){
			malt[i]=-1;
		}
		p=1;
		while(treq>0){
			if(k==1){
			for(i=1;i<=nflav;i++){
				if(malt[i]==1){
					cout<<"1 ";
				}else if(malt[i]==0){
					cout<<"0 ";
				}
				else cout<<"a ";
			}
			cout<<endl;
			}
			t=treq;
			for(i=1;i<=ncust;i++){
				if(S[i].size()==0){
				}else if(S[i].size()==1){
					//if(k==1) cout<<"yay";
					if((*S[i].begin()>0&&malt[a(*S[i].begin())]==1)||(*S[i].begin()<0&&malt[a(*S[i].begin())]==0)){
						p=0;
						break;
					}
					if(k==1) cout<<"yay";
					if(*S[i].begin()>0){
						malt[a(*S[i].begin())]=0;
					}else{
						malt[a(*S[i].begin())]=1;
					}
					S[i].clear();
					treq--;
				}else{
					for(it=S[i].begin();it!=S[i].end();){
						if(malt[a(*it)]!=-1){
							if((*it>0&&malt[a(*it)]==1)||(*it<0&&malt[a(*it)]==0)){
								tempit=it;
								it++;
								S[i].erase(tempit);
								treq--;
								if(S[i].size()==0){
									p=1;
									break;
								}
							}else{
								treq-=S[i].size();
								S[i].clear();
								break;
							}
						}else{
							it++;
						}
					}
				}


			}
		if(k==1) cout<<treq;

			if(t==treq||p==0) break;
			
		}


		fout<<"Case #"<<k<<": ";
		if(p){
			for(i=1;i<=nflav;i++){
				if(malt[i]==1){
					fout<<"1 ";
				}else{
					fout<<"0 ";
				}
			}
		}else{
			fout<<"IMPOSSIBLE";
		}
		fout<<endl;


	}

	return 0;
}

