

#include <iostream>
#include <string>
#include <vector>
using namespace std;

string combine[40];
string diff[30];
string cmd;

int main()
{
	int test,cs,c,d,n,i=0;
	cin>>test;
	cs=0;
	while(cs++<test){
		cin>>c;
		i=c;
		while(i--)cin>>combine[i];
		cin>>d;
		i=d;
		while(i--)cin>>diff[i];
		cin>>n;
		cin>>cmd;
		
		if(cmd.length() != n){
			cout<<"Error!"<<endl;
			return 0;	
		}

		vector<char>v;

		
		for(int i=0;i<n;++i){
			char cur = cmd.at(i);

			if(v.size()<1){ v.push_back(cur);continue; }

			char pre = v[ v.size()-1 ];
			int j=0;

		
			for(j=0;j<c;++j){
				if( cur   == combine[j].at(0) && pre == combine[j].at(1) ) break;
				if( pre == combine[j].at(0) && cur   == combine[j].at(1) ) break;
			}


			if(j<c){
				v.pop_back();
				v.push_back( combine[j].at(2) );
			}
			else{

				for(j=0;j<d;++j){
					for(int k=0;k<v.size();++k){
						if( cur == diff[j].at(0) && v[k]== diff[j].at(1) ) {v.clear(); break;}
						if( v[k] == diff[j].at(0) && cur == diff[j].at(1) ){v.clear(); break;}
					}
				}

				if(v.size()>0)v.push_back( cur );
 			}
	
		}
	


		cout<<"Case #"<<cs<<": [";

		for(int i=0;i<v.size();++i){
			if(i)cout<<", "<<v[i];
			else cout<<v[i];
		}
		cout<<"]"<<endl;
	}

	return 0;
}
