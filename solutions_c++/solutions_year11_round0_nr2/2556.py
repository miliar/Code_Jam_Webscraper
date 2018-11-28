#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

vector<char> buff;
vector<string> combine,oppose;

bool buff_proc(){
	bool changed=true,good=false;

	while(changed && buff.size()>1){
		changed=false;
		for(int i=0;i<combine.size();i++)
			if( (combine[i][0]==buff[0] && combine[i][1]==buff[1]) || (combine[i][0]==buff[1] && combine[i][1]==buff[0]) ){
				buff.erase(buff.begin());
				buff.erase(buff.begin());
				buff.insert(buff.begin(),combine[i][2]);
				buff_proc();
				changed=true;
				good=true;
				break;
			}
	}

	return good;
}

bool check_trash(){
	for(int o=0;o<oppose.size();o++)
		for(int b=1;b<buff.size();b++)
			if( (buff[0]==oppose[o][0] && buff[b]==oppose[o][1]) || (buff[0]==oppose[o][1] && buff[b]==oppose[o][0]) ){
				buff.clear();
				return true;
			}
	return false;
}

int main(){
	int T;
	string temp;
	cin>>T;

	for(int t=0;t<T;t++){
		int C,D,N;
		string seq;
		buff.clear();
		combine.clear();
		oppose.clear();
		cin>>C;
		for(int c=0;c<C;c++){
			cin>>temp;
			combine.push_back(temp);
		}
		cin>>D;
		for(int d=0;d<D;d++){
			cin>>temp;
			oppose.push_back(temp);
		}
		cin>>N;
		cin>>seq;
/*		cout<<"Combine: ";for(int i=0;i<C;i++) cout<<combine[i]<<" ";cout<<endl;
		cout<<"Oppose: ";for(int i=0;i<D;i++) cout<<oppose[i]<<" ";cout<<endl;
		cout<<"seq: "<<seq<<endl;*/
		for(int n=0;n<N;n++){
			buff.insert(buff.begin(),seq[n]);
//			for(int n=buff.size()-1;n>=0;n--) cout<<buff[n];cout<<endl;
			if(!buff_proc()) check_trash();
		}
		cout<<"Case #"<<t+1<<": [";
		for(int n=buff.size()-1;n>=0;n--){
			cout<<buff[n];
			if(n>0) cout<<", ";
		}
		cout<<"]"<<endl;
	}
}
