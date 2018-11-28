#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

#define ll long long
#define pi pair<int,int>
#define X first 
#define Y second
#define pb push_back
#define ab(x) ((x)<0?(-(x)):(x))
#define xx(x) ((x)*(x))
#define D 1000000007
#define Max (1<<30)
#define LLMAX (1ll<<60)
#define mp make_pair
#define MM 1000000000000000000ll
#define pss pair<string,string>
#define psi pair<string,int>
#define NN 3


char a[55][55];
int n=4;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	int CC=0;
	while(t--){
		CC++;
		for(int i=1;i<=n;i++)for(int j=1;j<=n;j++)cin>>a[i][j];


		bool X,O;
		X=O=0;
		int C=0;
		for(int i=1;i<=n;i++){
			int cntX1=0;
			int cntO1=0;
			int cntX2=0;
			int cntO2=0;
			int cntX3=0;
			int cntO3=0;
			int cntX4=0;
			int cntO4=0;

			for(int j=1;j<=n;j++){
				if(a[i][j]=='.')C++;

				if(a[i][j]=='X')cntX1++;
				if(a[i][j]=='O')cntO1++;
				if(a[j][i]=='X')cntX2++;
				if(a[j][i]=='O')cntO2++;
				
				if(a[i][j]=='T')cntX1++,cntO1++;
				if(a[j][i]=='T')cntX2++,cntO2++;
				
				if(a[j][j]=='X')cntX3++;
				if(a[j][j]=='O')cntO3++;
				if(a[j][j]=='T')cntX3++,cntO3++;

				
				if(a[j][5-j]=='X')cntX4++;
				if(a[j][5-j]=='O')cntO4++;
				if(a[j][5-j]=='T')cntX4++,cntO4++;

			}
			
			if(cntX1==4 || cntX2==4)X=1;
			if(cntO1==4 || cntO2==4)O=1;
			if(cntX3==4 || cntX4==4)X=1;
			if(cntO3==4 || cntO4==4)O=1;
		}

		cout<<"Case #";
		cout<<CC;
		cout<<": ";

		if(X)cout<<"X won";
		else if(O)cout<<"O won";
		else if(C)cout<<"Game has not completed";
		else cout<<"Draw";

		cout<<endl;
	}

}