/* PROGRAM TO FIND THE STATUS OF THE BULB ATTACHED TO THE SNAPPERS*/
   #include<stdio.h>
   #include<conio.h>
   #include<string.h>
   #include<math.h>
   void read();
   void main()
     {
	read();
     }
   void read()
   {
	 FILE *fin,*fou;
	 long nSwap,nSnap,fon,fdiff;
	 int  ncase,cread=0L,status;
	 char *ifilename,*ofilename;
	 printf("\n\nEnter the input filename along with path and extension\n");
	 scanf("%s",ifilename);
	 //ifilename="A-smallat.in";
	 printf("enter the output filename along with path and extension\n");
	 scanf("%s",ofilename);
	 fin=fopen(ifilename,"rt");
	 fou=fopen(ofilename,"wt");

	 if(fin==NULL)
	    printf("Input file is not opening %s",ifilename);
	 else  if(fou==NULL)
	    printf("Output file is not opening");
	 else
	 {
	    fscanf(fin,"%d",&ncase);
	    //printf("%d",ncase);
	    while(cread<ncase)
	    {
	       if(feof(fin))
	       break;
	       fscanf(fin,"%ld%ld",&nSwap,&nSnap);
	       fon=pow(2,nSwap)-1;
	       fdiff=pow(2,nSwap);
	       ++cread;
	       if(((nSnap-fon)%fdiff)==0)
	       {
	       fprintf(fou,"Case #%d: %s \n",cread,"ON");
	       }
	       else
	       {
	       fprintf(fou,"Case #%d: %s \n",cread,"OFF");
	       }
	     }
	 }
	    fclose(fou);
	    fclose(fin);
	    getch();
   }