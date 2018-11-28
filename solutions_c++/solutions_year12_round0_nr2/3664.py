#include<iostream>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<vector>
using namespace std;

int ans(int n,int s,int p,vector<int>&v){
	int rv=0;
	for(int i=0;i<v.size();i++){
//		switch(v[i]){
//			case 0:
//				if(p==0) rv++;
//				else return rv;
//				break;
//			case 1:
//				if(p<=1) rv++;
//				else return rv;
//				break;
//			case 2:
//			case 3:
//				if(p<=1) rv++;
//				else if(p==2 && s){
//					s--;
//					rv++;
//				}
//				else return rv;
//				break;
//			case 4:
//				if(p<=2) rv++;
//				else if(p==3 && s){
//					s--;
//					rv++;
//				}
//				else return rv;
//				break;
//		}
//		
		if(v[i]==0){
			if(p==0) rv++;
			else return rv;
		}
		else if((v[i]+2)/3>=p)
			rv++;
		else if(s && v[i]>=2 && (v[i]+4)/3>=p){
			s--;
			rv++;
		}
		else return rv;
	}
	return rv;
}

int main(int argc, char** argv){
	ifstream in("B-large.in");
//	ifstream in("b.test.txt");
	ofstream out("b.out");

string line;

int t=0;

in>>t;
	in.get();//get out \n

for(int i=0;i<t;i++){
	out<<"Case #"<<(i+1)<<": ";
	
	getline(in,line);
	istringstream iss(line);

	vector<int>v;
	
	int n,s,p;
	iss>>n>>s>>p;
	for(int i=0;i<n;i++){
		int b;
		iss>>b;
		v.push_back(b);
	}
	//sort
	sort(v.begin(),v.end());
	reverse(v.begin(),v.end());
	
	out<<ans(n,s,p,v);
	
	out<<endl;
}
	system("pause");
	return 0;
}
