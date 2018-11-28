#define DIGITS 7
#include <stdio.h>
#include <hash_map.h>
using namespace std;

int main(void)
{
freopen("E:\\A-small-attempt1.in" ,"r",stdin);
freopen("E:\\STUOutput.txt","w",stdout);
int n;
scanf("%d",&n);
//printf("%d\n",n);
hash_map <const char *, int> searchEngines;
for(int i = 0; i< n ; i++)
{
     searchEngines.clear();
     int m;
     scanf("%d",&m);
     //printf("%d\n",m);
     //char ch;
     //scanf("%c",ch);
     char temp1[100];
     gets(temp1);
     for(int j =0; j< m; j++) 
     {
      char temp[100];            
      //scanf("%[^\r^\n]",temp);
      gets(temp);
      //printf("%s -> %d\n",temp,j);
      searchEngines[temp]=j; 
     }
     int q;
     scanf("%d",&q);
     //printf("%d\n",q);
     //int **data = malloc(100 * sizeof(int *));     
     //data[0] = malloc(100 * 1000 * sizeof(int));
     //int **data = (int** )malloc(100 * sizeof(int *));     
     //data[0] = (int* )malloc(100 * 1000 * sizeof(int));
     int data[100][1000];
     for(int j=0; j<100; j++)
         for(int k =0; k< 1000; k++)
             data[j][k] =0;
      gets(temp1);     
     for(int j =0; j< q; j++) 
     { 
      char temp[100];
      //scanf("%[^\n]",temp); 
      gets(temp); 
      //printf("%s --> %d\n",temp,j);   
      data[searchEngines[temp]][j] = 1; 
     }
     //lastMin = 0;
    int lastMin;
      //for(int k=0; k<m;k++, printf("\n"))
        //      for(int j=0; j<q;j++)
          //          printf("%d\t",data[k][j]);
              
     for(int j=1;j<q;j++)
        for(int k =0; k< m;k++)
        {
            if(data[k][j]==1)
            {
                  lastMin = 2000;
                  for(int l=0; l<m;l++)
                      if(l!=k && lastMin> data[l][j-1])
                            lastMin = data[l][j-1];
                 data[k][j] = lastMin+1;
            }
            else
               data[k][j] = data[k][j-1];                
        }
     lastMin = 2000;
     for(int k =0; k<m; k++)
     {
        // printf(" >> %d   %d\n", data[k][q-1], q);
         if(lastMin> data[k][q-1])
              lastMin = data[k][q-1];
      } 
   // for(int k=0; k<m;k++, printf("\n"))
     //         for(int j=0; j<q;j++)
       //             printf("%d\t",data[k][j]);
                     
     printf("Case #%d: %d\n",i+1,lastMin);
     //free(data);
}                

//hash_map <const char *, int> searchString;
//searchString["first"] = 1;
//printf("%d", searchString["first"]);
//searchString.clear();
//scanf("%d",&n);
return 0;

}
