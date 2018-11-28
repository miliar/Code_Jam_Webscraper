#include<STDLIB.H>
#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<cmath>
#include<time.h>
#include<set>
#include<algorithm>
#include<fstream>
using namespace std;

int main(){
ofstream file("D:\\1.txt");
int n,t, ora, blu,time,o,b;
char h;
cin >> t;
int oran[12][2], blun[12][2];
for (int test=0; test<t; test++){
	time=0;
	o=0;b=0;
	ora=1; blu=1;
	int path=0;
	cin >> n;
	for (int i=0; i<n; i++){
		cin >> h;
		if (h=='O'){
			cin >> oran[o][0];
			oran[o][1]=i+1;
			o++;
		}
		else{
			cin >> blun[b][0];
			blun[b][1]=i+1;
			b++;
		}
	}
	oran[o][0]=99999999;
	oran[o][1]=99999999;
	blun[b][1]=99999999;
	blun[b][0]=99999999;
	int ko=0,kb=0; 
	int step=1;
	bool perb=false, pero=false;
	for (int i=1; ;i++){



		perb=false; pero=false;
		if (step>n)break;
		if (oran[ko][1]>=step){
			if (oran[ko][0]!=ora){
				if (oran[ko][0]<ora) ora--;
				else ora++;
				pero=true;
			}
		}
		if (blun[kb][1]>=step){
			if (blun[kb][0]!=blu){
				if (blun[kb][0]<blu) blu--;
				else blu++;
				perb=true;
			}
		}
		if (oran[ko][1]==step&&oran[ko][0]==ora&&pero==false){
			step++;
			ko++;
			time=i;
			continue;
		}
		if (blun[kb][1]==step&&blun[kb][0]==blu&&perb==false){
			step++;
			kb++;
			time=i;
			continue;
		}
	}
	cout<< "Case #"<<test+1<<": "<<time << endl;
}
file.close();
return 0;
}
