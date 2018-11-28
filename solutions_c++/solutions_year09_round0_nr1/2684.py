#include <iostream>
#include <cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<fstream>
#include<vector>

using namespace std;
int b[5090][16];
void ini(int d){
	int i,j;
	for(i=0;i<16;i++){
		for(j=0;j<d;j++){
			b[j][i]=0;
		}
	}
	return;
}
int main(void){
	int i,j,k,l,d,n,t,m,s,ii,jj;
	vector <string> a;
	string c;
	cin>>l>>d>>n;
	for(j=0;j<d;j++){
		cin>>c;
		a.push_back(c);
	}
	for(j=0;j<n;j++){
		cin>>c;
		ini(d);
		k=c.length();t=0;m=0;
		for(i=0;i<k;i++){
			if(c[i]=='('){m=1;continue;}
			if(c[i]==')'){m=0;t+=1;continue;}
			for(s=0;s<d;s++){
				if(b[s][t]==1){continue;}
				if(c[i]==a[s][t]){b[s][t]=1;b[s][15]+=1;}
			}
			if(m==0){t+=1;}
		}
		m=0;
		for(s=0;s<d;s++){
			if(b[s][15]==l){m+=1;}
		}
		cout<<"Case #"<<j+1<<": "<<m<<"\n";
	}
	return 0;
}

