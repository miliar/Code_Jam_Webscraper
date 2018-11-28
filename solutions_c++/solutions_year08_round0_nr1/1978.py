#include<iostream>
#include<string>
#include<set>

using namespace std;

main(){
	int tc,case_no;
	cin>>tc;
	char dummy=getchar();
	for(case_no=1;case_no<=tc;case_no++){
		int num_e,num_q,i,j;
		cin>>num_e;
		string e[num_e];
		dummy=getchar();
		for(i=0;i<num_e;i++){
			getline(cin,e[i]);
		}
		cin>>num_q;
		string q[num_q];
		dummy=getchar();
		for(i=0;i<num_q;i++){
			getline(cin,q[i]);
		}
		int switches=0,processed_q=0;
		set<string> s;
		for(i=0;i<num_e;i++){
			s.insert(e[i]);
		}
		while(processed_q<num_q){
			s.erase(q[processed_q]);
			if(s.size()==0){
				switches++;
				for(i=0;i<num_e;i++){
					s.insert(e[i]);
				}
				s.erase(q[processed_q]);
			}
			processed_q++;
		}
//		if(switches==-1)
//			switches++;
		cout<<"Case #"<<case_no<<": "<<switches<<endl;
	}
	return 0;
}


