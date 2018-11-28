#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>


using namespace std;

ifstream fin("a.in");
ofstream fout("google.out");



char digit(int d){

	return d<10 ? '0'+ d : 	'A'+ d -10;

}

string toBase (int n, int base) {

	string  ret;
	for(;n>0;n/=base){

		ret=digit(n%base) + ret;
	}

	return ret;
}


vector<int> aNat(string s) {

	vector<int> ret;

        int m=1;
	int n=0;;
	
	for(int j=s.size()-1;j>=0;j--) {
		if(s[j]!=' ') { n+=(s[j]-'0')*m; m=m*10;}
		else { ret.push_back(n); m=1;n=0;}
	}

	ret.push_back(n);	

	return ret;
	
	

}




bool isHappy(string a,int b) {

	for (int i=0;i<1000;i++){
	
		int t=0;
		
		for(int j=0;j<a.size();j++) {
	
			t+=(a[j]-'0')*(a[j]-'0');

		}

		if(t==1) return true;
	
		a=toBase(t,b);
	}


	return false;
}



int main (){

	vector<string> lines;
	
	string line;
	getline(fin, line);

	while( getline(fin, line) ) lines.push_back(line);


	vector<int> ret;

	for(int i=0;i < lines.size(); i++) {

		vector<int> bases=aNat(lines[i]);

		int count = 2;

		while(true)  {

			bool happy=true;

			
			for(int j=0;j<bases.size();j++) {				
				if(!isHappy( toBase(count,bases[j]), bases[j] ) ){ happy=false;break;}
				//cout<<toBase(count,bases[j])<< " "<< bases[j]<<endl;			
			}

		if(happy) break;
		count++;	
		
		}
		
		ret.push_back(count);


	}
	

	for(int i=0;i<ret.size();i++)  
		fout <<"Case #"<< i+1<<": "<< ret[i]<<endl;


}
