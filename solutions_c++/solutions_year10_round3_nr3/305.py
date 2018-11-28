
#include <iostream>
#include <vector>
#include <map>
#include <boost/lexical_cast.hpp>

struct pix
{
  int bwe;// black,white,empty
  int size;// subboard size

  pix():size(0){}
  void init(bool b)
  {
    bwe = b?1:-1;
    size = 0;
  }
};

int M,N;
std::vector<pix> field;
std::vector<int> bd;

int hex2int(char c)
{
  if('0'<=c && c<='9')
    return c-'0';
  else
    return (c-'A')+0xA;
}

pix& at(int m,int n)
{
  return field[m*N+n];
}

void calcAt(int m,int n)
{
  if(at(m,n).bwe !=0){
    if(m==0 || n==0){
      at(m,n).size = 1;
      return;
    }
    if(at(m,n-1).bwe == -at(m,n).bwe
       && at(m-1,n).bwe == -at(m,n).bwe
       && at(m-1,n-1).bwe == at(m,n).bwe){
      at(m,n).size = std::min(at(m-1,n).size,std::min(at(m,n-1).size,at(m-1,n-1).size))+1;
      //std::cout << at(m,n).size << ".\n";
    }
    else{
      at(m,n).size = 1;
    }
  }
}

void update_field()
{
  for(int m=0;m<M;++m){
    for(int n=0;n<N;++n){
      calcAt(m,n);

    //   switch(at(m,n).bwe){
    //   case -1:std::cout << '.';break;
    //   case 0:std::cout << '-';break;
    //   case 1:std::cout << '*';break;
    //   }
    }
    // std::cout << '\n';
  }
}

bool cut()
{
  int max_size = 0;
  int max_at_m = 0;
  int max_at_n = 0;

  for(int m=0;m<M;++m){
    for(int n=0;n<N;++n){
      if(at(m,n).bwe && at(m,n).size > max_size){
        max_size = at(m,n).size;
        max_at_m = m;
        max_at_n = n;
      }
    }
  }


  if(max_size==0)
    return false;

  //std::cout << max_size << "@" << max_at_m << ' ' << max_at_n << "\n";
  bd.push_back(max_size);

  for(int m=0;m<max_size;++m){
    for(int n=0;n<max_size;++n){
      at(max_at_m-m,max_at_n-n).bwe = 0;
    }
  }
  return true;
}

int main(int,char**)
{
  int T;
  std::cin >> T;
  for(int t=0;t<T;++t){
    //int M,N;
    std::cin >> M >> N;

    field.resize(M*N);
    for(int m=0;m<M;++m){
      for(int n=0;n<N/4;++n){
        char c;
        std::cin >> c;
        int p = hex2int(c);

        at(m,4*n).init(p&0x8);
        at(m,4*n+1).init(p&0x4);
        at(m,4*n+2).init(p&0x2);
        at(m,4*n+3).init(p&0x1);
      }
    }

    do{
      update_field();
    }while(cut());


    std::map<int,int> res;
    while(!bd.empty()){
      ++res[bd.back()];
      bd.pop_back();
    }
    std::cout << "Case #" << (t+1) << ": " << res.size() << '\n';

    for(auto itr=res.rbegin();itr!=res.rend();++itr){
      std::cout << itr->first << " " << itr->second << '\n';
    }
  }

  return 0;
}
