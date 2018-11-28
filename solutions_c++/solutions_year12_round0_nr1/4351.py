#include<iostream>
#include<string>
using namespace std;

int main(){
	string key,ans;
	int t,counter,temp,b;
	char save[150];
	key="ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	ans="ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
	for(b=0,temp=key.size();b<temp;++b)
		save[key[b]]=ans[b];
	save[' ']=' ';
	save['z']='q';
	save['q']='z';
	cin>>t;
	getline(cin,key);
	for(counter=1;counter<=t;++counter){
		getline(cin,key);
		cout<<"Case #"<<counter<<": ";
		for(b=0,temp=key.size();b<temp;++b)
			cout<<save[key[b]];
		cout<<endl;
	}
	return 0;
}
/*
ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv
ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup
*/
