#include<iostream>
#include<cstdio>
#include<string>
#include<algorithm>
#include<set>
#include<map>

using namespace std;

int main() {

	int tc, C, D, N;

	cin >> tc;
	
	for(int cases=1;cases<=tc;cases++) { 
		
			cin >> C;
			string str; string tmp;
			map< string, string > combine;
			map< string, string > oppose;

			for(int i=0;i<C;i++) { 
				cin >> str;   //cout << "str:" << str << endl;
				
				tmp = str.substr(0,2); //cout << "t:"<< tmp << endl;
				combine[tmp] = str.substr(2,1);
				tmp.clear();
				
				tmp = str.substr(1,1)+str.substr(0,1); //cout << "t:" << tmp << endl;
				combine[tmp] = str.substr(2,1);
				tmp.clear();

				str.clear(); 
			}
		
			cin >> D;
				
			for(int i=0;i<D;i++) { 
				str.clear();	
				tmp.clear();
				cin >> str; //cout << "str:" << str << " "; 
					
				tmp = str.substr(0,1); 
				oppose[tmp] = str.substr(1,1);
				//cout << tmp << " -> " << str.substr(1,1) << endl;
				tmp.clear();
				
				tmp = str.substr(1,1);
				oppose[tmp] = str.substr(0,1);
				//cout << tmp << " -> " << str.substr(0,1) << endl;

			}

			cin >> N;
			string toInvoke, oplist="";
			
			cin >> toInvoke;
			//cout << endl << "toInvoke:" << toInvoke << endl; 
			

			oplist += toInvoke.substr(0,1);

			map< string, string > :: iterator it, ito;
			
			for(int i=1;i<toInvoke.length();i++) { 
				tmp.clear();	
				oplist += toInvoke.substr(i,1);
				if(oplist.length() == 1) continue;
				tmp = oplist.substr(oplist.length()-2,2);
				//cout << "t:" << tmp << endl;
			
				it = combine.find(tmp);	

				int pos=oplist.length()-2;

				if(it != combine.end()) { 
					oplist.replace(pos,2,combine[tmp]);	
					//cout << "opl in if:" << oplist ;
				}
				else {
					tmp.clear(); 
					//cout << "opl in el:" << oplist ;
					pos = oplist.length();
					//	cout << "{" ;
					tmp = oplist.substr(pos-1,1);
					//	cout << "}" << endl;
					//cout << " last:" << tmp << "-> ";
					ito = oppose.find(tmp);
					
					bool clear = false;

					if(ito != oppose.end()) { 
						//cout << ((*ito).second) << endl;
						pos = oplist.length();	
						for(int x=0;x<pos-1;x++) { 
							string tosee = (*ito).second;	
							if(oplist[x] == tosee[0]) {
								clear = true; break;
							}	
						}
						if(clear) {
								//cout << "ol clear " << endl;
								oplist.clear(); clear = false;	
								oplist ="";
						}
					}
					
				}//else
				//cout << endl << "opf:" << oplist << endl;
			}//for
			
			cout << "Case #" << cases << ": ";
			cout << "[" ;
			
			if(!oplist.empty()) {
				for(int i=0;i<oplist.length()-1;i++) { 
					cout << oplist[i] << ", ";
				}
				int len=oplist.length();
				if(len > 0) cout << oplist[len-1] ;
			}

			cout << "]" << endl;
			
			oppose.clear();
			combine.clear();	
		
	}//tc

	return 0;	
}
