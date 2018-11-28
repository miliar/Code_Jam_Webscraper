#include<iostream>
#include<vector>
#include<string>
#include<cassert>
#include<iomanip>


std::string welcome = "welcome to code jam";
std::vector<int> pos[256];
int ca = 1;
void handle_case(std::string line)
{
  int arr[19] = {};
  arr[0] = 1;
  for(int i=0;i<line.size();i++)
  {
    unsigned char c = line[i];
    for(int j=0;j<pos[c].size();j++)
    {
      int p = pos[c][j];
      arr[p]+=arr[p-1];
      arr[p]%=10000;
    }
  }
  std::cout<<"Case #"<<ca<<": "<<std::setw(4)<<std::setfill('0')<<arr[19]<<"\n";
  ca++;

}

int main()
{
  assert(welcome.size()==19);
  for(int i=0;i<welcome.size();i++)
  {
    unsigned char c = welcome[i];
    pos[c].push_back(i+1);
  }
  int n;
  std::cin>>n;
  std::string line;
  std::getline(std::cin,line);
  for(int i=0;i<n;i++)
  {
    std::getline(std::cin,line);
    //std::cout<<line<<"\n";
    handle_case(line);
  }


}

