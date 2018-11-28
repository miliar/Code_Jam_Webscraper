#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <cmath>
#include <sstream>

using namespace std;

string dec2any(const string &decimal,unsigned int base){
	unsigned long int dec = strtoul(decimal.c_str(),NULL,10);
	if(dec==0)
		return "0";
	unsigned short int remaining;
	string output;
	for(;dec>0;dec/=base){
		stringstream remStr;
		remaining=dec%base;
		switch(remaining>9){
			case 1:
				remStr << (char)('A'+remaining-10);
				break;
			default:
				remStr << remaining;
				break;
		}
		output.insert(0,remStr.str());
	}
	return output;
}

int addition(int x,int y){
	string result;
	stringstream conv;
	conv << x;
	string binx = dec2any(conv.str(),2);
	conv.str("");
	conv << y;
	string biny = dec2any(conv.str(),2);


	if(biny.size() > binx.size())
		binx.insert(0,biny.size()-binx.size(),'0');
	else
		biny.insert(0,binx.size()-biny.size(),'0');


	for(int i=0; i<biny.size(); i++){
		result.push_back( (biny[i]==binx[i])?'0':'1' );
	}


	int decimal=0 ;//any2dec(result,2);

	int power=0;
	for(int sz=result.size()-1; sz>=0; sz--){
		decimal += (result[sz]=='1'?1:0) * (int)pow(2,power);
		power++;
	}

	return decimal;
}

int totalV(vector<int> & v){
	int total=0;
	for(int i=0;i<v.size();i++)
		total = addition(total,v[i]);
	return total;
}

int totalValue(vector<int> & v){
	int total=0;
	for(int i=v.size();i>0;i--)
		total += v[i-1];
	return total;
}

int main(){

	freopen("C-large.in","r",stdin);
	freopen("outC2.txt","w",stdout);
	int cases;
	cin >> cases;
	int caseOut=0;

	for(int i=0;i<cases;i++){
		caseOut++;
		int nums,total=0;
		vector<int> candies;
		cin >> nums;

		if(!nums){
			cout << "Case #"<<caseOut <<": " << "NO" << endl;
			continue;
		}

		for(int j=0;j<nums;j++){
			int candy;
			cin >> candy;
			candies.push_back(candy);
			total = addition(total,candy);
		}

		if(total%2 != 0){
			cout << "Case #"<<caseOut <<": " << "NO" << endl;
			continue;
		}

		stable_sort(candies.begin(),candies.end());
		bool found=false;

		vector<int> patrick;
		vector<int> sean(candies);

		patrick.push_back(sean.front());
		sean.erase(sean.begin());

		while(totalV(patrick) != totalV(sean)){
			if(sean.size()==0)
				break;
			patrick.push_back(sean.front());
			sean.erase(sean.begin());
		}
		if(sean.size() > 0 ){								 
			cout << "Case #"<<caseOut <<": " << totalValue(sean) << endl;
			found=true;
		}
		if(!found)
			cout << "Case #"<< caseOut << ": NO" << endl;
		cout.flush();
	}


	return 0;
}
