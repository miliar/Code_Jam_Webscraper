
/*Gowtham Chilamakuri*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <queue>
#include <cassert>
using namespace std;
main()
{
	int x,y;
	scanf("%d%*c",&x);
	for(y=1;y<=x;y++)
	{
		int i,j;
		string a("yhesocvxduiglbkrztnwjpfmaq");
		string b;
		getline(cin,b);
		printf("Case #%d: ",y);
		for(i=0;i<b.length();i++)
		{
			if(b[i]==' ')
			{
				printf(" ");
			}
			else
			{
				j=b[i];
				j=j-97;
				//printf("%d",j);
				printf("%c",a[j]);
			}
		}
		printf("\n");
	}
	return 0;
}
