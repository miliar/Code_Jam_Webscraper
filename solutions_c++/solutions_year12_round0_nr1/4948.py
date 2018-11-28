using namespace std;

/*
author : ravi shukla 
*/


# include<iostream>
# include<cstdio>
# include<cstring>
# include<cstdlib>
# include<cmath>
# include<cassert>
# include<cctype>
# include<algorithm>

# include<vector>
# include<limits>
# include<list>
# include<stack>
# include<queue>
# include<set>
# include<map>
# include<bitset>
# include<sstream>
# include<deque>
# include<fstream>


int main(){
  int tcases,cnum=0;
  freopen("q1inp.in","r+",stdin);
  freopen("q1out.txt","w+",stdout);
  map<char,char> mp;
  //:O
  mp['a']='y';mp['b']='h';mp['c']='e';mp['d']='s';mp['e']='o';mp['f']='c';
  mp['g']='v';mp['h']='x';mp['i']='d';mp['j']='u';mp['k']='i';
  mp['l']='g';mp['m']='l';mp['n']='b';mp['o']='k';mp['p']='r';mp['q']='z';
  mp['r']='t';mp['s']='n';mp['t']='w';mp['u']='j';mp['v']='p';mp['w']='f';
  mp['x']='m';mp['y']='a';mp['z']='q';mp[' ']=' ';
  
  cin>>tcases;
  string istr;
  getline(cin,istr);
  while(tcases--){
    cnum++;
    string ostr="";
    getline(cin,istr);
    for(int i=0;i<istr.length();i++){
      ostr+=mp[istr[i]];
    }
    
    
    
    cout<<"Case #"<<cnum<<": "<<ostr<<endl;
    
  }
  
  return 0;
}























