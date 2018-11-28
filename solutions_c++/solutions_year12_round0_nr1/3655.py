#include <iostream>
#include <string>

using namespace std;

int A[26];

void init(){
	A[0] = 121;A[1] = 104;A[2] = 101;A[3] = 115;A[4] = 111;A[5] = 99;A[6] = 118;A[7] = 120;A[8] = 100;A[9] = 117;A[10] = 105;A[11] = 103;A[12] = 108;A[13] = 98;A[14] = 107;
	A[15] = 114;A[16] = 122;A[17] = 116;A[18] = 110;A[19] = 119;A[20] = 106;A[21] = 112;A[22] = 102;A[23] = 109;A[24] = 97;A[25] = 113; 
}

string mod(string str){
	string s = "";
	int len = str.length(),i;
	
	for(i=0;i<len;i++){
		if(str[i] != ' ') s.push_back((char)A[(int)str[i]-97]);
		else s.push_back(' ');
	}
	
	return s;
}

int main(){
	int T,i=0;
	string str;
	cin>>T;
	getline(cin,str);
	init();
	
	while(T--){
		getline(cin,str);
		cout<<"Case #"<<i+1<<": "<<mod(str)<<endl;
		i++;
	}
	
	return 0;
}
