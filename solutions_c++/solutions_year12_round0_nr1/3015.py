#include <stdio.h>


int main() {
    freopen("v.txt","r",stdin);
    freopen("o1.txt","w",stdout);
    int t,len,c,i;
    char a[105],x[10];
    scanf("%d",&t);
    gets(x);
    c=1;
    while(t--)
    {
        len=0;
        gets(a);
        for(len=0;a[len]!='\0';++len);

        for(i=0;i<len;++i)
        {
            switch(a[i]){
                case 'a' : a[i]='y';
                    break;
            case 'b' : a[i]='h';
                    break;
case 'c' : a[i]='e';
                    break;
case 'd' : a[i]='s';
                    break;
case 'e' : a[i]='o';
                    break;
case 'f' : a[i]='c';
                    break;
case 'g' : a[i]='v';
                    break;
case 'h' : a[i]='x';
                    break;
case 'i' : a[i]='d';
                    break;
case 'j' : a[i]='u';
                    break;
case 'k' : a[i]='i';
                    break;
case 'l' : a[i]='g';
                    break;
case 'm' : a[i]='l';
                    break;
case 'n' : a[i]='b';
                    break;
case 'o' : a[i]='k';
                    break;
case 'p' : a[i]='r';
                    break;
case 'q' : a[i]='z';
                    break;
case 'r' : a[i]='t';
                    break;
case 's' : a[i]='n';
                    break;
case 't' : a[i]='w';
                    break;
case 'u' : a[i]='j';
                    break;
case 'v' : a[i]='p';
                    break;
case 'w' : a[i]='f';
                    break;
case 'x' : a[i]='m';
                    break;
case 'y' : a[i]='a';
                    break;
case 'z' : a[i]='q';
                    break;
default:
break;

            }
        }
         printf("Case #%d: %s\n",c++,a);



    }
    return 0;
}
