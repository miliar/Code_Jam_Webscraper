#include <iostream>
#include <map>
#include <fstream>
using namespace std;
int pow(int base,int index){
	int rs=1;
	for(int i=0;i<index;++i){
		rs*=base;
	}
	return rs;
}

int main(){
	ifstream infile;
	ofstream outfile;
	char inname[50];
	cout<<"input input filename: ";
	cin>>inname;
	infile.open(inname);
	outfile.open("p3Ans.txt");
	int T;
	infile>>T;
	int I=1;
	string line;
	getline(infile,line);
	while(I<=T){
		int ans=0;
		int A,B;
		multimap<int,int> mymm;
		multimap<int,int>::iterator it;
		infile>>A;
		infile>>B;
		for (int x=A;x<=B;++x){
			int rx=x;
			int num_digit=0;
			//find number of digit	
			int temp=B;
			while(temp>0){
				++num_digit;
				temp/=10;
			}
			//iterate to get rx number
			for(int i=1;i<num_digit;++i){
				rx=(rx/10)+(rx%10)*pow(10,(num_digit-1));
				//check validation of rx
				bool xrxvalid=true;
				if(rx!=x && rx<=B && rx>=A) {
					//check if the pair has already existed
					if(((int)mymm.count(x))!=0){
						for(it=mymm.equal_range(x).first;it!=mymm.equal_range(x).second;++it){
							if((*it).second==rx) xrxvalid=false;
						}
					}
					if(xrxvalid){
						++ans;
						mymm.insert(pair<int,int>(x,rx));
					}
				}
			}
		}
		//output	
		outfile<<"Case #"<<I<<": "<<ans/2<<"\n";
		++I;
	}
return 0;
}
