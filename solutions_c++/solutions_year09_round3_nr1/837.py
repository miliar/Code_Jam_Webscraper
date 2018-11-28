#include<stdio.h>
#include<string.h>
#include<memory.h>
#include<algorithm>
using namespace std;
char symbol[70];
long long int letter[50];
void solveproblem(int probno){
   int j;
   for(j = 0;j<50;j++)
       letter[j]=0;
    scanf("%s",symbol);
    int len = strlen(symbol);
    int i;
    long long int count=1;
    for(i = 0;i<len;i++){
        if(symbol[i]<= '9' && symbol[i] >='0'){
            if(letter[(symbol[i]-'0')]==0){
                letter[(symbol[i]-'0')]=count;
               // printf("%c %lld\n",symbol[i],count);
                count++;
            }

        }
        else{
             if(letter[(symbol[i]-'a')+10]==0){
                letter[(symbol[i]-'a')+10]=count;
              //  printf("%c %lld %lld\n",symbol[i],count,letter[(symbol[i]-'a')+10]);
                count++;
            }
        }
    }
    if(count ==2 ) count++;
    long long c=0;
    //printf("count = %lld",count);
     for(i = 0;i<len;i++){

            if(symbol[i]<= '9' && symbol[i] >='0'){
                if(letter[(symbol[i]-'0')]==1){
                    c=c*(count-1)+1;
                   // printf("cmae here count = %lld %lld",count,c);
                }
                else if(letter[(symbol[i]-'0')]==2){
                    c=c*(count-1);
                }
                else
                    c=c*(count-1) + letter[(symbol[i]-'0')]-1;

        }
        else{
           // printf("aa  %c %lld %d\n",symbol[i],count,letter[(symbol[i]-'a')+10]);

                 if(letter[(symbol[i]-'a')+10]==1){
                    c=c*(count-1)+1;
                    //printf("cmae here count = %lld %lld",count,c);
                }
                else if(letter[(symbol[i]-'a')+10]==2){
                    c=c*(count-1);
                }
                else
                    c=c*(count-1) + letter[(symbol[i]-'a')+10]-1;
            }

     //   printf("%c %lld\n",symbol[i],c);
     }
     printf("Case #%d: %lld\n",probno,c);

}
int main(){
        int n;
        int i;
        scanf("%d",&n);
        for (i=0;i<n;i++)
                solveproblem(i+1);
        return 0;
}
