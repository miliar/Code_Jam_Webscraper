#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<assert.h>
#define mode1 "r"
#define mode2 "w"
#define stream1 stdin
#define stream2 stdout
#define file1 "input.txt"
#define file2 "output.txt"
#define space ' '
#define loop(v,n) for(v=0;v<n;v++)
char myhashtable[893];

int main()
{
freopen(file1,mode1,stream1);
freopen(file2,mode2,stream2);
    //creating an hash table for decrypting the message
    myhashtable['y'-0]='a';myhashtable['n'-0]='b';myhashtable['f'-0]='c';myhashtable['i'-0]='d';myhashtable['c'-0]='e';myhashtable['w'-0]='f';myhashtable['l'-0]='g';myhashtable['b'-0]='h';myhashtable['k'-0]='i';myhashtable['u'-0]='j';myhashtable['o'-0]='k';myhashtable['m'-0]='l';myhashtable['x'-0]='m';myhashtable['s'-0]='n';myhashtable['e'-0]='o';myhashtable['v'-0]='p';myhashtable['z'-0]='q';myhashtable['p'-0]='r';myhashtable['d'-0]='s';myhashtable['r'-0]='t';myhashtable['j'-0]='u';myhashtable['g'-0]='v';myhashtable['t'-0]='w';myhashtable['h'-0]='x';myhashtable['a'-0]='y';myhashtable['q'-0]='z';
char mystring[1059];
float hi=3,h1=5,h2,h3;
unsigned  int no_of_test_cases;
unsigned int index=0;
unsigned int maybe,maybe2,maybe3;
unsigned int iter=1;
unsigned int length=0;
h2=hi+h1;
if(h2)
h3=9;

scanf("%u\n",&no_of_test_cases);

    while(iter<=no_of_test_cases)
    {


        gets(mystring);
        printf("Case #%u: ",iter++);
       length=strlen(mystring);
       loop(index,length)
        {
            if(isalpha(mystring[index]))
            {
                mystring[index]=myhashtable[mystring[index]-0];
            }
        putchar(mystring[index]);
}
    putchar('\n');

    }
    return 0;
}
