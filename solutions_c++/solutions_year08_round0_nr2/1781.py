#include <stdio.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <cctype>
#include <math.h>
using namespace std;

typedef struct{
	int go,arrive,bol;
} data;

int n,t,useA,useB;
int na,nb;
vector<data> A,B;

bool cf(const data a,const data b){
	if( a.arrive!=b.arrive)  return a.arrive<b.arrive;	
						return a.go<b.go;
}

vector<int> greed(int lastmin,int bol){
	int i;
	vector<int> temp(0);
	
	if (bol==0){
		for (i=0;i<na;i++){
			if (A[i].go>=lastmin && !A[i].bol){
				temp=greed(A[i].arrive+t,1);
				temp.push_back(i);
				return temp;
			}
		}
		return temp;
	}
		for (i=0;i<nb;i++){
			if (B[i].go>=lastmin && !B[i].bol){
				temp=greed(B[i].arrive+t,0);
				temp.push_back(i);
				return temp;
			}	
		}
		return temp;
}

vector<data> baca(int size){
	vector<data> A(size);
	string s1,s2,lala;
	int temp;
	int i;
	
	for (i=0;i<size;i++){
		cin>> s1 >> s2;
		lala.assign(s1,0,2);
		if (lala[0]=='0') lala.assign(lala,1,1);
		//cout << lala << endl;
		sscanf(lala.c_str(),"%d",&A[i].go);
		lala.assign(s1,3,2);
		if (lala[0]=='0') lala.assign(lala,1,1);
		//cout << lala << endl;
		A[i].go*=60;
		sscanf(lala.c_str(),"%d",&temp);
		A[i].go+=temp;
		
		lala.assign(s2,0,2);
		if (lala[0]=='0') lala.assign(lala,1,1);
		//cout << lala << endl;
		sscanf(lala.c_str(),"%d",&A[i].arrive);
		lala.assign(s2,3,2);
		if (lala[0]=='0') lala.assign(lala,1,1);
		//cout << lala << endl;
		A[i].arrive*=60;
		sscanf(lala.c_str(),"%d",&temp);
		A[i].arrive+=temp;
		A[i].bol=0;
	}
	sort(A.begin(),A.end(),cf);
	return A;
}

int main(){
	int i,j,k,l;
	char dumi;
	
	scanf("%d",&n);
	for (i=0;i<n;i++){
		scanf("%d",&t);
		scanf("%d %d%c",&na,&nb,&dumi);
		A=baca(na);
		B=baca(nb);
		useA=0;
		useB=0;
		
		for (j=0;j<na+nb;j){
			vector<int> trackA;
			vector<int> trackB;
			
			for (k=0;k<na;k++) if (!A[k].bol) break;
			if (k<na) {
				trackA=greed(A[k].arrive+t,1);
				trackA.push_back(k);
			}
			
			for (k=0;k<nb;k++) if (!B[k].bol) break;
			if (k<nb) {
				trackB=greed(B[k].arrive+t,0);
				trackB.push_back(k);
			}
			
			//puts("syalalalla");
			/*printf("%d %d %d %d\n",trackA.size(),trackB.size(),na,nb);
			for (k=0;k<trackA.size();k++){
				printf("%d\n",trackA[k]);	
			}
			for (k=0;k<trackB.size();k++){
				printf("%d\n",trackB[k]);
			}*/
			if (trackA.size()>trackB.size()){
				useA++;
				for (k=trackA.size()-1,l=0;k>=0;k--,l++) {
					(l%2==0) ? A[trackA[k]].bol=1:B[trackA[k]].bol=1;
				}
				j+=trackA.size();
			} else {
				useB++;
				for (k=trackB.size()-1,l=0;k>=0;k--,l++) {
					(l%2==1) ? A[trackB[k]].bol=1:B[trackB[k]].bol=1;
				}
				j+=trackB.size();
			}
		}
		
		printf("Case #%d: %d %d\n",i+1,useA,useB);
	}
	return 0;	
}
