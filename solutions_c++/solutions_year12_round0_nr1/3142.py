#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<iostream>
#include<fstream>
#include<vector>
#include<map>
#include<cassert>

using namespace std;


map<char,char > mpchar;

void update_dict(char *exam,char *ans){
  assert(strlen(exam)==strlen(ans));
  for(int i=0;i<strlen(exam);i++){
    map<char,char>::iterator it=mpchar.find(exam[i]);
    if(it==mpchar.end()){
      mpchar[exam[i]]=ans[i];
      //mpchar[ans[i]]=exam[i];
    }
  }
}

int main(int argc,char* argv[]){
  char exam1[]={"ejp mysljylc kd kxveddknmc re jsicpdrysi"};
  char exam2[]={"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"};
  char exam3[]={"de kr kd eoya kw aej tysr re ujdr lkgc jv"};
  char ans1[]={"our language is impossible to understand"};
  char ans2[]={"there are twenty six factorial possibilities"};
  char ans3[]={"so it is okay if you want to just give up"};
  update_dict(exam1,ans1);
  update_dict(exam2,ans2);
  update_dict(exam3,ans3);
  mpchar['z']='q';
  mpchar['q']='z';
  ifstream ifs(argv[1]);
  int N;
  ifs>>N;
  string buf;
  getline(ifs,buf);
  for(int i=0;i<N;i++){
    getline(ifs,buf);
    printf("Case #%d: ",i+1);
      for(int i=0;i<buf.length();i++)
	printf("%c",mpchar[buf[i]]);
    printf("\n");
  }
  return 0;
}

