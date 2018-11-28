#include<iostream>
#include<string.h>
#include<sstream>
using namespace std;

int main(){
	char mapping[26];int n;string q,s,o[30];
	mapping[97] = 'y';mapping[98] = 'h';mapping[99] = 'e';mapping[100] = 's';mapping[101] = 'o';mapping[102] = 'c';mapping[103] = 'v';
	mapping[104] = 'x';mapping[105] = 'd';mapping[106] = 'u';mapping[107] = 'i';mapping[108] = 'g';mapping[109] = 'l';mapping[110] = 'b';
	mapping[111] = 'k';mapping[112] = 'r';mapping[113] = 'z';mapping[114] = 't';mapping[115] = 'n';mapping[116] = 'w';mapping[117]= 'j';
	mapping[118] = 'p';mapping[119] = 'f';mapping[120] = 'm';mapping[121] = 'a';mapping[122] = 'q';
	getline (cin,q,'\n');
	stringstream(q) >> n;;int j=0;//cout<<n;
	while(j<n){
		getline (cin,s,'\n');
		//cout<<s;
		for(int i=0;i<s.length();i++){
			if(s[i]<=122 && s[i]>=97)
			o[j]+= mapping[s[i]];
			else o[j]+= s[i];
		}
		
		++j;
	}j=0;
	while(j<n){
		cout<<"Case #"<<j+1<<": "<<o[j]<<endl;
		++j;
	}
}
