#include<stdio.h>
#include<stdlib.h>

void convert(char line[])
{
     int conversion_table[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
          
     for(int k=0; k<102; k++)
     {
             if(line[k]=='\0') break;
             if(line[k]==' ') continue;
             line[k]=conversion_table[line[k]-'a'];
     }
     
}

int main()
{
    FILE* input=fopen("input.in","r");
    FILE* output=fopen("output.out","w");
    
    int nLines;
    fscanf(input,"%d",&nLines) ;
    
    char line[102];
   // fprintf(output,"%d",nLines);
    fgets(line,101,input);
    for(int k=0; k<nLines; k++)
    {       
            fgets(line,102,input);
            if(line[0]=='\0'){ nLines--; k--; continue;}
            //fprintf(output,"%s",line);
            convert(line);
            fprintf(output,"Case #%d: ",k+1);
            fprintf(output,"%s\n",line);
            
    }
    fclose(input);
    fclose(output);
   // system("PAUSE");
    return 0;
}    
