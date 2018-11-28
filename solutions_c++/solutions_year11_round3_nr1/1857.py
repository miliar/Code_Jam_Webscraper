/*
 * TheSquareTiles.cpp
 *
 *  Created on: May 22, 2011
 *      Author: batchunag
 */

#include <iostream>
#include <algorithm>
#include <vector>
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
	freopen("input.txt","r",stdin);
	freopen("answer.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=1; t<=T; t++){
		cout<<"Case #"<<t<<":"<<endl;
		int R,C;
		cin>>R>>C;
		string S[50];
		for (int r=0; r<R; r++)
			cin>>S[r];
		int b=1;
		for (int r=0; r<R; r++)
			for (int c=0; c<C; c++){
				if (S[r][c]=='#'){
					if (S[r][c+1]=='#'&&S[r+1][c]=='#'&&S[r+1][c+1]=='#'){
						S[r][c]='/';
						S[r][c+1]='\\';
						S[r+1][c]='\\';
						S[r+1][c+1]='/';
					}
					else {
						r=R;
						c=C;
						b=0;
					}
				}
			}
		if (b==1){
			for (int r=0; r<R; r++)
				cout<<S[r]<<endl;
		}
		else cout<<"Impossible"<<endl;
	}
	return 0;
}
