#include<iostream>
#include<vector>
#include<string>

using namespace std;

vector<string> get_nth_set(string exp,int n){
	vector<string> set;
	int state = 2;
	int at = 0;
	for(int i = 0; i< exp.size(); i++){
		string s = exp.substr(i,1);
		if(at>n){break;}
		if(s=="("){
			state = 1;continue;
		}
		if(s==")"){
			state = 2;at++;continue;
		}
		if(at==n){
			if(state==1){
				set.push_back(s);continue;
			}
			else{
				set.push_back(s);break;
			}
		}
		if(state==2){at++;}
	}
	return set;
}

bool chk_set_contains(string element, vector<string> set){
	for(int i = 0; i<set.size(); i++){
		if(set[i] == element){
			return true;
		}
	}
	return false;
}

void mydisplay(vector<string> s){
	for(int i = 0; i<s.size(); i++){
		cout<<s[i]<<endl;
	}
}

int main(){
    int L,D,N;
    cin>>L>>D>>N;
    vector<string> valid;
    vector<string> exp;
	for(int i = 0; i<D; i++){
		string s;
		cin>>s;
		valid.push_back(s);
	}
	for(int i = 0; i< N; i++){
		string s;
		cin>>s;
		exp.push_back(s);
	}
    
	for(int i = 0; i < N ; i++){
		int count =0;
		bool valid_word = true;
		for(int j =0; j<D; j++){
			
			for(int k = 0; k<L; k++){
				if(!chk_set_contains(valid[j].substr(k,1),get_nth_set(exp[i],k))){
					valid_word = false;
					break;
				}
			}
			if(valid_word){
				count++;				
			}
			valid_word = true;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
    ///test
    /**
    cout<<"Valids"<<endl;
    for(int i = 0; i < valid.size() ; i++){
            cout<<valid[i]<<endl;
    }
    cout<<"inputs"<<endl;
    for(int i = 0; i < exp.size() ; i++){
            cout<<exp[i]<<endl;
    }  
    **/  
    ///
//	system("pause");
    return 0;
}


