#include<iostream>
#include<stdio.h>
#include<conio.h>

using namespace std;

int main()
{FILE *R,*W;
int z,Q,a,b,c,d,n,s,p,t,i,j;
R=fopen("I","r");
W=fopen("out.txt","a");
fscanf(R,"%d",&t);

z=0;
while(z<t)
{z++;
Q=0;
fscanf(R,"%d%d%d",&n,&s,&p);

for(i=0,j=0;i<n;i++)
{ fscanf(R,"%d",&d);

a=d/3;
if(a>=p)
 Q++;

else
 { c=d-a;
   b=c/2;
   if(b>=p)
    Q++;
    else
    {c=c-b;
     if(c>=p)
      Q++;
     else if(s>0 && p>1 && (a==p-1 || b==p-1 || c==p-1))
     { if((3*p-4)<=d)
          Q++; s--; }

     }
 }
}
fprintf(W,"Case #%d: %d\n",z,Q);


}

fclose(W);
fclose(R);
getch();
return 0;
    }
