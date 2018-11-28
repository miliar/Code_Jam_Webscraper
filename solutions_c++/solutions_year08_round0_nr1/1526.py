#include <iostream>
#include <vector>
#include <string>
#define pb push_back
using namespace std;

int main() {
  int n;
  cin>>n;
  for(int cas=1;cas<=n;cas++) {
    int s;
    cin>>s;
    string temp;
    getline(cin,temp);

    vector <string> engines;
    for(int i=0;i<s;i++) {
     
      getline(cin,temp);
      engines.pb(temp);
      //cout<<temp<<endl;
    }
    //cout<<endl;
    int q;
    cin>>q;      
    getline(cin,temp);

    int row[1000];
    for(int i=0;i<q;i++) {
      int temprow[1000];
      string query;
      getline(cin,query);
      //cout<<query<<endl;

      if(i==0){
	for(int j=0;j<engines.size();j++) {
	  row[j]=(query==engines[j])?100000:0;
	  //cout<<row[j]<<" ";
	}
	//cout<<endl;
      }
      else {
	for(int j=0;j<engines.size();j++) {
	  //cout<<query<<":"<<engines[j]<<endl;
	  if(query==engines[j])
	    temprow[j]=100000;
	  else {
	    int min=row[j];
	    for(int k=0;k<engines.size();k++){
	      if(row[k]+1<min)
		min=row[k]+1;
	    }
	    temprow[j]=min;
	  }
	}
      
	for(int j=0;j<engines.size();j++) {
	  //cout<<temprow[j]<<" ";
	  row[j]=temprow[j];
	}
	//cout<<endl;
      }
    }
    int min=100000;
    for(int i=0;i<engines.size();i++)
      if(row[i]<min)
	min=row[i];
    cout<<"Case #"<<cas<<":"<<" "<<min<<endl;
    
  }
  
  return 0;
}
