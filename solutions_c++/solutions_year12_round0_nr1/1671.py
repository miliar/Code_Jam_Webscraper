#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(void)
{
    int n,i,count;
    char c[101],t;
    FILE *fp1,*fp2;
    if((fp1=fopen("A-small-attempt2.in","r"))==NULL)exit(0);
    if((fp2=fopen("A-small-attempt2.out","w"))==NULL)exit(0);
    fscanf(fp1,"%d",&n);
    fscanf(fp1,"%c",&t);
    for(count=1;count<=n;count++)
    {
         fgets(c,200,fp1);
         fprintf(fp2,"Case #%d: ",count);
         for(i=0;c[i]!='\0';i++)
         {
             
             switch(c[i])
             {
                    case 'a':fprintf(fp2,"y",t);break;
                    case 'b':fprintf(fp2,"h",t);break;
                    case 'c':fprintf(fp2,"e",t);break;
                    case 'd':fprintf(fp2,"s",t);break;
                    case 'e':fprintf(fp2,"o",t);break;
                    case 'f':fprintf(fp2,"c",t);break;
                    case 'g':fprintf(fp2,"v",t);break;
                    case 'h':fprintf(fp2,"x",t);break;
                    case 'i':fprintf(fp2,"d",t);break;
                    case 'j':fprintf(fp2,"u",t);break;
                    case 'k':fprintf(fp2,"i",t);break;
                    case 'l':fprintf(fp2,"g",t);break;
                    case 'm':fprintf(fp2,"l",t);break;
                    case 'n':fprintf(fp2,"b",t);break;
                    case 'o':fprintf(fp2,"k",t);break;
                    case 'p':fprintf(fp2,"r",t);break;
                    case 'q':fprintf(fp2,"z",t);break;
                    case 'r':fprintf(fp2,"t",t);break;
                    case 's':fprintf(fp2,"n",t);break;
                    case 't':fprintf(fp2,"w",t);break;
                    case 'u':fprintf(fp2,"j",t);break;
                    case 'v':fprintf(fp2,"p",t);break;
                    case 'w':fprintf(fp2,"f",t);break;
                    case 'x':fprintf(fp2,"m",t);break;
                    case 'y':fprintf(fp2,"a",t);break;
                    case 'z':fprintf(fp2,"q",t);break;
                    case ' ':fprintf(fp2," ",t);break;
             }
         }
         fprintf(fp2,"\n",t);
    }
    fclose(fp2);
    fclose(fp1);
    return 0;
}
