#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>

using namespace std;
int main( )
{
	int i, j, k, t, tt;
	int arr[128];
	char str[102];
	arr[32]=32;
	arr[97]=121,arr[98]=104,arr[99]=101,arr[100]=115,arr[101]=111,arr[102]=99,arr[103]=118,arr[104]=120,arr[105]=100,arr[106]=117,arr[107]=105;
	arr[108]=103,arr[109]=108,arr[110]=98,arr[111]=107,arr[112]=114,arr[113]=122,arr[114]=116,arr[115]=110,arr[116]=119,arr[117]=106,arr[118]=112;
	arr[119]=102,arr[120]=109,arr[121]=97,arr[122]=113 ;

	cin>>tt;
	cin.getline(str,100,'\n');
	for( t = 1; t <= tt; ++ t )
	{
	   std::cin.getline(str,101,'\n');
	   i=0;
	   while(str[i])
	   {  str[i]=arr[str[i]]; i++;      }
	
	   printf("Case #%d: %s\n",t,str);
	}

 return 0;
}
	