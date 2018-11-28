#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

int main(){
	int mapping[200];
	mapping[int('a')] = int('y');
	mapping[int('o')] = int('e');
	mapping[int('z')] = int('q');
	string s1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string s2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	if(s1.length()!=s2.length())
		cout<<"Length does not match!"<<endl;
	for(int i = 0 ; i < s1.length();i++){
		mapping[int(s1[i])]=int(s2[i]);
	}
	mapping[97+16]=int('z');
	mapping[32]=32;


	string case_num;

    getline(cin,case_num);
	for (int t =0 ;t <atoi(case_num.c_str()); t++){
		string to_translate;
		getline (cin,to_translate);

		for(int i = 0;i<to_translate.length();i++)
			to_translate[i]=char(mapping[int(to_translate[i])]);
		cout<<"Case #"<<t+1<<": "<<to_translate<<endl;

	}


	return 0;

}
