#include <iostream>
#include <sstream>
#include <string>
#include <set>
using namespace std;
typedef unsigned long int ulong;

ulong StringToNumber ( const std::string &Text )
{
	stringstream ss(Text);
	ulong result;
	return ss >> result ? result : 0;
}

string NumberToString ( ulong Number )
{
	stringstream ss;
	ss << Number;
	return ss.str();
}


ulong uSolution(ulong A, ulong B)
{
	ulong uAnswer(0);
	ulong uTrans;
	ulong uTemp;
	string sTrans;
	string sTemp;
	set<int> Values;
	set<int>::iterator it;

	for(ulong n=A; n<=B; n++){
		uTrans = n;
		sTrans = NumberToString(uTrans);
		for(size_t i=1; i<sTrans.length(); i++){
			if(sTrans[i]!=0){
				sTemp = sTrans.substr(i,sTrans.length()-1);
				sTemp.append(sTrans.substr(0,i)); 
				uTemp = StringToNumber(sTemp);
				it = Values.find(uTemp);
				if(uTemp>=A && uTemp<=B && uTemp>uTrans && it==Values.end()){
					uAnswer++;
					Values.insert(uTemp);
				}
			}
		}
		Values.clear();
	}
	return uAnswer;
}

int main()
{
	int T;
	ulong A,B;
	cin>>T;

	for(int i=1; i<=T; i++){
		cin>>A>>B;
		cout << "Case #"<<i<<": "<<uSolution(A,B)<<endl;
	}
	return 0;
}
