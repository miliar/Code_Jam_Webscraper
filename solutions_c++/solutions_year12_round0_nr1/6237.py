#include<iostream>
#include<map>
#include<stdio.h>
#include<string>
#include<vector>
#include<fstream>

using namespace std;

int main () {
    map<char,char>ID;

//freopen("input.in","r",stdin);
//freopen("output.out","w",stdout);

    
// initialize  map 
    
ID[' ']=' ';  // for space 
ID['a']='y';
ID['b']='h';
ID['c']='e';
ID['d']='s';
ID['e']='o';
ID['f']='c';
ID['g']='v';
ID['h']='x';
ID['i']='d';
ID['j']='u';
ID['k']='i';
ID['l']='g';
ID['m']='l';
ID['n']='b';
ID['o']='k';
ID['p']='r';
ID['q']='z';
ID['r']='t';
ID['s']='n';
ID['t']='w';
ID['u']='j';
ID['v']='p';
ID['w']='f';
ID['x']='m';
ID['y']='a';
ID['z']='q';




int t,cases=1;

scanf("%d",&t);

while (t--)  {
      char w[101];
scanf(" %[^\n]",w);
printf("Case #%d: ",cases);
for (int i=0;i<strlen(w);i++)
    printf("%c",ID[w[i]]);
printf("\n");
cases++;
}

return 0; 

}


      
