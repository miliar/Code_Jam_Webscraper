#include<iostream>
#include<fstream>
#include <string>
#include <map>

using namespace std;


int rotateNum(int n, int shift, int dig);
int digits(int m);
void main(){
	ifstream fin;
	ofstream fout;

	int ntest, A, B, n, m, count;

	fin.open("C-small-attempt0.in");
	fout.open("Output.txt");

	if(fin.good() == true) {
		fin >> ntest; //cout<<"Number of test case is "<<ntest<<endl;
		//fin.ignore();
		for(int j=0; j<ntest; j++){
			fin>>A;
			fin>>B;
			count=0;
			for(n=A; n<=B; n++){
				m=n;
				int dig=digits(n);
				int k=1;
				int c=0;
				m=rotateNum(n,k,dig);	
				
				while(k<dig){
					if(digits(m)!=dig){
						k++;
						m=rotateNum(n,k,dig);
						continue;
					}
					if(m==n)
						break;
					//if(n==120)
					//	cout<<"current n "<<n<<" and current m "<<m <<endl;
					if(n<m && m<=B){
						count++;
						c++;
					}
					k++;
					m=rotateNum(n,k,dig);
					
				}
				//fout<<"########   For  n "<<n <<" number of pairs is "<<c<<" and count so far is "<<count<<endl;
			}
			fout<<"Case #"<<j+1<<": "<<count<<endl;
			//cout<<"Case #"<<j+1<<": "<<count<<endl;
		}
	}
}
int rotateNum(int m, int sh, int dig){
	int quo, rem;
	int div=(int)pow((double)10,sh);
	quo=m/div;
	rem=m%div;
	div=(int)pow((double)10,(dig-sh));

	return(rem*div+quo);
}
int digits(int m){
	int c=1;
	while((m/10)!=0){
		c++;
		m=m/10;
	}
	return c;
}