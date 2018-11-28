#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
#include<set>
#include<cstdio>
#include<cmath>

using namespace std;

vector<string> index;

int main()
{
  int l,d,n;
  string str;
  index.clear();
  cin>>l>>d>>n;

  for(int i=0;i<d;i++){
    cin>>str;
    index.push_back(str);
  }

  cin.ignore();

  for(int i=0;i<n;i++){
    getline(cin,str);

    int idx=0;
    vector<string> part(l,"");  
    bool flg=false;

    for(int j=0;j<str.size();j++){
      if(str[j]=='('){
	flg=true;
	continue;
      }
      else if(str[j]==')'){
	flg=false;
	idx++;
	continue;
      }
      else if(flg){
	part[idx]+=str[j];
      }
      else {
	part[idx]+=str[j];
	idx++;
      }
    }


    int ans=0;
    for(int j=0;j<d;j++){
      bool f=true;

      for(int k=0;k<l;k++){
	bool match=false;
	for(int id=0;id<part[k].size();id++){
	  if(index[j][k]==part[k][id]){
	    match=true;
	    break;
	  }
	}
	if(!match){
	  f=false;
	  break;
	}
      }
      if(f)ans++;
    }
    cout<<"Case #"<<i+1<<": "<<ans<<endl;
  }
  return 0;
}
