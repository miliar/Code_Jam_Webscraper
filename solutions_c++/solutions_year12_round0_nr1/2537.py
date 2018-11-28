#include<iostream>
#include<map>
using namespace std;

int main()
{
    int t,i=0,cnt=1;
    map<char,char>m1;
    char str[105];
    char c[105],ch;
    
    m1['a']='y';
    m1['b']='h';
    m1['c']='e';
    m1['d']='s';
    m1['e']='o';
    m1['f']='c';
    m1['g']='v';
    m1['h']='x';
    m1['i']='d';
    m1['j']='u';
    m1['k']='i';
    m1['l']='g';
    m1['m']='l';
    m1['n']='b';
    m1['o']='k';
    m1['p']='r';
    m1['q']='z';
    m1['r']='t';
    m1['s']='n';
    m1['t']='w';
    m1['u']='j';
    m1['v']='p';
    m1['w']='f';
    m1['x']='m';
    m1['y']='a';
    m1['z']='q';
    
    scanf("%d",&t); 
    getchar();
    while(t--)
    {
        gets(str);
        i=0;
        printf("Case #%d: ",cnt++);
        
        while(str[i]!='\0')
        {   
            if(str[i]==' ')
            {
                c[i]=' '; 
                printf("%c",c[i]);  
                str[i]='\0';          
            }    
            else
            {
                ch=str[i];
                c[i]=m1[ch];    
                printf("%c",c[i]);
                str[i]='\0';
            }  
            i++;         
        }
        printf("\n");
    }   
}
