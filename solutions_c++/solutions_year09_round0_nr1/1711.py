#include <iostream>
#include <vector>
#include <string>
#include <regex.h>
using namespace std;


int main() {
  int l, d, n;
  scanf("%d %d %d", &l, &d, &n);

//string pt="";
  vector<string> w;
  for(int i=0; i<d; i++) {
    string ppp;
    cin>>ppp;
    w.push_back(ppp);
//pt+=ppp+"/";
  }
  for(int iii=1; iii<=n; iii++) {
    string m;
    cin>>m;


regex_t reg;

string st=m;
for(int i=0; i<st.size(); i++) {
  if(st[i]=='(') st[i]='[';
  if(st[i]==')') st[i]=']';
}


regmatch_t matches[1];

regcomp(&reg,st.c_str(),REG_EXTENDED|REG_ICASE);




int nm=0;
for(int i=0; i<w.size(); i++) {
  if(regexec(&reg,w[i].c_str(),1,matches,0)==0) nm++;
}


regfree(&reg);


cout<<"Case #"<<iii<<": "<<nm<<endl;






  }

  return 0;
}
