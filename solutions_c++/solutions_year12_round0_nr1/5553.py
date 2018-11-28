#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct string {
    char s[105];
    };
FILE *fp ; 
struct string a[30];

 



int main(){ 
    
    int fp;
    char in[30],out[30];
        //sprintf(in,"input.txt",fp);
        sprintf(out,"output.txt",fp);
        //freopen(in,"r",stdin);
        freopen(out,"w",stdout);
        
    int t,i,j;
    scanf("%d",&t);
    
    for(i=0;i<t;i++){
        scanf("\n");
        gets(a[i].s);
        
        }
    
    for(i=0;i<t;i++){
        int l = strlen(a[i].s);
        for(j=0;j<l;j++){
            switch(a[i].s[j]){
                case 'a':
                    a[i].s[j] = 'y';
                    break;
                case 'b':
                    a[i].s[j] = 'h';
                    break;
                case 'c':
                    a[i].s[j] = 'e';
                    break;
                case 'd':
                    a[i].s[j] = 's';
                    break;
                case 'e':
                    a[i].s[j] = 'o';
                    break;
                case 'f':
                    a[i].s[j] = 'c';
                    break;
                case 'g':
                    a[i].s[j] = 'v';
                    break;
                case 'h':
                    a[i].s[j] = 'x';
                    break;
                case 'i':
                    a[i].s[j] = 'd';
                    break;
                case 'j':
                    a[i].s[j] = 'u';
                    break;
                case 'k':
                    a[i].s[j] = 'i';
                    break;
                case 'l':
                    a[i].s[j] = 'g';
                    break;
                case 'm':
                    a[i].s[j] = 'l';
                    break;
                case 'n':
                    a[i].s[j] = 'b';
                    break;
                case 'o':
                    a[i].s[j] = 'k';
                    break;
                case 'p':
                    a[i].s[j] = 'r';
                    break;
                case 'q':
                    a[i].s[j] = 'z';
                    break;
                case 'r':
                    a[i].s[j] = 't';
                    break;
                case 's':
                    a[i].s[j] = 'n';
                    break;
                case 't':
                    a[i].s[j] = 'w';
                    break;
                case 'u':
                    a[i].s[j] = 'j';
                    break;
                case 'v':
                    a[i].s[j] = 'p';
                    break;
                case 'w':
                    a[i].s[j] = 'f';
                    break;
                case 'x':
                    a[i].s[j] = 'm';
                    break;
                case 'y':
                    a[i].s[j] = 'a';
                    break;
                case 'z': 
                    a[i].s[j] = 'q';
                    break;   
                default :
                    break;
                }
            }
        printf("Case #%d: %s\n",i+1,a[i].s);
        }
    //system("pause");
    return 0;
    }
