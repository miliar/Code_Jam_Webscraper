//*****Template*****//
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cassert>
#include <vector>
#include <cstdio>
#include <string>
#include <cmath>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <utility>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <numeric>
#include <iterator>
#include <functional>

#define INF 987654321
#define ll long long
#define rep0N(i,n) for(int i = 0;i < n;i++)
#define repN0(i,n) for(int i = n-1;i >= 0;i--)
#define repij(i,j,n) for(int i = j;j < n;i++)
#define pb(a) push_back(a)
#define si(a) scanf("%d",&a)
#define pi(a) printf("%d",a)

using namespace std;

int Z = 0;

int chaat(vector<vector<char>> Burr,int p, int q, char c) {
	int cunt = 0;
	for(int i = 0; i < 4; i++){
		if(Burr[i][q] == c || Burr[i][q] == 'T'){
			cunt++;
			if(cunt == 4)
				return cunt;
		}
		else
			break;
	}
	cunt = 0;
	for(int i = 0; i < 4; i++){
		if(Burr[p][i] == c || Burr[p][i] == 'T'){
			cunt++;
			if(cunt == 4)
				return cunt;
		}
		else
			break;
	}
	cunt = 0;
	if(p == q){
		if((Burr[0][0] == c || Burr[0][0] == 'T') && (Burr[1][1] == c || Burr[1][1] == 'T') && (Burr[2][2] == c || Burr[2][2] == 'T') && (Burr[3][3] == c || Burr[3][3] == 'T')){
			cunt = 4;
			return cunt;
		}
	}
	if((p == 1 && q==2) || (p==2 && q==1) || (p==3 && q==0) || (p==0 && q==3)){
		if((Burr[3][0] == c || Burr[3][0] == 'T') && (Burr[2][1] == c || Burr[2][1] == 'T') && (Burr[1][2] == c || Burr[1][2] == 'T') && (Burr[0][3] == c || Burr[0][3] == 'T')){
			cunt = 4;
			return cunt;
		}
	}
	return 0;
}

int main(){
	int test,X;
	vector<int>ZX;
	cin>>test;
	for(int Y = 1; Y <= test; Y++){
	    vector<int> V4;
		int E1,Ax,Ao;
		E1 = Ax = Ao = 0;
		char choor,bv;
		vector<vector<char> >Arr(4,vector<char>(4,'c'));
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> choor;
				Arr[i][j] = choor;
			}
		}
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(Arr[i][j] == '.')
					E1 = 1;
				if(Arr[i][j] == 'X')
					Ax = chaat(Arr,i,j,Arr[i][j]);
				if(Arr[i][j] == 'O')
					Ao = chaat(Arr,i,j,Arr[i][j]);
			}
			if(Ax == 4 || Ao == 4)
				break;
		}
        if(Ax == 4)
			cout<<"Case #"<<Y<<": "<< "X won"<<endl;
        if(Ao == 4)
            cout <<"Case #"<<Y<<": "<< "O won" << endl;
        if(Ax != 4 && Ao != 4) {
			if(E1 == 1)
				cout<<"Case #"<<Y<<": "<<"Game has not completed"<<endl;
		}
		if(Ax != 4 && Ao != 4){
			if(E1 == 0)
				cout <<"Case #"<<Y<<": "<< "Draw" << endl;
		}
	}
	return 0;
}

