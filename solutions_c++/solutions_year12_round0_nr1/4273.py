/*
 * Soln.cpp
 *
 *  Created on: Mar 31, 2012
 *      Author: avikramj
 */

#include<iostream>
#include<string>
#include<fstream>
using namespace std;
char eng[]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char goog[]={'y','n','f','i','c','w','l','b','k','u','o','m','x','n','s','e','v','z','p','d','r','j','g','t','h','a','q'};
char rev[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
void convert(string &s);
int main(){
	char buf[110];


    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");
    int numCases;
    int i=1;
    if(in.getline(buf,110))
    	sscanf(buf,"%d",&numCases);
	while(in.getline(buf,110)){
//		cout<<"Enters\n";
		string s(buf);
		convert(s);
		cout<<s;
		out<<"Case #"<<i<<": "<<s<<endl;
		i++;
	}
	cin>>buf;
	in.close();
	out.close();
//	cout<<"ends\n";
	return 0;

}

void convert(string &s){
	for(int i=0;i<s.size();i++){
		if(s[i]==' ')
			continue;
		else{
			s[i]=rev[s[i]-'a'];
		}
	}
}
