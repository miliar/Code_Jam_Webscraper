#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cstdio>

using namespace std;

int main()
{
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	
	vector<string> iniData(6,"");
	iniData[1]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	iniData[3]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	iniData[5]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	iniData[0]="our language is impossible to understand";
	iniData[2]="there are twenty six factorial possibilities";
	iniData[4]="so it is okey if you want to just give up";

	map<char,char> mp;

	for(int i=1; i<iniData.size();i+=2){
		for (int j=0;j<iniData[i].size();j++){
			if(iniData[i][j]==' ')continue;
			mp[iniData[i][j]]=iniData[i-1][j];
		}
	}
	mp['y']='a';
	mp['e']='o';
	mp['q']='z';
    mp['z']='q';	
	/*map <char,char> :: iterator it;
	for(it=mp.begin();it!=mp.end();it++){
		cout << it->first << it->second << endl;
	}*/
	
	int t;
	cin >> t;
	string ss;
	getline(cin,ss);
	
	for (int i=0;i<t;i++){
		string temp="";
		getline(cin,temp);
		string ans="";
	//	cout << temp << endl;
		for(int j=0;j<temp.size();j++){
			if(temp[j]==' '){
				ans+=' ';
				continue;
			}
			ans+=mp[temp[j]];
		}
		cout << "Case #" << i+1<<": " <<ans << endl;
	}
//	fclose(stdin);
//	fclose(stdout);
	return 0;
}
