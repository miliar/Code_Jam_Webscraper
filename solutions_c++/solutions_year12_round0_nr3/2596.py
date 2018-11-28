#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
	ofstream fout("codejamq3large.txt");
	ifstream fin("C-large.in");
	int t,a,b,count,c,p,i,y;
	fin>>t;
	//cin.ignore(1);
	int x=0,z=0;
	while(t--){
		fin>>a;
		fin>>b;
		p=a;
		c=1;
		while(p!=0){
			c=c*10;
			p=p/10;
		}
		c=c/10;
		count=0;
		for(i=a;i<b;i++){
			y=((i%10)*c)+(i/10);
			while(y!=i){
				if((y<=b)&&(y>i))
					count++;
				y=((y%10)*c)+(y/10);
			}
		}
		z++;
		fout<<"Case #"<<z<<": "<<count<<"\n";
	}
	return 0;
}
