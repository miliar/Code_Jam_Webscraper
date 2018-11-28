#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main(){
	string t;
	int N;
	getline(cin,t,'\n');
	N=atoi(t.c_str());
	ofstream out("out.txt");
	for(int i=0;i<N;i++){
		string temp;
		int count=0;
		int S;
		getline(cin,temp,'\n');
		S=atoi(temp.c_str());
		vector<string> engine(S);
		int num[S];
		for(int j=0;j<S;j++)
			num[j]=0;
		for(int j=0;j<S;j++){
			string s;
			getline(cin,s,'\n');
			engine[j]=s;
			//cout<<engine[j]<<endl;
		}
		sort(engine.begin(),engine.end());
		int Q;
		getline(cin,temp,'\n');
		Q=atoi(temp.c_str());
		int empty=S;
		for(int j=0;j<Q;j++){
			string s;
			getline(cin,s,'\n');
			vector<string>::iterator location=find(engine.begin(),engine.end(),s);
			int pos=location-engine.begin();
			if(empty==1&&location!=engine.end()&&num[pos]==0){
				num[pos]++;
				for(int k=0;k<S;k++){
					if(k==pos)
						continue;
					num[k]=0;
					
				}
				empty=S-1;
				count++;
				continue;
			}
			
			if(location!=engine.end()){
				if(num[pos]==0){
					num[pos]++;
					empty--;
				}
				else
					num[pos]++;
			}
		}
		out<<"Case #"<<i+1<<": "<<count<<endl;
	}
    system("pause");
    return 0;
}
