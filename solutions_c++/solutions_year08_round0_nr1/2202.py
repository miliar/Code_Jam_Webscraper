#include<iostream>
#include<map>
#include<string>

struct Kounter{
  int num_switches;
  int num_elig;
  std::map<std::string,bool> is_elig;

  Kounter();
  Kounter& add_engine(std::string& engine);
  Kounter& add_query(std::string& query);
  int rslt();
};

int main(){
  int n,m;
  std::string s;
  std::cin>>n;
  for(int i=1;i<=n;++i){
    Kounter counter;
    std::cin>>m;
    //this line removes redundant '\n'.
    std::getline(std::cin,s);
    while(m--){
      std::getline(std::cin,s);
      counter.add_engine(s);
    }
    std::cin>>m;
    //this line removes redundant '\n'.
    std::getline(std::cin,s);
    while(m--){
      std::getline(std::cin,s);
      counter.add_query(s);
    }
    std::cout<<"Case #"<<i<<": "
      <<counter.rslt()<<std::endl;
  }
  return 0;
}

Kounter::Kounter(){
  num_switches=0;
  num_elig=0;
}

int Kounter::rslt(){
  return num_switches;
}

Kounter& Kounter::add_engine(std::string& engine){
  num_elig++;
  is_elig[engine]=true;
  return *this;
}

Kounter& Kounter::add_query(std::string& query){
  if(!is_elig[query])
    return *this;
  else{
    is_elig[query]=false;
    num_elig--;
    if(0==num_elig){
      num_switches++;
      num_elig=is_elig.size()-1;
      for(std::map<std::string,bool>::iterator it=is_elig.begin();
	  it!=is_elig.end();
	  it++){
	(*it).second=true;
      }
      is_elig[query]=false;
    }
  }
  return *this;
}
