/*
Vikas.kumar_vkx
:)

*/
#include <iostream>
#include <string.h>
using namespace std;

int main() {

int n=3;
int s=1;
int m=5;
char a[1000];
int count=0;n=6;s=2;m=8;
int tt=0;

    int T; scanf("%d\n",&T);
	while (T--) {tt++;count=0;
//                    scanf("%s",&a);
gets(a);

for(int i=0;i<strlen(a);i++){

if(a[i]=='y')a[i]='a';
else if(a[i]=='n')a[i]='b';
else if(a[i]=='f')a[i]='c';
else if(a[i]=='i')a[i]='d';
else if(a[i]=='c')a[i]='e';
else if(a[i]=='w')a[i]='f';
else if(a[i]=='l')a[i]='g';
else if(a[i]=='b')a[i]='h';
else if(a[i]=='k')a[i]='i';
else if(a[i]=='u')a[i]='j';
else if(a[i]=='o')a[i]='k';
else if(a[i]=='m')a[i]='l';
else if(a[i]=='x')a[i]='m';
else if(a[i]=='s')a[i]='n';
else if(a[i]=='e')a[i]='o';
else if(a[i]=='v')a[i]='p';
else if(a[i]=='z')a[i]='q';
else if(a[i]=='p')a[i]='r';
else if(a[i]=='d')a[i]='s';
else if(a[i]=='r')a[i]='t';
else if(a[i]=='j')a[i]='u';
else if(a[i]=='g')a[i]='v';
else if(a[i]=='t')a[i]='w';
else if(a[i]=='h')a[i]='x';
else if(a[i]=='a')a[i]='y';
else if(a[i]=='q')a[i]='z';

}


                    printf("Case #%d: %s\n",tt,a);

        }                    scanf("%d",&n);
}
