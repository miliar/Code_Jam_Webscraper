#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>

using namespace std;
int main( )
{
	int i, j, k, q, qq;
	int ss[128];
	char mystr[102];
	ss[32]=32;
	ss[97]=121,ss[98]=104,ss[99]=101,ss[100]=115,ss[101]=111,ss[102]=99,ss[103]=118,ss[104]=120,ss[105]=100,ss[106]=117,ss[107]=105;
	ss[108]=103,ss[109]=108,ss[110]=98,ss[111]=107,ss[112]=114,ss[113]=122,ss[114]=116,ss[115]=110,ss[116]=119,ss[117]=106,ss[118]=112;
	ss[119]=102,ss[120]=109,ss[121]=97,ss[122]=113 ;

	cin>>qq;
	cin.getline(mystr,100,'\n');
	for( q = 1; q <= qq; ++ q )
	{
	   std::cin.getline(mystr,101,'\n');
	   i=0;
	   while(mystr[i])
	   {  mystr[i]=ss[mystr[i]]; i++;      }
	
	   printf("Case #%d: %s\n",q,mystr);
	}

 return 0;
}
