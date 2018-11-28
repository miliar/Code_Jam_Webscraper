#include<vector>
#include<iostream>
#include<string.h>
#define ll long long	
using namespace std;
vector<string> engines;
vector<int> queries;
ll best(int q){
	vector<bool> in;
	int incount=0;
	for(int i=0;i<engines.size();i++)
		in.push_back(false);
	while(q<queries.size()){
		//cout<<engines[queries[q]]<<" "<<queries[q]<<" "<<incount<<endl;
		if(!in[queries[q]]){
			incount++;
			in[queries[q]]=true;
		}
		if(incount==engines.size()){
			//cout<<"switch at "<<q<<endl;
			return 1+best(q);			
		}
		q++;
	}
	return 0;
}
int main(){
	vector<int> engine,query;
	int N;
	cin>>N;
	//cout<<N<<endl;
	for(int i=0;i<N;i++){
		engines.clear();engine.clear();
		queries.clear();query.clear();
		int S,Q;
		cin>>S;
		//cout<<S<<endl;
		cin.ignore();
		for(int j=0;j<S;j++){
			string temp;
			getline(cin,temp);
			//cin>>temp;
			//cout<<temp<<endl;
			engines.push_back(temp);
		}
		cin>>Q;
		cin.ignore();
		//cout<<Q<<endl;
		for(int j=0;j<Q;j++){
			string temp;
			getline(cin,temp);
			//cin>>temp;
			//cout<<temp<<endl;
			int k=0;
			while(k<engines.size() && !(temp==engines[k])){
				k++;				
			}
			queries.push_back(k);
		}
		cout<<"Case #"<<i+1<<": "<<best(0)<<endl;		
	}	
}
