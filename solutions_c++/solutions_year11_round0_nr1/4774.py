#include<fstream>
#include<iostream>
using namespace std;

void main(){
	int all,test;	
	char ob;
	int obnum;
	int temp;
	int i,j;

	ifstream fin("d:\\A-small-attempt0.in");
	ofstream fout("d:\\A-small-attempt0.out");
	fin>>all;
	for(i=1;i<=all;i++){
		fin>>test;

		int cu_o=1;
		int cu_b=1;
		int su_o=0;
		int su_b=0;
		int time=0;
		char last=NULL;

		for(j=0;j<test;j++){

			fin>>ob;
			fin>>obnum;
			if(ob=='O'){
				if(j!=0 || last=='B')
					if(obnum>=cu_o+su_o){
						cu_o=cu_o+su_o;
						su_o=0;
					}else if(obnum<=cu_o-su_o){
						cu_o=cu_o-su_o;
						su_o=0;
					}else{
						cu_o=obnum;
						su_o=0;
					}
				if(obnum>=cu_o)
					temp=obnum-cu_o+1;
				else
					temp=cu_o-obnum+1;
				time += temp;
				cu_o=obnum;
				last='O';
				su_b += temp;
			}

			if(ob=='B'){
				if(j!=0 || last=='O')
					if(obnum>=cu_b+su_b){
						cu_b=cu_b+su_b;
						su_b=0;
					}else if(obnum<=cu_b-su_b){
						cu_b=cu_b-su_b;
						su_b=0;
					}else{
						cu_b=obnum;
						su_b=0;
					}
				if(obnum>=cu_b)
					temp=obnum-cu_b+1;
				else
					temp=cu_b-obnum+1;
				time += temp;
				cu_b=obnum;
				last='B';
				su_o += temp;
			}
		}
		fout<<"Case #"<<i<<": "<<time<<endl;
	}
}