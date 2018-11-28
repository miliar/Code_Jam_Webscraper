#include <stdio.h>
#include <stdlib.h>

#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;


vector< pair<char,int> > commands;
int n;

int getCommand(char bot, int from, int *newcommand) {
	for (int i=from;i<n;i++) {
		if (commands[i].first==bot) {
			*newcommand=commands[i].second;
			return i;
		}
	}
	*newcommand=-1;
	return n;
}

int execute() {
	int done=0;
	int time=0;
	
	int poso=1;
	int posb=1;
	
	int exeo=0;
	int exeb=0;
	
	int como=-1;
	int comb=-1;
	while (exeo<n||exeb<n) {
		if (como==-1) exeo=getCommand('O', exeo, &como);
		if (comb==-1) exeb=getCommand('B', exeb, &comb);
		
//		cout<<"Time "<<time+1<<" ";
		
		if (como!=-1) {
			if (como==poso&&exeo<exeb) {
				como=-1;
//				printf("press   %d ",poso);
			} else {
				if (como<poso) {
					poso--; 
//					printf("move to %d ",poso);
				}
				if (como>poso) {
					poso++; 
//					printf("move to %d ",poso);
				}
			}
		}
		
		if (comb!=-1) {
			if (comb==posb&&exeo>exeb) {
				comb=-1;
//				printf("press   %d ",posb);
			} else {
				if (comb<posb) {
					posb--; 
//					printf("move to %d ",posb);
				}
				if (comb>posb) {
					posb++; 
//					printf("move to %d ",posb);
				}
			}
		}
//		printf("\n");
		
		if (como==-1) exeo++;
		if (comb==-1) exeb++;
		
		time++;
	}
	return time;
}


int main() {
	int k, t;
	cin>>t;
	int c=1;
	while(t--) {
		// compute
		cin>>n;
		commands.clear();
		int time;
		for (int i=0;i<n;i++) {
			string c;
			int but;
			cin>>c>>but;
			commands.push_back(pair<char,int>(c[0],but));
		}
		time=execute();

		//
		printf("Case #%d: %d",c, time);
		//print result
		
		printf("\n");
		c++;
	}
}
