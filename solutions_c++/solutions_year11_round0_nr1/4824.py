
#include<conio.h>
#include<stdio.h>
#include<iostream.h>
#include<alloc.h>
#include<math.h>

int main()
{

clrscr();
FILE *fp1,*fp2;

fp1 = fopen("A-small.in","r");
fp2 = fopen("A-small.out","w");


int tcase;
fscanf(fp1,"%d",&tcase);
 int cs =0;

while(tcase != 0)
{
  tcase--; cs++;
  int nbut=0;
  fscanf(fp1,"%d",&nbut);


  int *num,*time;
  char *c;
  num = (int*)malloc(nbut*sizeof(int));
  c = (char*)malloc(nbut*sizeof(char));
  time = (int*)malloc(nbut*sizeof(int));
  int i=0;
  while(nbut > 0)
  {
	int sp = getc(fp1);
	int m = getc(fp1);
	*(c+i)= char(m);
	getc(fp1);
	fscanf(fp1,"%d",&(*(num+i)));

	i++;
	nbut--;
  }
      // now i has number of elements


    int j=0;
    *(time+0)=*(num+0); j++;

    while(j<i && i>1)
    {

       if (*(c+j) == *(c+j-1))
	{
		int diff = *(num + j-1) - *(num+j);
		*(time+j) = abs(diff) + 1;
		j++;
	}
	else
	{

			int diff = 0;    int k=0;
			for(k=j-1;k>=0;k--)
			{
			if(*(c+j) == *(c+k))
			{
				diff = abs(*(num+j)-*(num+k));
				int tdif =0;
				for(int m=k+1;m<j;m++)
				{
					tdif= tdif + *(time+m);

				}
				if(diff<=tdif)
			      { diff = tdif;
			       *(time +j) = 1; }
			       else
			       *(time + j) = abs(diff-tdif)+1 ;

			       break;
		       }


			} //for inner ends

			if(k == -1)
			{

				diff = *(num+j);
				int tdif =0;
				for(int m=k+1;m<j;m++)
				{
					tdif= tdif + *(time+m);

				}
				if(diff<=tdif)
				{diff = tdif;
				*(time+j)=1;}
				else
				{*(time+j)=abs(diff-tdif);}

			}


		  j++;

		}
	}

  int tot =0;
  for(int m =0;m<i;m++)
  {
	tot = tot + *(time+m);
       //	cout<<*(time+m)<<"\n";
  }


  fprintf(fp2,"Case #%d: %d \n",cs,tot);
}

return 0;

}

