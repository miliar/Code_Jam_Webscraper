#include <iostream>
#include <string>
#define C 36
#define D 28
using namespace std;

main(){
  int t, c, d, n;
  string combine[C];
  string opposed[D];
  string data;
  cin >> t;
  for(int tc=0;tc<t;tc++){
    cin >> c;
    for(int i=0;i<c;i++) cin >> combine[i];
    cin >> d;
    for(int i=0;i<d;i++) cin >> opposed[i];
    cin >> n;
    cin >> data;
    bool inc=true, ind=true;
    if(c==0) inc=false;
    if(d==0) ind=false;
    while(1){
      bool end=true;
      for(int i=1;i<data.size();i++){
	for(int j=0;j<c;j++){
	  if((data[i-1]==combine[j][0] && data[i]==combine[j][1]) || (data[i-1]==combine[j][1] && data[i]==combine[j][0]) ){
	    end=false;
	    string tmp=data;
	    data="";
	    for(int k=0;k<tmp.size();k++){
	      if(k==i-1){
		data+=combine[j][2];
		k++;
	      }else data+=tmp[k];
	    }
	    i-=2;
	  }
	}
	for(int j=0;j<d;j++){
	  bool opp[2];
	  opp[0]=false, opp[1]=false;
	  int l=-1;
	  for(int k=0;k<=i;k++){
	    if(data[k]==opposed[j][0]) opp[0]=true;
	    else if(data[k]==opposed[j][1]) opp[1]=true;
	    if(opp[0] && opp[1]){
	      l=k;
	      break;
	    }
	  }
	  if(l==-1) continue;
	  end=false;
	  string tmp=data;
	  data="";
	  for(int k=l+1;k<tmp.size();k++){
	    data+=tmp[k];
	  }
	  i=0;
	}
      }
      if(end) break;
    }
    cout << "Case #" << tc+1 << ": [";
    if(data.size()==0) cout << ']' << endl;
    else{
      cout << data[0];
      for(int i=1;i<data.size();i++){
	cout << ", " << data[i];
      }
      cout << ']' << endl;
    }
  }
  return 0;
}
