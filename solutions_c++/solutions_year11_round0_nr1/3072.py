#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;



int b,o;
int posb,poso;

int main(){
    int t;
    int n;
    int z=1;
    scanf("%d",&t);
    FILE *p = fopen("A.txt","w");
    
    
    while(t--)
    {
    int time=0;
    scanf("%d",&n);
    getchar();
    b=o=0;
    posb=1;poso=1;
    int a; char c;
    for(int i=0;i<n;i++)
    {
        scanf("%c %d",&c,&a);  
        if(i<n-1)getchar();
        if(c=='B')
        {
            
           time+=(abs(posb-a)-b>0)?abs(posb-a)-b+1:1;
           o+=(abs(posb-a)-b>0)?abs(posb-a)-b+1:1;   
           posb=a;
           b=0;
           //printf("%dtime\n",time);
        }     
        else if(c=='O')
        {
            
            time+=(abs(poso-a)-o>0)?abs(poso-a)-o+1:1;
            b+=(abs(poso-a)-o>0)?abs(poso-a)-o+1:1; 
            poso=a;
            o=0;
            //printf("%dtimeo\n",time);
        }  
        //
    }      
    
    fprintf(p,"Case #%d: %d\n",z++,time);    
              
    }
    
    
    
    
    
    return 0;
    }
