#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;


int main(){
	ifstream fin("B-large.in");
	//ifstream fin("test.txt");
	ofstream fout("B-large.out");
	
	int T;
	fin>>T;
	string str;
	getline(fin,str);
	for(int t=1;t<=T;t++){
		getline(fin,str);
		bool found=false;
		int l,r;
		l=-1;
		
		for(int i=str.length()-1;i>=1;i--){
			for(int j=i-1;j>=0;j--){
				if(str[i]>str[j]){
					if(j>l){	found=true;	l=j;	r=i;}
				}
			}
		}
		
		if(found){
			str.insert(str.begin()+l,str[r]);
			str.erase(str.begin()+r+1);
		}
		
		sort(str.begin()+l+1,str.end());
		
		if(!found || str[0]=='0'){
			str.append("0");
			sort(str.begin(),str.end());
			//cout<<str<<endl;
			if(str[0]=='0'){
				for(int i=1;i<str.length();i++){
					if(str[i]>'0'){
						char tmp=str[0];
						str[0]=str[i];
						str[i]=tmp;
						found=true; break;
					}
				}
			}
		}
		
		//cout<<"Case #"<<t<<": "<<str<<endl;
		fout<<"Case #"<<t<<": "<<str<<endl;
	}
}
















