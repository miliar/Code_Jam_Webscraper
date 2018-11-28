#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main ()
{
  string mystr;
  int T;
  getline(cin,mystr);
  stringstream(mystr) >> T;
  string result;
  int temp=0;
  char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
  for(int i=0;i<T;i++)
  {
          getline(cin, mystr);
          result="";
          //cout<<mystr<<endl;
          for(int j=0;j<mystr.length();j++)
          {
                if(mystr[j]==' ')
                {
									result=result+' ';
								}
                else
                {
                    temp=int(mystr[j])-97;
                    result=result+a[temp];
								}
					}
					cout<<"Case #"<<(i+1)<<": "<<result<<endl;
	}  
  return 0;
}
