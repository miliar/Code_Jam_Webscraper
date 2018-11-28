#include<iostream>
#include<vector>
#include<string>

using namespace std;


int main(){
  vector<char> v=vector<char>(26,'a');
  int T; 
  vector<string> s=vector<string>(T,"a");
  vector<string> t=s;
  string q=string(200,'a');
  v[0]='y'; v[1]='h';  v[2]='e';  v[3]='s'; v[4]='o';
  v[5]='c'; v[6]= 'v';   v[7]='x'; v[8]='d'; v[9]='u';
  v[10]='i'; v[11]='g'; v[12]='l'; v[13]='b'; v[14]='k';
  v[15]='r'; v[16]='z'; v[17]='t'; v[18]='n'; v[19]='w';
  v[20]='j'; v[21]='p'; v[22]='f'; v[23]='m'; v[24]='a'; v[25]='q';
					      
  
  cin>>T;
  s=vector<string>(T,"a");
  getline(cin,q);
 
  for (int i=0;i<T;i++){
    getline (cin, q);
    s[i]=q;
  }
 
  
  t=s;
  for (int i=0;i<T;i++){
    for (int j=0;j<s[i].size();j++){
      if (s[i][j]!=' ')
	t[i][j]=v[(int) (s[i][j]-'a')];
      else t[i][j]=' ';
    }
  }
  
  for (int i=0;i<T;i++)
    cout<<"Case #"<<i+1<<": "<<t[i]<<endl;
  return 0;
}
    
