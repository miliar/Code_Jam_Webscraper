#include<iostream>
#include<string>
#include<algorithm>
#include<sstream>

using namespace std;

void translate(string ss, string code, string sol){
	for(int i=0; i<ss.size(); i++){
		cout<<sol[code.find(ss[i],0)];
	}
}







int main(){
	
	string code ="zejp mysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjvq";
	string sol ="qour languageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveupz";
	
	
	int n=0;
	cin>>n;
	string ss;
	getline(cin,ss);
	for(int i=0; i<n;i++){
		cout<<"Case #"<<i+1<<": ";
		getline(cin,ss);
		translate(ss, code , sol);
		
		
		cout<<endl;
	}	
	
}
