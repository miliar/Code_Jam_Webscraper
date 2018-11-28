#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>

using namespace std;
int main( )
{
    int i, j, k, temp, temp1;   
    int a[128];
    char str[102];
    a[32]=32;
    a[97]=121,a[98]=104,a[99]=101,a[100]=115,a[101]=111,a[102]=99,a[103]=118,a[104]=120,a[105]=100,a[106]=117,a[107]=105;
    a[108]=103,a[109]=108,a[110]=98,a[111]=107,a[112]=114,a[113]=122,a[114]=116,a[115]=110,a[116]=119,a[117]=106,a[118]=112;
    a[119]=102,a[120]=109,a[121]=97,a[122]=113 ;

    cin>>temp1;
    cin.getline(str,100,'\n');
    for( temp = 1; temp <= temp1; ++ temp )
    {
    std::cin.getline(str,101,'\n');
    i=0;
    while(str[i])
    { 
      str[i]=a[str[i]]; i++;
    }
    printf("\nCase #%d: %s\n",temp,str);
    }
     return 0;
}
				
