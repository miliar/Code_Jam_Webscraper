#include<string>
#include<iostream>
#include<algorithm>

int main()
{
  int n;
  std::cin>>n;
  for(int i=0;i<n;i++)
  {
  std::string str;
  std::cin>>str;
  if(std::next_permutation(str.begin(),str.end()))
  {
  }else
  {
    str.push_back('0');
    std::sort(str.begin(),str.end());
    for(int i=0;i<str.size();i++)
    {
      if(str[i]!='0')
      {
        std::swap(str[0],str[i]);
        break;
      }
    }
  }
  std::cout<<"Case #"<<(i+1)<<": ";
    std::cout<<str<<"\n";
  }
}
