#include<conio.h>
#include<stdio.h>
int no_of_snaps_required(int);
int ON_OFF_state(int,long int);

int main()

{
long int n,m,snaps,no_of_inputs,i;
char *state;
FILE *in,*out;
in=fopen("a.in","r");
out=fopen("output_file.out","w");
fscanf(in,"%d",&no_of_inputs);
for(i=0;i<no_of_inputs;i++)
{
fscanf(in,"%d %d ",&n,&snaps);
printf("%d %d\n",n,snaps);
m=no_of_snaps_required(n);
printf("\n%d",m);


if(ON_OFF_state(m,snaps))
  state= "ON";
else
state ="OFF";

fprintf(out,"Case #%d: %s\n",i+1,state);
}
fclose(out);
//fcloseall();
getch();

}


int no_of_snaps_required(int m)

{

if(m==1)
  return 1;
  else
  return 2*no_of_snaps_required(m-1) + 1;

  }


int ON_OFF_state(int cycle,long int temp_snaps)

  {
  while(1)
  {
  temp_snaps=temp_snaps-cycle;

   if(temp_snaps==0)
      return 1;
     else if(temp_snaps<0)
         return 0;
      else
         temp_snaps--;
   }
   }





