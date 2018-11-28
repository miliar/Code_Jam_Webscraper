#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
   	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
    
    char ch,s[100];
    int d1[100][2],z=0,numT,count=0,steps,l1;
    fscanf(fp,"%s",s);
    numT=atoi(s);
    while(count<numT)
    {
                   fscanf(fp,"%s",s);
                   z=atoi(s);
                   l1=0;
                   while(l1<z)
                   {
                              fscanf(fp,"%s",s);
                              ch=(char)s[0];     
                                
                              if(ch=='o'||ch=='O')
                              {
                                                  d1[l1][0]=1;
                                                  fscanf(fp,"%s",s);
                                                  d1[l1][1]=atoi(s); 
                                                 
                                                      
                              }
                              else if(ch=='b'||ch=='B')
                              {
                                   d1[l1][0]=2;
                                   fscanf(fp,"%s",s);
                                   d1[l1][1]=atoi(s);
                                  
                              }
                              l1++; 
                           
                   }
                  int i=0,j=0,pd1,pd2,x1=1,x2=1;
                  steps=0;
                  while(1)
                  {
                          pd1=0;
                          pd2=0;
                          while(d1[i][0]!=1 && i<l1)
                                            i++;
                          if(i<l1)
                                 pd1=d1[i][1];
 
                          while(d1[j][0]!=2 && j<l1)
                                            j++;
                          if(j<l1)
                                 pd2=d1[j][1];

                          if(pd1==0 && pd2==0)
                                    break;

                          if(i<j || pd2==0)
                          {
                                 if(x1<=pd1)
                                 {
                                            while(x1<pd1)
                                              {
                                                            x1++;
                                                            steps++;
                                                            if(pd2!=0)
                                                            {
                                                                                   if(x2<pd2)
                                                                                         x2++;
                                                                                   else if (x2>pd2)
                                                                                         x2--;
                                                             }
                                              }
                                              steps++;
                                                if(pd2!=0)
                                                  {
                                                             if(x2<pd2)
                                                                        x2++;
                                                             else if (x2>pd2)
                                                               x2--;
                                                   }
                                 }
                                 
                                 else if(x1>pd1)
                                 { 
                                           while(x1>pd1)
                                           {
                                                          x1--;
                                                          steps++;
                                                          if(pd2!=0)
                                                          {
                                                                    if(x2<pd2)
                                                                               x2++;
                                                                    else if(x2>pd2)
                                                                                   x2--;
                                                          }
                                           }
                                           steps++;
                                           if(pd2!=0)
                                           {
                                                     if(x2<pd2)
                                                                x2++;
                                                     else if(x2>pd2)
                                                                    x2--;
                                            }
                                 }
                                 i++;
                          }

                          if(j<i || pd1==0)
                          {
                                 if(x2<=pd2)
                                 {
                                           while(x2<pd2)
                                            {
                                                 x2++;
                                                 steps++;
                                                 if(pd1!=0)
                                                 {
                                                         if(x1<pd1)
                                                                  x1++;
                                                         else if (x1>pd1)
                                                               x1--;
                                                 }
                                             }
                                             steps++;
                                             if(pd1!=0)
                                              {
                                                   if(x1<pd1)
                                                               x1++;
                                                    else if (x1>pd1)
                                                               x1--;
                                               }
                                 }
                                 
                                 else if(x2>pd2)
                                 {
                                         while(x2>pd2)
                                          {
                                               x2--;
                                               steps++;
                                               if(pd1!=0)
                                               {
                                                      if(x1<pd1)
                                                               x1++;
                                                      else if (x1>pd1)
                                                               x1--;
                                                }
                                          }
                                          steps++;
                                          if(pd1!=0)
                                          {
                                               if(x1<pd1)
                                                               x1++;
                                               else if (x1>pd1)
                                                               x1--;
                                          }
                                 }
                                 j++;
                          }                  
                   }
                   fprintf(ofp, "Case #%d: %d",count+1,steps);
                   count++;
                   if(count<numT)
                                 fprintf(ofp,"\n");
    }
    fclose(fp);
    fclose(ofp);
    return 0;
}
