#include <cstdlib>
#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

//int* binaryTo(long i);
//long binaryFrom(int* i);

//long patrickAdd(long i1,long i2);

int xorAdd(int num1,int num2);

int main(){
	int caseCount = 0;
	cin >> caseCount;
	cin.ignore();
	for(int i=0;i<caseCount;i++){
		string inText;
		int candiesCount=0;
		long* candies;
		//get input parameters
		cin>>candiesCount;
		cin.ignore();
		getline(cin,inText);
		stringstream streamInText(inText);
		candies = (long*)malloc(sizeof(long)*candiesCount);
		for(int j=0;j<candiesCount;j++){
			//read numbers
			long num;
			streamInText >> num;
			candies[j]=num;
		}
		sort(candies,candies+candiesCount);
		//find pile
		int max_r=-1;
		for(int j=1;j<candiesCount;j++){
			int p1=0;
			int p1_r=0;
			int p2=0;
			int p2_r=0;
			bool i1=false;
			bool i2=false;
			for(int k=0;k<j;k++){
				if(!i1){
					p1=candies[k];
					i1=true;
				}
				else p1=xorAdd(p1,candies[k]);
				p1_r=p1_r+candies[k];
			}
			for(int k=j;k<candiesCount;k++){
				if(!i2){
					p2=candies[k];
					i2=true;
				}
				else p2=xorAdd(p2,candies[k]);
				p2_r=p2_r+candies[k];
			}
	//		cout << "j: " <<j<<endl;
	//		cout << "p1: " <<p1<<"/"<<p1_r<<endl;
	//		cout << "p2: " <<p2<<"/"<<p2_r<<endl;
			if(p1==p2){
				int r=max(p1_r,p2_r);
				if(r>max_r)max_r=r;
				//				break;
			}
		}

		//return output
		cout << "Case #"<<i+1<<": ";
		if(max_r==-1)cout<<"NO"<<endl;
		else cout<<max_r<<endl;
	}
}

int xorAdd(int num1,int num2){
	return num1^num2;
}
