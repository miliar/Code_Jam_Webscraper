#include<stdio.h>

int main(){
    freopen("input.in","r",stdin);
    freopen("output1_lib.txt","w",stdout);
    char table[26];
    table['y'-'a']='a';
    table['n'-'a']='b';
    table['f'-'a']='c';
    table['i'-'a']='d';
    table['c'-'a']='e';
    table['w'-'a']='f';
    table['l'-'a']='g';
    table['b'-'a']='h';
    table['k'-'a']='i';
    table['u'-'a']='j';
    table['o'-'a']='k';
    table['m'-'a']='l';
    table['x'-'a']='m';
    table['s'-'a']='n';
    table['e'-'a']='o';
    table['v'-'a']='p';
    table['z'-'a']='q';
    table['p'-'a']='r';
    table['d'-'a']='s';
    table['r'-'a']='t';
    table['j'-'a']='u';
    table['g'-'a']='v';
    table['t'-'a']='w';
    table['h'-'a']='x';
    table['a'-'a']='y';
    table['q'-'a']='z';
    int n=0;
    scanf("%d" ,&n);
    int i=0;
    char input[200];
    gets(input);
    for(i=0;i<n;i++){
        //scanf("%s",input);
        gets(input);
        printf("Case #%d: ",i+1);
        int j=0;
        while(input[j]!='\0'){
            char c=input[j];
            if(c!=' '){
                printf("%c",table[c-'a']);
            }
            else{
                printf(" ");
            }
            j++;
        }
        printf("\n");
    }
    return 0;
}

