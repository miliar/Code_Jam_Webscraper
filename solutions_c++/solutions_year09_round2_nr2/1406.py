# include <iostream>
using namespace std;
int main()
{
    string str,str1;
    int test,nooftest=1;
    cin>>test;
    while (nooftest<=test)
    {
          cin>>str;
          str1=str;
          next_permutation(str1.begin(),str1.end());
          if (str<str1)
          {
                       
          cout<<"Case #"<<nooftest++<<": "<<str1<<endl;
          continue;
          }
          else 
          {
          
          
          
          
          str.insert(1,"0");
          sort(str.begin(),str.end());
          while (next_permutation(str.begin(),str.end()))
          if(str[0]!='0')
          break;
          
          
          
          
          cout<<"Case #"<<nooftest++<<": "<<str<<endl;
          
          }
          
    }
    
    return 0;
    
}

