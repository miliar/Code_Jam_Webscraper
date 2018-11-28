#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

int map[26] = {'y','h','e','s','o','c','v','x','d','u','i',
                'g','l','b','k','r','z','t','n','w','j','p',
                'f','m','a','q'};


int main() {
freopen("A-small-attempt2.in","r",stdin);
freopen("p1.out","w",stdout);
  int T;
  cin>>T;
  cin.get();
  for(int i=0;i<T;i++) {
    char line[110];
    cin.getline(line,110);
    cout<<"Case #"<<(i+1)<<": ";
    for(int j=0;j<strlen(line);j++) {
      char c = line[j];
      if(c!=' ')
        c = map[c-'a'];
      cout<<c;
    }
    cout<<"\n";
  }
  return 0;
}

