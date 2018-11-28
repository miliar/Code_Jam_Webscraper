#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
	ifstream fin("B-large.in");
	ofstream fout("out1.txt");
	int t,i,n,s,p,a[100],count;
	fin>>t;
	fin.ignore(1);
	int x=0;
	while(t--){
		fin>>n;
		fin>>s;
		fin>>p;
		count=0;
		for(i=0;i<n;i++)
			fin>>a[i];
		if(p==0){
			count = n;
		}
		else{
			for(i=0;i<n;i++){
				if(((3*p)-2)<=a[i])
					count++;
				else if(a[i]!=0){
					if((a[i]==((3*p)-3))||(a[i]==((3*p)-4))){
						if(s>0){
							s--;
							count++;
						}
					}
				}
			}	
		}
		x++;
		fout<<"Case #"<<x<<": "<<count<<"\n";
	}
	return 0;
}


					
			
