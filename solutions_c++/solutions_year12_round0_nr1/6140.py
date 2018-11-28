#include <stdio.h>
void traslation(char a[],int z);
main()
{
int i;
char vec[99999],c;
scanf("%d",&i);
scanf("%c",&c);
for(int j=0;j<i;j++){
//scanf("%c",&c);
gets(vec);
//scanf("%c",&c);
traslation(vec,j+1);
}
//printf("%s\n",vec);

return 0;
}
void traslation(char a[],int z)
{
int i;
printf("Case #%d: ",z);
char c;
for(i=0;a[i]!='\0';i++){
c=a[i];
/*printf("c");
printf("\n");*/
switch(c)
{
case 'a':printf("y");break;
case 'b':printf("h");break;
case 'c':printf("e");break;
case 'd':printf("s");break;
case 'e':printf("o");break;
case 'f':printf("c");break;
case 'g':printf("v");break;
case 'h':printf("x");break;
case 'i':printf("d");break;
case 'j':printf("u");break;
case 'k':printf("i");break;
case 'l':printf("g");break;
case 'm':printf("l");break;
case 'n':printf("b");break;
case 'o':printf("k");break;
case 'p':printf("r");break;
case 'q':printf("z");break;
case 'r':printf("t");break;
case 's':printf("n");break;
case 't':printf("w");break;
case 'u':printf("j");break;
case 'v':printf("p");break;
case 'w':printf("f");break;
case 'x':printf("m");break;
case 'y':printf("a");break;
case 'z':printf("q");break;
case ' ':printf(" ");break;
}
}
printf("\n");
}
