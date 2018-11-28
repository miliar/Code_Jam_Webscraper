#include<set>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

set<string> old;
set<string> needed;
set<string>::iterator ito;
//set<int>::iterator itn;

vector<string> get_subs(string dir){
  string temp = dir + "/";
  vector<string> ans;
  for(int i=0; i<temp.size(); i++){
    if(temp[i]=='/' && i>0){
      // cout<<"b4"<<endl;
      ans.push_back(temp.substr(0,i));
      //   cout<<temp.substr(0,i)<<endl;
    }  
}
  return ans;
}

int main(){
  int tst_cases,exist,want;  
  cin>>tst_cases;
  for(int cse =1; cse<=tst_cases; cse++){
    needed.clear();
    old.clear();
    cin>>exist>>want;
    // cout<<exist<<want<<endl;
    // cin>getline(
    string tmp;    
    getline (cin,tmp);
    cout<<tmp;
    //store old ones
    for(int i=0; i<exist; i++){
      //    cout<<"before get line"<<endl;
      getline(cin,tmp);
      //   cout<<tmp<<endl;
      vector<string> subs =  get_subs(tmp);
      for(int j=0; j<subs.size(); j++){
	//cout<<"before insert"<<endl;
	//	subs[j];
	//cout<<"before before insert"<<subs <<endl;
	old.insert(subs[j]);
	//cout<<"after insert"<<endl;
      }
    }
    //  cout<<"got here"<<endl;
    // for(ito=old.begin(); ito!=old.end(); ito++){
       //   cout<<(*ito)<<endl;
    //  }

     //cout<<"old size "<<old.size()<<endl;

     int numb_old = old.size();

    //find new ones
    for(int i=0; i<want; i++){
      getline(cin,tmp);
      vector<string> subs =  get_subs(tmp);
      for(int j=0; j<subs.size(); j++){
	old.insert(subs[j]);
	//ito = old.end();
	//	if(old.find(subs[j])!=old.end() || needed.find(subs[j])!= needed.end()){
		  // needed.insert(subs[j]);
		  //	}
      }
    }

    cout<<"Case #"<<cse <<": "<< old.size() - numb_old <<endl;


  }

  return 0;
}

