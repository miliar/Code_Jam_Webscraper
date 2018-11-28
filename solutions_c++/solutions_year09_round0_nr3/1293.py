#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

//0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
//w e l c o m e   t o     c  o  d  e     j  a  m

int main()
{
  int N,i,j,a[2][19],c;
  string s;
  cin>>N;
  getline(cin,s);
  for(c=1;c<=N;c++)
    {
      getline(cin,s);
      // cout<<s<<"\n";
      for(j=0;j<19;j++)
	a[0][j]=a[1][j]=0;
      for(i=0;i<s.length();i++)
	{
	  switch(s[i])
	    {
	    case 'w': a[1][0]=(a[0][0]+1)%10000;
	      break;
	    case 'e': a[1][1]=(a[0][1]+a[0][0])%10000;
	      a[1][6]=(a[0][6]+a[0][5])%10000;
	      a[1][14]=(a[0][14]+a[0][13])%10000;
	      break;
	    case 'l': a[1][2]=(a[0][2]+a[0][1])%10000;
	      break;
	    case 'c': a[1][3]=(a[0][3]+a[0][2])%10000;
	      a[1][11]=(a[0][11]+a[0][10])%10000;
	      break;
	    case 'o': a[1][4]=(a[0][4]+a[0][3])%10000;
	      a[1][9]=(a[0][9]+a[0][8])%10000;
	      a[1][12]=(a[0][12]+a[0][11])%10000;
	      break;
	    case 'm': a[1][5]=(a[0][5]+a[0][4])%10000;
	      a[1][18]=(a[0][18]+a[0][17])%10000;
	      break;
	    case ' ': a[1][7]=(a[0][7]+a[0][6])%10000;
	      a[1][10]=(a[0][10]+a[0][9])%10000;
	      a[1][15]=(a[0][15]+a[0][14])%10000;
	      break;
	    case 't': a[1][8]=(a[0][8]+a[0][7])%10000;
	      break;
	    case 'd': a[1][13]=(a[0][13]+a[0][12])%10000;
	      break;
	    case 'j': a[1][16]=(a[0][16]+a[0][15])%10000;
	      break;
	    case 'a': a[1][17]=(a[0][17]+a[0][16])%10000;
	      break;
	    }
	  for(j=0;j<19;j++)
	    a[0][j]=a[1][j];
	}
      printf("Case #%d: %04d\n", c, a[1][18]);
    }
}
