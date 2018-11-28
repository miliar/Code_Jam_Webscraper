#include<iostream>
#include<string>

using namespace std;

char map[100];

void preprocess() 
{
	string s1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string s2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string s3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	
	string s4="our language is impossible to understand";
	string s5="there are twenty six factorial possibilities";	
	string s6="so it is okay if you want to just give up";
	
	for(int i=0;i<s1.length();i++) {
		if(s1[i]!=' ')
			if(map[s1[i]-'a'] ==0)
				map[s1[i]-'a']=s4[i];
	}
	
	for(int i=0;i<s2.length();i++) {
		if(s2[i]!=' ')	
			if(map[s2[i]-'a'] ==0)
				map[s2[i]-'a']=s5[i];
	}
	
	for(int i=0;i<s3.length();i++) {
		if(s3[i]!=' ')
			if(map[s3[i]-'a'] ==0)
				map[s3[i]-'a']=s6[i];
	}
	
	map['z'-'a']='q';
	map['q'-'a']='z';
}

int main()
{
		
	
	string temp;
	int t;
	
	preprocess();
	
	cin>>t;
	getline(cin,temp);
	
	for(int i=0;i<t;i++) {
		getline(cin,temp);
		for(int j=0;j<temp.length();j++) {
			if(temp[j]!=' ') {
				temp[j]=(char)map[temp[j]-'a'];
				
			}
		}
		 
		cout<<"Case #"<<i+1<<": "<<temp<<"\n";
	}
	
	return 0;
}

