#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

string int2str(int n){
  string ret;
  while ( n>0 ){
    char tmp=((n%10)+'0');
    ret = tmp + ret;
    n /= 10;
  }
  return ret;
}

int sub1(){
  int A;
  int B;
  cin >> A;
  cin >> B;
  
  string Astr=int2str(A);
  string Bstr=int2str(B);
  //cout << endl; 
  //cout << Astr <<"-"<< Bstr << endl;
  
  int ret=0;
  for ( int i=A ; i<=B ; i++ ){
    string tmp=int2str(i);
    
    vector<string> checked;
    checked.clear();
    for ( unsigned int k=1 ; k<Astr.size() ; k++ ){
      //if ( tmp.substr(0,k)==tmp.substr(Astr.size()-k, k) ){
      string cat=tmp.substr(Astr.size()-k, k)+tmp.substr(0,Astr.size()-k);
      if ( tmp!=cat && tmp<cat && Astr<cat && cat<=Bstr ){
	
	int ischecked=false;
	for ( unsigned int m=0; m<checked.size() ; m++ )
	  if ( cat==checked[m] ){
	    //ret--;
	    ischecked=true;
	    break;
	  }
	
	if ( ischecked==false ){
	  checked.push_back(cat);
	  ret++;
	}
	//cout << tmp <<":"<< cat << endl;
      }  
    } 
  }
  
  return ret;
}


int main (int argc, char*argv[]){
  int T;
  cin >> T;
  
  for ( int i=0 ; i<T ; i++ ){
    cout << "Case #" << i+1 << ": " ;  
    cout << sub1();
    cout << endl;
  }
  
  return 1;
};


