#include <stdio.h>

int freqs[1005];


void quickSort(int* arr,int startPos, int endPos,int t) 
{ 
    int i,j; 
    int ch; 
    ch=arr[startPos]; 
    i=startPos; 
    j=endPos; 
    if(t==0) 
    { 
        while(i<j) 
        { 
            while(arr[j]>=ch && i<j)--j; 
            arr[i]=arr[j]; 
            while(arr[i]<=ch && i<j)++i; 
            arr[j]=arr[i]; 
        } 
        arr[i]=ch; 
        if(i-1>startPos) quickSort(arr,startPos,i-1,t); 
        if(endPos>i+1) quickSort(arr,i+1,endPos,t); 
    } 
    else 
    { 
        while(i<j) 
        { 
            while(arr[j]<=ch&&i<j) --j; 
            arr[i]=arr[j]; 
            while(arr[i]>=ch&&i<j) ++i; 
            arr[j]=arr[i]; 
        } 
        arr[i]=ch; 
        if(i-1>startPos) quickSort(arr,startPos,i-1,t); 
        if(endPos>i+1) quickSort(arr,i+1,endPos,t); 
    } 
} 


void main()
{
	FILE *inf, *outf;
	int i, k,  T;
	int onekeynum, keynum, ltnum;
	int result;
	int weight;

	inf = fopen("Text_in.txt","r");
	outf = fopen("Text_out.txt","w");

	fscanf(inf,"%d", &T);
	for (i=1; i<=T; i++)
	{
		
		fscanf(inf,"%d%d%d", &onekeynum, &keynum, &ltnum);
		for (k=0;k<ltnum;k++)
			fscanf(inf,"%d", &(freqs[k]));

		quickSort(freqs, 0, ltnum-1,1);

		result = 0;
		weight = 0;
		for (k=0;k<ltnum;k++)
		{
			if (0==(k%keynum))
				weight++;
			result += freqs[k] * weight;
		}
		fprintf(outf, "Case #%d: %d\n", i, result);
	}

	fclose(inf);
	fclose(outf);
}
