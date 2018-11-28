#include<iostream>
#include<cstring>

using namespace std;

int main() {
	string str1 = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string str2 = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	
	char dict[123];
	int leng = str1.size();
	for(int i=0;i<leng;i++) {
		dict[str1[i]]=str2[i];		
	}
	dict[32]=32;
	dict['z']='q';
	dict['q']='z';
	
	int n;
	cin >> n;
	getline(cin,str1);
	for(int i=0;i<n;i++) {
		string str1;
		cout << "Case #" << i+1 << ": ";
		getline(cin, str1);
		int len = str1.size();
		for(int j=0;j<len;j++) {
			cout << dict[str1[j]];
		}
		cout << "\n";
		//cout << str1 << "\n";
	}
	
	return 0;
}
