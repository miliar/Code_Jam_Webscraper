#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <map>
#include <iostream>

using namespace std;

map<char,char> mc;

int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
    
    mc[' ']=' ',
    mc['a']='y',
    mc['b']='h',
    mc['c']='e',
    mc['d']='s',
    mc['e']='o',
    mc['f']='c',
    mc['g']='v',
    mc['h']='x',
    mc['i']='d',
    mc['j']='u',
    mc['k']='i',
    mc['l']='g',
    mc['m']='l',
    mc['n']='b',
    mc['o']='k',
    mc['p']='r',
    mc['q']='z',
    mc['r']='t',
    mc['s']='n',
    mc['t']='w',
    mc['u']='j',
    mc['v']='p',
    mc['w']='f',
    mc['x']='m',
    mc['y']='a',
    mc['z']='q';
    
    int t;
    scanf("%d",&t);
    cin.ignore();
    
    
    for(int j=0;j<t;j++)
    {
		printf("Case #%d: ",j+1);
		string str;	
		getline(cin,str);
		for(int i=0;i<str.size();i++)
		{
		  cout<<mc[str[i]];
		}
		
		cout<<endl;
	}
	return 0;
	
}
