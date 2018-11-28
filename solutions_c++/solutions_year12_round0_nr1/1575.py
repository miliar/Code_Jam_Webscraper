/*
LANG: C++
TASK: A
*/

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <queue>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <iomanip>

using namespace std;

int T;
map<char,char> mp;
char input[200],output[200];

void init(){
    mp['a']='y';
    mp['b']='h';
    mp['c']='e';
    mp['d']='s';
    mp['e']='o';
    mp['f']='c';
    mp['g']='v';
    mp['h']='x';
    mp['i']='d';
    mp['j']='u';
    mp['k']='i';
    mp['l']='g';
    mp['m']='l';
    mp['n']='b';
    mp['o']='k';
    mp['p']='r';
    mp['q']='z';
    mp['r']='t';
    mp['s']='n';
    mp['t']='w';
    mp['u']='j';
    mp['v']='p';
    mp['w']='f';
    mp['x']='m';
    mp['y']='a';
    mp['z']='q';
}

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	init();
	scanf("%d\n",&T);
	for(int i=1; i<=T; i++){
	    gets(input);
	    int j=0;
	    for(; input[j]!='\0'; j++){
	        if(input[j]==' '){
                output[j]=input[j];
	        }
	        else{
                output[j]=mp[input[j]];
	        }
	    }
	    output[j]='\0';
		cout<<"Case #"<<i<<": "<<output<<endl;
	}
	return 0;
}
