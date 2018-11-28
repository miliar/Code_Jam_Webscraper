#include<iostream>
#include<cstdio>
#include<deque>
#include<vector>
#include<string>

using namespace std;

int main(){
	freopen("in.txt","rt",stdin);
	freopen("out.txt","wt",stdout);
	int t,counter=1;
	char times[128][128];
	bool opp[128][128];
	string stringtimes,stringop;
	cin>>t;
	while(t--){
		for(int i=0;i<128;i++){
				for(int k=0;k<128;k++){
					times[i][k]=-1;
				    opp[i][k]=0;
				}
		}
		int num1;
		cin>>num1;
		for(int k=0;k<num1;k++){
		     cin>>stringtimes;
		     times[(int)stringtimes[0]][(int)stringtimes[1]]=stringtimes[2];
		     times[(int)stringtimes[1]][(int)stringtimes[0]]=stringtimes[2];
		}
		int num2;
		cin>>num2;
		for(int m=0;m<num2;m++){
			cin>>stringop;
			opp[(int)stringop[0]][(int)stringop[1]]=1;
			opp[(int)stringop[1]][(int)stringop[0]]=1;
		}
		int num3;
		deque<char>str;
		cin>>num3;
		char c;
		for(int i=0;i<num3;i++){
			cin>>c;
			if(str.empty()) str.push_back(c);
			else{
			if(times[(int)str.back()][(int)c]!=-1){
			char temp=str.back();
			str.pop_back();
			str.push_back(times[(int)temp][(int)c]);
			}
			else{
				for(int s=0;s<str.size();s++){
					if(opp[(int)str[s]][(int)c]==1)
						str.clear();
			 }
				if(!str.empty()) str.push_back(c);
			}
		  }
		}
		cout<<"Case #"<<counter++<<": [";
		string str1="";
		for(int i=0;i<str.size();i++){
			cout<<str1<<str[i];
			str1=", ";
		}
		cout<<"]\n";
	}
	return 0;
}
