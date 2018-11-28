#include<iostream>
#include<cstdio>

using namespace std;

int main(){
  char mappings[26];
  mappings[0]='y';//a
  mappings[1]='h';mappings[2]='e';mappings[3]='s';mappings[4]='o';//e
  mappings[5]='c';mappings[6]='v';
  mappings[7]='x';//h
  mappings[8]='d';
  mappings[9]='u';//j
  mappings[10]='i';
  mappings[11]='g';
  mappings[12]='l';
  mappings[13]='b';//n
  mappings[14]='k';
  mappings[15]='r';
  mappings[16]='z';
  mappings[17]='t';//r
  mappings[18]='n';
  mappings[19]='w';
  mappings[20]='j';
  mappings[21]='p';//v
  mappings[22]='f';
  mappings[23]='m';
  mappings[24]='a';
  mappings[25]='q';//z
  int T;
  string ss;
  scanf("%d", &T);
  getline (cin,ss);
  for(int j = 1 ; j <= T ; j++){
   getline (cin,ss);
   int len = ss.length();
   for(int i = 0; i < len; i++){
      if(ss[i] == ' ')continue;
      ss[i] = mappings[ ss[i] - 97 ];
   }
   cout << "Case #"<<j<<": " <<ss << endl;
  }
}

