//Besm Allah

#include<cstdio>
#include<iostream>
using namespace std;

char know[700];

char inp[200];
int main(){
	int T;
know[97] = 121;
know[98] = 104;
know[99] = 101;
know[100] = 115;
know[101] = 111;
know[102] = 99;
know[103] = 118;
know[104] = 120;
know[105] = 100;
know[106] = 117;
know[107] = 105;
know[108] = 103;
know[109] = 108;
know[110] = 98;
know[111] = 107;
know[112] = 114;
know[113] = 'z';
know[114] = 116;
know[115] = 110;
know[116] = 119;
know[117] = 106;
know[118] = 112;
know[119] = 102;
know[120] = 109;
know[121] = 97;
know[122] = 'q';
know[' '] = ' ';
	cin>>T;
	cin.getline(inp,100);
	for(int i = 0 ; i < T ; i++){
		cin.getline(inp,110);
		cout<<"Case #"<<i+1<<": ";
		for(int i = 0 ; inp[i] ; i++)
			cout<<know[inp[i]];
		cout<<endl;
	}
	
}
