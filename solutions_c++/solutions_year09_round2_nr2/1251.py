

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

#define LEN 10

int numList[LEN];

//int baseCheck(const string& numStr){
//	bool numFlag[10];
//	memset(numFlag, false, sizeof(bool)*LEN);
//	for(size_t i=0;i<numStr.size();i++)
//		numFlag[numStr[i]-'0'] = true;
//	int j=0;
//	for(int i=0;i<LEN;i++)
//		if(numFlag[i]){
//			numList[j] = i;
//			j++;
//		}
//	return j;
//}

//void Sort(string& numStr, int start){
//
//}

string check(string& numStr){
	//numStr.reserve();
	int flag=-1;
	for(size_t i=numStr.size()-1;i>0;i--)
		if(numStr[i] > numStr[i-1]){
			flag = i-1;
			break;
		}
	if(-1 == flag){
		//reverse(numStr.begin(), numStr.end());
		//size_t i = 0;
		//bool nflag = false;
		//string newStr = numStr.substr(i, numStr.size()-i);
		//return newStr;
		//return numStr;
		reverse(numStr.begin(), numStr.end());
		numStr = '0'+numStr;
		//cout<<numStr.size()<<endl;
		//reverse(numStr.begin(), numStr.end());
		cout<<numStr<<endl;
		int k=0;
		while(numStr[k]-'0' == 0)
			k++;
		cout<<k<<endl;
		numStr[0] = numStr[k];
		//cout<<numStr[i]<<endl;
		numStr[k] = '0';
		//string newStr = numStr[i]+numStr;
		//newStr[1] = '0';
		return numStr;
	}
	char ch = numStr[flag];
	int j= numStr.size()-1;
	while(j>flag+1){
		if(numStr[j] > ch)
			break;
		j--;
	}

	//cout<<numStr[flag]<<" "<<numStr[j]<<endl;

	numStr[flag] = numStr[j];
	numStr[j] = ch;
	string newStr = numStr.substr(flag+1, numStr.size()-flag-1);

	for(size_t i = flag+1;i<numStr.size();i++)
		numStr[i] = newStr[numStr.size()-1-i];
	//cout<<newStr<<endl;
	//sort(numStr, flag+1);
	//cout<<numStr<<endl;
	//string newStr = numStr.substr(flag, numStr.size()-flag);
	//cout<<ch<<" "<<newStr<<endl;
	//return newStr;
	//cout<<numStr<<endl;
	return numStr;
}

int main(){
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int T;
	fin>>T;
	string numStr;
	for(int i=1;i<=T;i++){
		fin>>numStr;
		fout<<"Case #"<<i<<": ";
		fout<<check(numStr)<<endl;
		//cout<<numStr<<endl;
		//int base = baseCheck(numStr);
		//cout<<base(numStr)<<endl;
		//for(int j=0;j<base(numStr);j++)
		//	cout<<bases[j]<<" ";
		//cout<<endl;
	}
	return 0;
}