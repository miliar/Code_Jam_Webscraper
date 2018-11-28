#include <fstream>
#include <string>
using namespace std;

ifstream fin ("1.in");
ofstream fout("1.out");

char a[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
  string s,r;
  int n,i,j;
  fin >> n;
  getline (fin,s);
  for(i=1;i<=n;i++)
  {
    getline (fin,s);r="";
    //fout << s << endl;
    for(j=0;j<s.length();j++)
      if(s.at(j)==' ')
	r+=' ';
      else
	r+=a[(int)(s.at(j)-'a')];
    fout << "Case #" << i << ": " << r << endl;
  }
}
     
    