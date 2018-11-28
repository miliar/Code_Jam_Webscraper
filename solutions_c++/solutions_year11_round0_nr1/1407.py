#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
using namespace std;


int main(int argc, char ** argv)
{
#ifdef KOMPA_NA_MISHO
	freopen ("in.txt","r",stdin);
#endif
	/////////////////////////////Code goes here:
	int t=0;
	cin>>t;
	for(int casen=1; casen<=t; casen++){
		int n=0;
		cin>>n;
		vector<int> targets(n);
		vector<int> turns(n);
		vector<vector<int>> trg(2, vector<int>());
		trg[0].push_back(1);
		trg[1].push_back(1);
		for(int i=0; i<n; i++){
			char a=' ';
			while(a==' '){
				cin.get(a);
			}
			cin>>targets[i];
			if(a=='B'){
				turns[i]=0;
			}				
			else{
				turns[i]=1;
			}
			trg[turns[i]].push_back(targets[i]);
			
		}
		int pos[] = {0,0}; //index of last position
		int fint[] ={0,0}; //last time when occupied
		for(int i=0;i<n; i++){
			int turn = turns[i];
			int time_needed ;
			if(pos[turns[i]] == trg[turns[i]].size() - 1)
				time_needed = 0;
			else{
				time_needed = trg[turn][pos[turn]];
				pos[turn]++;
				time_needed-= trg[turn][pos[turn]];
				time_needed =  abs(time_needed);
			}
				
			fint[turn]+= time_needed;
			fint[turn] = max( fint[turn] + 1, fint[!turn] + 1);			
		}
		cout<<"Case #"<<casen<<": "<<max(fint[0], fint[1]) <<endl; 
		//cout<< max(fint[0], fint[1])<<endl;

	}
	//cout<<"-\n";


	////////////////////////////////////////////
#ifdef KOMPA_NA_MISHO
	fclose (stdin);
#endif
	return 0;
}