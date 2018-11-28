#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

int main(){
	int N;
	cin>>N;
	string str;	
	getline(cin,str);
	string wel ="welcome to code jam";
	string pattern = "welcom tdja";
	string::size_type index,index2;
	
	int vec[19]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};

	ofstream cou("gjamC.txt");

	for(int n=1;n<=N;n++){
		getline(cin,str);

		str.erase(str.find_last_of('m')+1);
		index = str.find_first_not_of(pattern);
		while(index != string::npos){
			index2 = str.find_first_of(pattern,index);
			if(index2!=string::npos) str.erase(index,index2-index);
			else str.erase(index);
			index = str.find_first_not_of(pattern);
		}

		for(int i=str.size()-2;i>=0;i--){
			if(str[i] == 'w')
				vec[0] = (vec[0]+vec[1])%10000;
			else if(str[i] == 'e'){
				vec[1] = (vec[1]+vec[2])%10000;
				vec[6] = (vec[6]+vec[7])%10000;
				vec[14] = (vec[14]+vec[15])%10000;
			}
			else if(str[i] == 'l')
				vec[2] = (vec[2]+vec[3])%10000;
			else if(str[i] == 'c'){
				vec[3] = (vec[3]+vec[4])%10000;
				vec[11] = (vec[11]+vec[12])%10000;
			}
			else if(str[i] == 'o'){
				vec[4] = (vec[4]+vec[5])%10000;
				vec[9] = (vec[9]+vec[10])%10000;
				vec[12] = (vec[12]+vec[13])%10000;
			}
			else if(str[i] == 'm'){
				vec[5] = (vec[5]+vec[6])%10000;
				vec[18] = (vec[18] + 1 )%10000;
			}
			else if(str[i] == ' '){
				vec[7] = (vec[7]+vec[8])%10000;
				vec[10] = (vec[10]+vec[11])%10000;
				vec[15] = (vec[15]+vec[16])%10000;
			}
			else if(str[i] == 't')
				vec[8] = (vec[8]+vec[9])%10000;
			else if(str[i] == 'd')
				vec[13] = (vec[13]+vec[14])%10000;
			else if(str[i] == 'j')
				vec[16] = (vec[16]+vec[17])%10000;
			else if(str[i] == 'a')
				vec[17] = (vec[17]+vec[18])%10000;
			else
				cout<<"‰½‚â‚Á‚Ä‚ñ‚Ì?"<<endl;
		}
		cou<<"Case #"<<n<<": ";
		if(vec[0]<10)
			cou<<"000"<<vec[0]<<endl;
		else if(vec[0]<100)
			cou<<"00"<<vec[0]<<endl;
		else if(vec[0]<1000)
			cou<<"0"<<vec[0]<<endl;
		else
			cou<<vec[0]<<endl;

		for(int j=0;j<19;j++)
			vec[j]=0;
		vec[18]=1;
	}


	return 0;
}
