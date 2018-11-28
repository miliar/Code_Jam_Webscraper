#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <vector>
#include <string>
#include <math.h>




using namespace std;

int main()
{
    FILE *_i,*_o;
    int N;
    int ns,nq,c=1,fnd=0,sw=0,br=0;
    string s[100],q[1000];
    
    char *a;
    a=(char *)(malloc(100*sizeof(char)));
    //s=(char **)(calloc(100,100*sizeof(char)));
    //q=(char **)(calloc(1000,100*sizeof(char)));
    
    _i=fopen("al.in","r");
    _o=fopen("save_l.out","w+");
    
      //reading inputs
fscanf(_i,"%d",&N);

for(int k=1;k<=N;k++)
{
c=1;fnd=0;sw=0;br=0;
 fscanf(_i,"%d",&ns); 
 fscanf(_i,"\n");
 for(int i=0;i<ns;i++)
          { fgets(a,101,_i);s[i]=a; }
           
 fscanf(_i,"%d",&nq); 
 fscanf(_i,"\n");
 for(int i=0;i<nq;i++)
           {fgets(a,101,_i); q[i]=a;} 
 
for(int i=1;i<nq;i++){
        fnd=0;
        for(int j=i-1;j>=br;j--)
         if(q[i]==q[j])
            {fnd=1;break;}
            
        if(fnd==0)
           {c++;}
        if(c==ns)
           {sw++;c=1;br=i;}   
   }
 /*  
 int si[100],j;
 for(int i=0;i<ns;i++)si[i]=0; 
 c=0; 
for(int i=1;i<nq;i++){
        
        for( j=0;j<ns;j++)
         if(q[i]==s[j])
         if(sw%2==0)
          if(si[j]==1)
            {break;}
          else
             {si[j]=1;c++;cout<<i<<" "<<c<<endl;break;}
         else
          if(si[j]==0)
            {break;}
          else
             {si[j]=0;c++;break;} 
            
        
        if(c==ns)
           {sw++;c=1;
            if(sw%2==0)
             si[j]=1;
            else
             si[j]=0;
           }   
   }
   */
cout<<"case "<<k<<": "<<sw<<endl;
 
fprintf(_o,"Case #%d: %d",k,sw);
fprintf(_o,"\n");       
            
}

fclose(_o);
fclose(_i);	

free(a);
    
    
    
    
getche();
return 0;
}
