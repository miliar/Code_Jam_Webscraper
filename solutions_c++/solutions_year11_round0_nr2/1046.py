#include<set>
#include<map>
#include<iostream>
#include<list>
using namespace std;


int main(){
	int T;

	cin>>T;

	for(int i = 0 ; i < T; i++){
		int a;
		cin>>a;
		string r;
		map<string,char> invoke;
		set<string> clean;

		for(int j = 0 ; j < a; j++){
			string s;
			cin>>s;
//			cout<<" s " << s <<endl;
//			cout<< s.substr(0,2)<<endl;;
			invoke[s.substr(0,2)] = s[2];
			string s2;
			s2.push_back(s[1]);
			s2.push_back(s[0]);
			invoke[s2] = s[2];
		}

		int b;
		cin>>b;
		for(int j = 0;  j < b; j++){
			string s;
			cin>>s;
//			cout<<" s " << s <<endl;
			
			string s2;
			s2.push_back(s[1]);
			s2.push_back(s[0]);
	

			clean.insert(s);
			clean.insert(s2);
		} 

//		for(map<string,char>::iterator it = invoke.begin(); it!= invoke.end(); it++){
//			cout<<"invoke = "<< it->first << " -- " << it->second<<endl; 
//		}

		int tam;
		string p;
		cin>>tam;
		cin>>p;
		list<char> l;
	
		for(int j = 0; j < tam; j++){
			char c = p[j];
			
//			cout<< "c = "<<c<<endl;

			if(l.empty()){
				l.push_back(c);
				continue;
			}
			
			char antigo = l.back();
			
			string padrao;
			padrao.push_back(antigo);
			padrao.push_back(c);
			
			if(invoke.find(padrao) != invoke.end()){
//				cout<<"achei padrao "<< padrao<< endl;
//				cout<<"inserindo  "<< invoke[padrao]<< endl;

				l.pop_back();
				l.push_back(invoke[padrao]);
				continue;
			}

			bool sai = false;
			for(set<string>::iterator it =  clean.begin(); it != clean.end(); it++){
				string pa = *it;

				if(pa[1] == c){
					for(list<char>::iterator itc = l.begin(); itc != l.end(); itc++){
						if(*itc == pa[0]){
							l.clear();
							sai = true;
				//			cout<<"Apaguei tudo"<<endl;
							break;
						}
		
					}
					if(sai)
						break;
				}

			}
			if(sai) continue;
			
			l.push_back(c);

		
		}

		cout<<"Case #"<<i+1<<": [";
		int size = l.size();
		int atual = 0;
		for(list<char>::iterator itc = l.begin(); itc != l.end(); itc++){
			cout<<*itc;
			atual++;
			if(atual < size)
			cout<<", ";
		}
		cout<<"]"<<endl;
		

	}
	




	return 0;
}


