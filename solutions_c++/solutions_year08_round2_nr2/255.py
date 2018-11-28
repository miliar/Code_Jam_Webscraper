#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;
#define n first
#define g second
#define INF 1000000

int c,C,A,B,P,p,i,j,o;
vector<pair<int,int> > num;
int main(){
int primos[2000];

primos[0]=2;

for(i=2;i<12000;i++){
for(o=0;primos[o]!=0;o++){
if(i%primos[o]==0) break;
if(primos[o+1]==0) primos[o+1]=i;
}}
cin >> C;
for(c=0;c<C;c++){
	cin >> A >> B >> P;

	num.resize(B+1);
	for(i=A;i<=B;i++){ num[i].n=i; num[i].g=i; }
	for(i=0;i<1000;i++) if(primos[i]>=P) break;
//	cout << primos[i] << endl;

	for(p=i;primos[p]<=B;p++){
		for(i=A;i<=B;i++){
			if(num[i].n%primos[p]==0){
				for(j=i+1;j<=B;j++){
					if(num[j].n%primos[p]==0){
						for(o=A;o<=B;o++){
							if(j!=o && num[j].g==num[o].g) num[o].g=num[i].g;
						}
						num[j].g=num[i].g;
					}
				}
			}
		}
	}

//	for(i=A;i<=B;i++) cout << "Num: " << num[i].n << ", Grupo: " << num[i].g << endl;
	bool repe;
	int grupos=B-A+1;
	for(i=A;i<=B;i++){
		repe=0;
		for(j=A;j<=B;j++){
			if(repe==0 && num[j].g==i) repe=1;
			else if(num[j].g==i) grupos--;
		}
	}
	cout << "Case #" << c+1 << ": " << grupos << endl;
}


}
