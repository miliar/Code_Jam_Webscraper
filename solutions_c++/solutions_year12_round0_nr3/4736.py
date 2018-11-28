#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <list>

int 
main(int argc,char** argv)
{

std::ifstream ifs(argv[1]);
std::string buff;
getline(ifs,buff);
int T=atoi(buff.c_str());

int inA,inB;
for(int j=0;j<T;j++){  
  std::string sout;
  getline(ifs,buff);
  std::istringstream is(buff);
  is>>inB>>inA; 

int nout = 0;
int val1,val2;
val2 = inB;
for(val1=inA;val1>inB;val1--){
  char cval1[1024];
  char cval2[1024];
  sprintf(cval1,"%d",val1);//big 
  sprintf(cval2,"%d",val2);//small

  std::list<char> a_list,b_list,c_list;
  int i=0;
  while(cval1[i]!='\0'){
    a_list.push_back(cval1[i]);
    b_list.push_back(cval1[i]);
    c_list.push_back(cval2[i]);
    ++i;
  }

  while(true){
    std::list<char>::iterator ita = a_list.begin();
    a_list.push_back(*ita);
    a_list.pop_front();
    ita = a_list.begin();

    std::string out;
    while(ita!=a_list.end()){
      out+=*ita;
      ++ita;
    }
    int v = atoi(out.c_str());

    if(a_list==b_list)
      break;
    if(*ita=='0'){
      continue;
    //}else if(a_list > b_list){
    }else if( v > val1){
      continue;
    }else if( v < val2){
      continue;
    }
     ++nout;
     //std::cout<<v<<std::endl;
  }
}
  printf("Case #%d: %d\n",j+1,nout);
}

  return 0;
}
