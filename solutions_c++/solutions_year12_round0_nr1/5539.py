#include<stdio.h>   
#include<stdlib.h> 
int main(void){   
    char* str=(char*)malloc(200*sizeof(char));
    int i,j,t;
    scanf("%d",&t);
    fflush(stdin);
    //FILE * p;
     //p = fopen ("C:\\myfile.txt","w");
    for(j=0;j<t;j++){
        i=0;
        do{
            str[i]=getchar();
            i++;
            if(str[i-1]=='a') str[i-1]='y';
            else if(str[i-1]=='b') str[i-1]='h';
            else if(str[i-1]=='c') str[i-1]='e';
            else if(str[i-1]=='d') str[i-1]='s';
            else if(str[i-1]=='e') str[i-1]='o';
            else if(str[i-1]=='f') str[i-1]='c';
            else if(str[i-1]=='g') str[i-1]='v';
            else if(str[i-1]=='h') str[i-1]='x';
            else if(str[i-1]=='i') str[i-1]='d';
            else if(str[i-1]=='j') str[i-1]='u';
            else if(str[i-1]=='k') str[i-1]='i';
            else if(str[i-1]=='l') str[i-1]='g';
            else if(str[i-1]=='m') str[i-1]='l';
            else if(str[i-1]=='n') str[i-1]='b';
            else if(str[i-1]=='o') str[i-1]='k';
            else if(str[i-1]=='p') str[i-1]='r';
            else if(str[i-1]=='r') str[i-1]='t';
            else if(str[i-1]=='s') str[i-1]='n';
            else if(str[i-1]=='t') str[i-1]='w';
            else if(str[i-1]=='u') str[i-1]='j';
            else if(str[i-1]=='v') str[i-1]='p';
            else if(str[i-1]=='w') str[i-1]='f';
            else if(str[i-1]=='x') str[i-1]='m';
            else if(str[i-1]=='y') str[i-1]='a';
            else if(str[i-1]=='q') str[i-1]='z';
            else if(str[i-1]=='z') str[i-1]='q';
        }while (str[i-1]!= '\n' && i<200);
        str[i-1]='\0';
        //fprintf(p,"Case #%d: %s\n",j+1,str);     
        printf("Case #%d: %s\n",j+1,str); 
    }
    //fclose(p);
    //system("pause");
    return 0;
}

