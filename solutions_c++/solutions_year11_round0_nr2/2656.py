#include<iostream>
#include<string>

using namespace std;

int main(){
  
  int c,d,n;
  string s;
  cin >> n;
  for(int ii=0;ii<n;ii++){
    char ch[100][100]={{0}},ch2[100][100]={{0}};
    cin >> c; 
    for(int i=0;i<c;i++){
      cin >> s;
      if(ch[s[0]][s[1]]==0)
	ch[s[0]][s[1]]=ch[s[1]][s[0]]=s[2];
    }
    cin >> d;
    for(int i=0;i<d;i++){
      cin >> s;
      ch2[s[0]][s[1]]=ch2[s[1]][s[0]]=1;
    } int p;
    cin >> p;
    cin >> s;
    for(int i=0;i<s.length();i++){
      //cout << "now : " << s << endl;
      if(i==0)i++;
      if(ch[s[i]][s[i-1]]!=0){
	string tmp=s.substr(0,i-1);
	tmp+=ch[s[i]][s[i-1]];
	tmp+=s.substr(i+1);
	s=tmp;
      }
      for(int j=0;j<i;j++){
	if(ch2[s[j]][s[i]]!=0){
	  s=s.substr(i+1);
	  i=0;
	  break;
	}
      }
    }
    printf("Case #%d: [",ii+1);
    for(int i2=0;i2<s.length();i2++){
      if(i2!=0)printf(", ");
      cout << s[i2];
    }
    cout << "]" << endl;
  }

  return 0;
}
