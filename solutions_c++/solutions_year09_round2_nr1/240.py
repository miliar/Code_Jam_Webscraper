#include <iostream>
#include <sstream>
#include <map>
#include <string>
using namespace std;
string a;
map<string,bool>h;
struct tree{
  double weight;
  string feature;
  tree* l,*r;
};
void process(string x,tree* y){
  int l,r;
  y->l=y->r=0;
  
  //  cout << x <<endl;
  
  for (l = 0; l < x.length(); ++l)if (x[l]=='(') break;
  for (r = x.length()-1; r>=0; --r) if (x[r]==')') break;
  string t = x.substr(l+1,r-l-1);
  //  cout << t <<endl;
  
  istringstream iss(t);
  iss >> (y->weight);
  //  cout << y->weight << endl;
  
  if (iss >> y->feature){
    y->l = new tree();
    y->r= new tree();
    string pk;
    getline(iss,pk);
    int l = 0,p=0;
    while (pk[l]!='(')++l;
    p=1;
    while (p>0){
      ++l;
      if (pk[l]=='(') ++p;
      if (pk[l]==')') --p;
    }
    process(pk.substr(0,l+1),y->l);
    process(pk.substr(l+1),y->r);
  }
}


int main(){
  int t,cas=0;
  cin >> t;
  while (t--){
    int n;
    cout << "Case #"<<++cas<<":\n";
    cin >>n;
    string pk;
    a="";
    getline(cin,pk);
    while (n--){
      getline(cin,pk);
      a+=" "+pk;
    }
    tree *root = new tree();
    process(a,root);
    
    int m;
    cin >>m;
    while(m--){
      string s;
      int p;
      cin >> s;
      cin >> p;
      h.clear();
      //      cout <<"haha\n";
      
      while (p--){
	string w;
	cin >> w;
	h[w]= true;
      }
      double x = 1;
      tree *temp=root;
      while (temp->l!=0){
	//	cout << x <<endl;
	//	cout <<"?\n"<<temp->l <<" "<<temp->feature<<endl;
	
	x*=temp->weight;
	//	cout << temp->feature <<endl;
	
	if (h.find(temp->feature)==h.end()){
	  
	  temp = temp->r;
	  //	   cout <<"r\n";
	  
	}
	
	else{ 
	  temp = temp->l;
	  //	  cout <<"l\n";
	}
      }
      if (temp!=0)
      x = x*temp->weight;
      
      cout << x <<endl;
      
    }
    

  }  
}
