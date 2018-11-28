#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
 FILE *in,*out;
  in= fopen("in.in","r");
  out=fopen("out.out","w");
  int i,j,t,k,w,d;
  int a[5][5],b[5],c[5];
  char x[10],r;
  
  //cout<<"D";
  
  fscanf(in,"%d",&t);
  k=0;
  while(k<t){k++;
             d=0;    
             for(i=0;i<4;i++)
             {b[i]=1;c[i]=1;}
             for(i=0;i<4;i++){fscanf(in,"%s",x);
                              for(j=0;j<4;j++){
                              r=x[j];
                              
                                      if(r=='X')
                                      {a[i][j]=2;}
                                      else if(r=='O')
                                      {a[i][j]=-1;}
                                      else if(r=='.')
                                      {d=1;a[i][j]=0;}
                                      else if(r=='T')
                                      {a[i][j]=1;}    
                                      b[i]*=a[i][j];
                                      c[j]*=a[i][j];
                                      }}
  /*           for(i=0;i<4;i++){for(j=0;j<4;j++){cout<<a[i][j]<<" ";}cout<<endl;}
cout<<endl;
for(i=0;i<4;i++)
cout<<b[i]<<" "; cout<<endl;
for(i=0;i<4;i++)
cout<<c[i]<<" ";
cin>>i;
              cout<<"e";
         */                             
             w=0;                                    
             for(i=0;i<4;i++)
             {  if(b[i]>5 || c[i]>5 )
                {w=2;break;}
                if(b[i]==1 || b[i]==-1 || c[i]==-1 || c[i] == 1)
                {w=1;break;}
             }
             if(w==0)
             {i=a[0][0] * a[1][1] * a[2][2] * a[3][3];
              j=a[0][3] * a[1][2] * a[2][1] * a[3][0];
              if(i>5 || j>5)
              {w=2;}
              else if( i==1||i==-1||j==1||j==-1)
              {w=1;}
             }
             if(w==0)
             {  if(d==0)
                {fprintf(out,"Case #%d: Draw\n",k);
                }
                else
                fprintf(out,"Case #%d: Game has not completed\n",k);
             }
             else if(w==1)
             fprintf(out,"Case #%d: O won\n",k);
             else
             fprintf(out,"Case #%d: X won\n",k);
             
  }        
     
    
return 0;}
