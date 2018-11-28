#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <cstring>
#include <numeric>
#include <utility>
using namespace std;

int main () {
	fstream filestr;
	ofstream outstr;
	int cases;
	int n,m;
	int win=0;
	vector<int> vres(600,0);
	string hexa, btemp;
	vector<string> b;
	
	filestr.open("/Users/HOOI/Downloads/C-small-attempt0.in");
	outstr.open("/Users/HOOI/Documents/XCode/CodeJam/OUTPUT.txt");
	filestr >> cases;
	for (int cs=0;cs<cases;cs++){
		int res=0;
		b.clear();
		vres.clear();
		vres.resize(600);
		win=0;
		filestr >> m >> n; //n=row length, m = number of rows
		cout << "n is "<< n << " and m is "<< m << endl;
		for (int i=0;i<m;i++){ 
			filestr >> hexa;
			btemp="";
			for (int j=0;j<hexa.size();j++){
				if (hexa[j]=='0') btemp += "0000";
				else if (hexa[j]=='1') btemp += "0001";
				else if (hexa[j]=='2') btemp += "0010";
				else if (hexa[j]=='3') btemp += "0011";
				else if (hexa[j]=='4') btemp += "0100";
				else if (hexa[j]=='5') btemp += "0101";
				else if (hexa[j]=='6') btemp += "0110";
				else if (hexa[j]=='7') btemp += "0111";
				else if (hexa[j]=='8') btemp += "1000";
				else if (hexa[j]=='9') btemp += "1001";
				else if (hexa[j]=='A') btemp += "1010";
				else if (hexa[j]=='B') btemp += "1011";
				else if (hexa[j]=='C') btemp += "1100";
				else if (hexa[j]=='D') btemp += "1101";
				else if (hexa[j]=='E') btemp += "1110";
				else if (hexa[j]=='F') btemp += "1111";
			}
			b.push_back(btemp);
		}
		cout << "printing b:" << endl;
		for (int i=0;i<m;i++)
			cout << b[i] << endl;
		
		
		for (int cut=min(m,n); cut >0; cut--){
			cout << "cut="<<cut<<": "<<endl;
			for (int i=0;i<m-cut+1;i++){
				for (int j=0;j<n-cut+1;j++){
					cout << "i="<<i<<", j="<<j<<endl;
					char col = b[i][j];
					col = ((1+col-'0')%2)+'0'; 
				
					for (int k=i;k<i+cut;k++){
						if (cut%2==0 && k!=i) col = ((1+col-'0')%2)+'0'; 
						for (int l=j;l<j+cut;l++){
							col = ((1+col-'0')%2)+'0'; 
							if (b[k][l]==col){ cout << "b["<<k<<"]["<<l<<"] =="<<col<<endl; }
							if (b[k][l]!=col){ cout << "b["<<k<<"]["<<l<<"] !="<<col<<endl; goto failure; }

						}
					}
					cout << "success at i="<<i<<", j="<<j<<", cut="<<cut<<endl;
					
					for (int k=i;k<i+cut;k++)
						for (int l=j;l<j+cut;l++)
							b[k][l]='2';
					for (int i=0;i<m;i++) cout << b[i] << endl;
					win=1;
					vres[cut]++;
					failure:;
				}
			}
			if (win==1) res++;
			win=0;
		}
		outstr << "Case #"<<cs+1<<": "<< res <<endl;
		cout << "Case #"<<cs+1<<": "<< res <<endl;
		for (int i=599;i>=0;i--) if (vres[i]!=0) cout << i << " " << vres[i] << endl; 
		for (int i=599;i>=0;i--) if (vres[i]!=0) outstr << i << " " << vres[i] << endl; 
	}
	filestr.close();
	outstr.close();
	return 0;
}