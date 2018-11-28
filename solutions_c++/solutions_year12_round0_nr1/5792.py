#include <iostream>
#include <fstream>
#include <sstream>

#define MAX_CHAR 100
#define MAX_CASE 30

class Translator{
 private:
  char dict[1024];
 public:
  int learn(const char* input_str,const char* output_str);
  char convChar(char c);
  int display();
};

int
Translator::learn(const char* ci,const char* co)
{
  for(int i=0;i<MAX_CHAR;i++){
    if(ci[i] == '\0')
    	break;
    dict[ci[i]] = co[i];
  }
  return 0;
}

char
Translator::convChar(char c){
  return dict[c];
}

int
Translator::display(){
  for(int i=0;i<1024;++i){
    if(dict[i]!='\0'&&dict[i]!=' '){
      std::cout<<"idx:";
      printf("%c",i);
      std::cout<<":: "<<dict[i]<<std::endl;
    }
  }
}

int
main(int argc,char** argv)
{
  
int base[]={'a','b','c','d','e','f',
            'g','h','i','j','k','l',
            'm','n','o','p','q','r',
            's','t','u','v','w','x',
            'y','z'};

const char* src[4];
src[0]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
src[1]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
src[2]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
src[3]="qeez";

const char* res[4];
res[0]="our language is impossible to understand";
res[1]="there are twenty six factorial possibilities";
res[2]="so it is okay if you want to just give up";
res[3]="zooq";

Translator* tr = new Translator();
for(int i=0;i<4;i++){
  tr->learn(src[i],res[i]);
}

char c;
int T=0;
std::ifstream ifs(argv[1]);
std::string buff;
getline(ifs,buff);

T=atoi(buff.c_str());
for(int j=0;j<T;j++){  
  std::string sout;
  getline(ifs,buff);
  const char* cchar = buff.c_str();
  for(int k=0;k<MAX_CHAR;k++){
    if(cchar[k]=='\0')break;
    sout+=tr->convChar(cchar[k]);
  }
  if(sout.size()!=0){
    printf("Case #%d: ",j+1);
    std::cout<<sout<<std::endl;
    sout="";
  }
}
  return 0;
}
