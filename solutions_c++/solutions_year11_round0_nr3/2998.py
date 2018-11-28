#include <algorithm>
#include <iostream>
#include <fstream>
#include <stack>
#include <deque>
#include <list>
#include <vector>
#include <map>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cctype>
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

   /*
// any base to Decimal
string any2dec(const string &input,unsigned int base){
	unsigned long int output=0;
	unsigned short int val;
	string::reverse_iterator iter=input.rbegin();
	for(int i=0;iter!=input.rend();iter++,i++){
		switch(tolower(*iter)>='0' && tolower(*iter)<='9'){
		case 1:
			val=tolower(*iter)-'0';
			break;
		default:
			val=10+tolower(*iter)-'a';
			break;
		}
		output+=val*pow((double)base,(double)i);	
	}
	stringstream outputstr;
	outputstr << output;
	return outputstr.str();
}  */

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

	freopen("C-small-attempt2.in","r",stdin);
	freopen("outputC.txt","w",stdout);
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

		vector<int> patrick;
		vector<int> sean;

		/*
		patrick.push_back(sean.front());
		sean.erase(sean.begin());

		while(totalV(patrick) != totalV(sean)){
			if(sean.size()==0)
				break;
			patrick.push_back(sean.front());
			sean.erase(sean.begin());
		}
		if(sean.size() == 0 ){
			cout << "Case #"<<caseOut <<": " << "NO" << endl;
			continue;
		}
		*/

		stable_sort(candies.begin(),candies.end());
		bool found=false;
		//do{
			patrick.clear();
			sean=candies;
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
				//break;
			}
		//}while ( next_permutation(candies.begin(),candies.end()) );
		if(!found)
			cout << "Case #"<< caseOut << ": NO" << endl;
	}


	return 0;
}
