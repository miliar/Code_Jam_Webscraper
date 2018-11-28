#include <iostream>
#include <vector>


using namespace std;
typedef long long LL;
typedef vector<LL> vll;

LL value(vll & gr,LL Rides,LL k){
  //cout << "starting value " << endl;
  LL n = gr.size();
  vector<bool> seen(n,false);
  vll len(n,-1),price(n,0);
  int i =0,ind=0;  
  LL ride =0,earn =0,onride=0;
  //seen[0] = true;
  LL R = Rides;
  while(true){    
    ind = i %n;
    if(!R) return earn;
    //cout << i << " " << ind << " " << ride << endl;
    if((ride+gr[ind] <= k) && (onride < gr.size())){
      ride += gr[ind];
      ++onride;
      //cout << "add p" << endl;
    }
    else{      
      //cout << "round " << ride << " " << i << endl;
      --R;
      earn +=ride;      
      onride =1;
      ride =gr[ind];
      if(!seen[ind]){
	seen[ind] = true;
	price[ind] = earn;
	len[ind] = Rides-R;
      }
      else{	
	//cout << "cycle found " << endl;
	int cycle = Rides-R-len[ind];
	LL earnc = earn-price[ind];
	//	cout << "lc  " << cycle << " earnc " << earnc << endl;	
	earn+= (R/cycle)*earnc;
	R= R%cycle;
      }
    }
    ++i;
  }
  
}


int main(int argc,char*argv[]){
  LL t,r,k,n;
  cin >>t;
  for(int i=1;i<=t;++i){
    cin >> r >> k >> n;
    vll gr(n,0);
    for(int j=0;j<n;++j)
      cin >>gr[j];
    cout << "Case #" << i << ": " << value(gr,r,k) << endl;
  }
}

