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

using namespace std;

int main()
{
	int n,i,j;
	string str;
	cin>>n;
	for(i=0;i<=n;i++)
	{
	    getline(cin,str);
	    if(i!=0){
	    for(j=0;j<(int)str.size();j++)
	    {
	        switch(str[j])
	        {
	            case 'a' : str[j]='y';
	            break;
	            case 'b' : str[j]='h';
	            break;
	            case 'c' : str[j]='e';
	            break;
	            case 'd' : str[j]='s';
	            break;
	            case 'e' : str[j]='o';
	            break;
	            case 'f' : str[j]='c';
	            break;
	            case 'g' : str[j]='v';
	            break;
	            case 'h' : str[j]='x';
	            break;
	            case 'i' : str[j]='d';
	            break;
	            case 'j' : str[j]='u';
	            break;
	            case 'k' : str[j]='i';
	            break;
	            case 'l' : str[j]='g';
	            break;
	            case 'm' : str[j]='l';
	            break;
	            case 'n' : str[j]='b';
	            break;
	            case 'o' : str[j]='k';
	            break;
	            case 'p' : str[j]='r';
	            break;
	            case 'q' : str[j]='z';
	            break;
	            case 'r' : str[j]='t';
	            break;
	            case 's' : str[j]='n';
	            break;
	            case 't' : str[j]='w';
	            break;
	            case 'u' : str[j]='j';
	            break;
	            case 'v' : str[j]='p';
	            break;
	            case 'w' : str[j]='f';
	            break;
	            case 'x' : str[j]='m';
	            break;
	            case 'y' : str[j]='a';
	            break;
	            case 'z' : str[j]='q';
	            break;
	            case ' ' : str[j]=' ';
	            break;
	            default : break;
	        }
	    }
	    cout<<"Case #"<<i<<": "<<str<<endl;}
	}
	return 0;
}
