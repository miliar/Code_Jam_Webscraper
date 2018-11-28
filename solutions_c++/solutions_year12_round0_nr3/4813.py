#include <iostream>
#include <sstream>
#include <math.h>
#include <fstream>

using namespace std;



int test;
int n[50], m[50];
int length;
int nd[7],md[7];

int check(int);
void extract(int[7],int, int);
int recycle(int,int,int);


void main() {
	ifstream in;
		in.open("a.txt");
	in>>test;
	ofstream out;
	out.open("output.txt");
for (int i=1;i<=test;i++)
in>>n[i]>>m[i];

for (int i=1;i<=test;i++){

int min,max,total,start;
total=0;
min=n[i];
max=m[i];
start=min;
while (min<=max){
total+=recycle(start,min,max);
min+=1;
}

out<<"Case #"<<i<<": "<<total/2<<endl;

	


}
in.close();
out.close();
cin>>length;
}

int check(int n){
	int a=1;

	while(n>=10){
	n/=10;
	a+=1;
	}
	return a;
}
void extract(int nd[7],int n,int length){

	int a,b;
	a=n;
	for (int i=length;i>=1;i--){
		b=a%10;
		nd[i]=b;
		a-=b;
		a/=10;
		}
}

int recycle(int beg, int n, int max){
	
	
	extract(nd,n,check(n));
	if (n<10)return 0;
if (n<100) {
if (nd[2]*10+nd[1]<=max&&nd[2]*10+nd[1]>=beg&&nd[2]*10+nd[1]!=n)return 1;
return 0;
}

int temp=0;
if (nd[3]*100+nd[1]*10+nd[2]<=max&&nd[3]*100+nd[1]*10+nd[2]>=beg&&nd[3]*100+nd[1]*10+nd[2]!=n)temp+=1;
if (nd[2]*100+nd[3]*10+nd[1]<=max&&nd[2]*100+nd[3]*10+nd[1]>=beg&&nd[2]*100+nd[3]*10+nd[1]!=n)temp+=1;
return temp;
}