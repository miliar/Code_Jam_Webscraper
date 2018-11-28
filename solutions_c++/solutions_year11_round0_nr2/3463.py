#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char isInCo(char a[][3],int len,char c1,char c2);
int isInOpp(char a[][2],int len,char c1,char c2);
void del(char *a,int len,int k,int num);

int main()
{
   	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
    
    char s[20];
    int numT,count=0;
    fscanf(fp,"%s",s);
    numT=atoi(s);

    while(count<numT)
    {
                int numCo,numOpp,numSp,i,j,k;
                char co[37][3],opp[29][2],sp[101],ch;
                fscanf(fp,"%s",s);
                numCo=atoi(s);          
                i=0;                          
                while(i<numCo) 
                {
                               fscanf(fp,"%s",co[i]);
                               i++;
                }
                fscanf(fp,"%s",s);
                numOpp=atoi(s);                                    
                i=0;
                while(i<numOpp) 
                {
                               fscanf(fp,"%s",opp[i]);
                               i++;
                }
                fscanf(fp,"%s",s);
                numSp=atoi(s);
                fscanf(fp,"%s",sp);                   
                
                k=1;
                i=0;
                j=0;
                while(k<numSp)                       
                {
                               j=k;
                               while(j>0 && numCo!=0)
                               {                                         
                                         ch=isInCo(co,numCo,sp[j],sp[j-1]);
                                         if(ch!='0')
                                         {
                                                      sp[j-1]=ch;                                                      
                                                      del(sp,numSp,j,1); // deletes starting from j
                                                      numSp--;
                                                      k--;
                                                      if(j+1<numSp)
                                                                 j++;
                                         }
                                         j--;
                               }
                               j=0;
                               while(j<k && numOpp!=0)
                               {
                                          for(i=j+1;i<=k;i++)
                                          {
                                                   if(isInOpp(opp,numOpp,sp[i],sp[j]))
                                                   {
                                                                      del(sp,numSp,0,i+1);
                                                                      k=0;
                                                                      numSp=numSp-i-1;                                                        
                                                   }
                                          }
                                          j++;
                               }
                               k++;
                }
                fprintf(ofp, "Case #%d: [",count+1);
                for(i=0;i<numSp;i++)
                {
                                    fprintf(ofp,"%c",sp[i]);
                                    if(i!=numSp-1)
                                                fprintf(ofp,", ");
                }
                fprintf(ofp,"]");
                count++;
                if(count<numT)
                              fprintf(ofp,"\n");
    }
    fclose(fp);
    fclose(ofp);
    return 0;
}

char isInCo(char a[][3],int len,char c1,char c2)
{
     int i=0;
     while(i<len)
     {
                 if(a[i][0]==c1 && a[i][1]==c2)
                                               return a[i][2];
                 else if(a[i][1]==c1 && a[i][0]==c2)
                                               return a[i][2];
                 i++;
     }
     return '0';                                          
}

int isInOpp(char a[][2],int len,char c1,char c2)
{
     int i=0;
     while(i<len)
     {
                 if(a[i][0]==c1 && a[i][1]==c2)
                                               return 1;
                 else if(a[i][1]==c1 && a[i][0]==c2)
                                                    return 1;
                 i++;
     }
     return 0;
}
                                                    
void del(char *a,int len,int k,int num)
{
     int i=k;
     while(i<len-num)
     {
                     a[i]=a[i+num];
                     i++;
     }
}
