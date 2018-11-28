#include<algorithm>

#include<iostream>
#include<string>
#include<vector>
#include<tr1/unordered_set>
int N,L,D;

std::vector<std::string> dict;

int ca = 1;


void handle_line(std::string reg)
{
  std::vector<std::tr1::unordered_set<char> > input(dict[0].size());

  int c = 0;
  for(int i=0;i<reg.size();i++)
  {

    if(reg[i]=='(')
    {
      i++;
      while(reg[i]!=')')
      {
        input[c].insert(reg[i]);
        i++;
      }
    }else
    {
      input[c].insert(reg[i]);
    }
    c++;
  }

  int count = 0;
  //std::cout<<reg<<"\n";
  for(int i=0;i<dict.size();i++)
  {
    bool match = true;
    for(int j=0;j<dict[i].size();j++)
    {
      if(input[j].count(dict[i][j])==0)
      {
        match = false;
      }
    }
    if(match)
    {
      count++;
    }
    //std::cout<<dict[i]<<" - "<<c<<"\n";
  }
  std::cout<<"Case #"<<ca<<": "<<count<<"\n";
  ca++;
}

int main()
{
  std::cin>>L>>D>>N;
  std::string line;
  for(int i=0;i<D;i++)
  {
    std::cin>>line;
    //std::cout<<"word:"<<line<<"\n";
    dict.push_back(line);
  }
  for(int i=0;i<N;i++)
  {
    std::cin>>line;
    //std::getline(std::cin,line);
    //std::cout<<"input:"<<line<<"\n";
    handle_line(line);
  }
  return 0;
}
