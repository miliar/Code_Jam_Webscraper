#include<stdio.h>
#include<conio.h>
#include<string.h>


void main()
{       FILE *rfp,*wfp;
	int i,j,n;
	char ch[110]={'\0'};
	char ans[26]={"yhesocvxduiglbkrztnwjpfmaq"};


	clrscr();
	rfp = fopen("d:/t1.in","r+");
	wfp = fopen("d:/z.txt","w+");
	fscanf(rfp, "%d",&n);
       //	printf("n==%d\n",n);
       for(i=0;i<n;i++)
	{  fflush(stdin);

	 fscanf(rfp," %[^\n]",&ch);

      fprintf(wfp,"Case #%d: ",i+1);
	 for(j=0;j<strlen(ch);j++)
		{  if(ch[j]==32)
			fprintf(wfp," ");
		   else
		       {	fprintf(wfp,"%c",ans[ch[j]-97]);
		       }
		}
		fprintf(wfp,"\n");

	}

	fclose(wfp);
	fclose(rfp);
}