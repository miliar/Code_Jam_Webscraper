#include <algorithm>
#include <iostream>
#include <vector>
#include <functional>
#include <string>
using namespace std;

int main (){
	int i,t=0,T,index;
	char temp;
	string lett = " \nabcdefghijklmnopqrstuvwxyz";
	string mapp = " \nyhesocvxduiglbkrztnwjpfmaq";
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	cin >> T;
	while (t<T){
		i=0;
		string res; 
		cin >> temp;
		res.push_back(mapp[lett.find(temp)]);
		
		while(temp != '\n'){
			cin >> noskipws >> temp;
			if (cin.eof()) break;
			res.push_back(mapp[lett.find(temp)]);
			i++;
		}
		cout << "Case #" << ++t << ": " << res;
	}
	 return 0;
}
