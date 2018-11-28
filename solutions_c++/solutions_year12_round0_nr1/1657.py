#include <iostream>
using namespace std;

char hash[26]=
{
// a   b   c   d   e   f   g
  'y','h','e','s','o','c','v',
// h   i   j   k   l   m   n
  'x','d','u','i','g','l','b',
// o   p   q
  'k','r','z',
// r   s   t
  't','n','w',
// u   v   w
  'j','p','f',
// x   y   z
  'm','a','q'
};

int main()
{
  freopen("A-small-attempt0.in","r",stdin);
  freopen("A-small-attempt0.out","w",stdout);
  int T,i,j;
  char str[500];

  cin>>T;
  cin.getline(str,500);
  for (i=1; i<=T; ++i)
    {
      cin.getline(str,500);
      
      for (j=0; str[j]!=0; ++j)
        if (str[j]!=' ')
          str[j]=hash[str[j]-'a'];
          
      cout<<"Case #"<<i<<": "<<str<<endl;
    }

  fclose(stdin);
  fclose(stdout);
  
  return(0);
}
