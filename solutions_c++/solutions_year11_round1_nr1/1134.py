#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
#include <math.h>

using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;


int smallest(int p){
float t1=(float)100/p;
if (p==0) return 0;
for (int i=1;i<100;i++){
	float t2=(float)t1*i;
	if (t2==(int)t2) return t2;
}
}
int main(){
ifstream input;
ofstream output;
input.open("d:/input.in");
output.open("d:/output.in");
int N;
input>>N;
for(int i=1;i<=N;i++){
	output<<"Case #"<<i<<": ";
	cout<<"Case #"<<i<<": ";
	double td;
	int pd,pg;
	input>>td;
	input>>pd>>pg;
	cout<<td<<"   "<<smallest(pd)<<"  "<<(td>=smallest(pd))<<endl;
	if (td>=smallest(pd)){
		if(pg!=100 && pg!=0) output<<"Possible\n"; else {
			if(pg==100){ if(pd==100) output<<"Possible\n"; else output<<"Broken\n";}
			if(pg==0){if(pd==0)output<<"Possible\n"; else output<<"Broken\n";}
		}
	}else output<<"Broken\n";

}
system("pause");
return 0;
}