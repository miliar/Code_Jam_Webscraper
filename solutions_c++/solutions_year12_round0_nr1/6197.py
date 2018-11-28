#include<iostream>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("naseefa.txt","w",stdout);
    char a[10000];
    long t,b,c,d,i,j,k,l;
    cin>>t;
    getchar();
    for(i=0;i<t;i++)
    {
    gets(a);
    l=strlen(a);
    printf("Case #%ld: ",i+1);
    for(j=0;j<l;j++)
    {
                    if(a[j]=='a')
                    printf("y");
                    else if(a[j]=='b')
                    printf("h");
                    else if(a[j]=='c')
                    printf("e");
                    else if(a[j]=='d')
                    printf("s");
                    else if(a[j]=='e')
                    printf("o");
                    else if(a[j]=='f')
                    printf("c");
                    else if(a[j]=='g')
                    printf("v");
                    else if(a[j]=='h')
                    printf("x");
                    else if(a[j]=='i')
                    printf("d");
                    else if(a[j]=='j')
                    printf("u");
                    else if(a[j]=='k')
                    printf("i");
                    else if(a[j]=='l')
                    printf("g");
                    else if(a[j]=='m')
                    printf("l");
                    else if(a[j]=='n')
                    printf("b");
                    else if(a[j]=='o')
                    printf("k");
                    else if(a[j]=='p')
                    printf("r");
                    else if(a[j]=='q')
                    printf("z");
                    else if(a[j]=='r')
                    printf("t");
                    else if(a[j]=='s')
                    printf("n");
                    else if(a[j]=='t')
                    printf("w");
                    else if(a[j]=='u')
                    printf("j");
                    else if(a[j]=='v')
                    printf("p");
                    else if(a[j]=='w')
                    printf("f");
                    else if(a[j]=='x')
                    printf("m");
                    else if(a[j]=='y')
                    printf("a");
                    else if(a[j]=='z')
                    printf("q");
                    else if(a[j]==' ')
                    printf(" ");
    }
    cout<<endl;
    }
    return 0;
}
