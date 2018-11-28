#include <iostream>
#include <string>
using namespace std;

int main ()
{
    string m[26] = {"y","h","e","s","o","c","v","x","d","u","i","g","l","b","k","r","z","t","n","w","j","p","f","m","a","q"  };
    int t,i,len,j=1;
    string mystr;

    char ch;

    scanf("%d",&t);

    cin>>ch;

     while(j<=t)
    {

  getline (cin, mystr);
  len = mystr.length();

  cout<<"Case #"<<j<<": ";

      int n = (int)ch;

      if(j==1)
     cout<<m[n-97];


  for(i=0;i<len;i++)
  {
    int num = (int)mystr[i];


    if(num>=97 && num<=122 )
    cout<< m[num-97];
    else
    cout<<" ";

  }
  cout<<endl;
  j++;
    }
  return 0;
}
