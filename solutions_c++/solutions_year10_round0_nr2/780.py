#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "BigInteger.cpp"

using namespace std;

BigInteger gcd(BigInteger a,BigInteger b){
	BigInteger r;
	while(1){
		if(b == 0) break;
		r = b;
		b = a % b;
		a = r;
		
	}
	return a;
}
BigInteger getans(vector<BigInteger>& num){
	vector<BigInteger> list;
	for(int i = 0; i < num.size(); i++)
		for(int j = i + 1; j < num.size(); j++){
			BigInteger temp = num[i] - num[j];
			temp = temp.getAbs();
			list.push_back(temp);
		}
	cout << "here" << endl;
	BigInteger rt = list[0];
	for(int i = 1; i < list.size(); i++)
		rt = rt.gcd(list[i]);
	BigInteger sm = rt - BigInteger("0");
	while(rt < num[0])
		rt = rt + sm;
	return rt - num[0];

}
int main(){
	ifstream in("input");
	ofstream out("output");
	int cases;
	in >> cases;
	
	int n;

	for(int i = 1; i <= cases; i++){
		out << "Case #" << i << ": ";
		//cout << i << endl;
		in >> n;
		string c;
		vector<BigInteger> num;
		for(int j = 0; j < n; j++)
		{
			in >> c;
			num.push_back(BigInteger(c));
		}
		out << (getans(num)).toString() << endl;
	}
	out.close();
	return 0;
}
