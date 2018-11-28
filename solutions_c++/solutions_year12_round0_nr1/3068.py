#include <iostream>
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n;
    int i,j;
    char go[200];
    scanf("%d",&n);
    n++;
    for(i=0;i<n;i++) {
        gets(go);
        j=0;
        while(go[j]!='\0') {
            if(go[j]=='y') go[j]='a';
            else if(go[j]=='n') go[j]='b';
            else if(go[j]=='f') go[j]='c';
            else if(go[j]=='i') go[j]='d';
            else if(go[j]=='c') go[j]='e';
            else if(go[j]=='w') go[j]='f';
            else if(go[j]=='l') go[j]='g';
            else if(go[j]=='b') go[j]='h';
            else if(go[j]=='k') go[j]='i';
            else if(go[j]=='u') go[j]='j';
            else if(go[j]=='o') go[j]='k';
            else if(go[j]=='m') go[j]='l';
            else if(go[j]=='x') go[j]='m';
            else if(go[j]=='s') go[j]='n';
            else if(go[j]=='e') go[j]='o';
            else if(go[j]=='v') go[j]='p';
            else if(go[j]=='z') go[j]='q';
            else if(go[j]=='p') go[j]='r';
            else if(go[j]=='d') go[j]='s';
            else if(go[j]=='r') go[j]='t';
            else if(go[j]=='j') go[j]='u';
            else if(go[j]=='g') go[j]='v';
            else if(go[j]=='t') go[j]='w';
            else if(go[j]=='h') go[j]='x';
            else if(go[j]=='a') go[j]='y';
            else if(go[j]=='q') go[j]='z';
            j++;
        }
        if(i!=0) printf("Case #%d: %s\n",i,go);
    }
    return 0;
}
