#include <stdio.h>

int v1[900];
int v2[900];

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
	int i, k, n,  T;
	__int64 result;

	__int64 l = 10000000005; 
//printf("%lld\n",l);

	inf = fopen("x_in.txt","r");
	outf = fopen("x_out.txt","w");

	fscanf(inf,"%d", &T);
	for (i=0; i<T; i++)
	{
		
		fscanf(inf,"%d", &n);
		for (k=0;k<n;k++)
			fscanf(inf,"%d", &(v1[k]));
		for (k=0;k<n;k++)
			fscanf(inf,"%d", &(v2[k]));
		quickSort(v1,0,n-1,0);
		quickSort(v2,0,n-1,1);

		result = 0;
		for (k=0;k<n;k++)
			result += v1[k] * v2[k];

		fprintf(outf, "Case #%d: %lld\n", i+1, result);
	}

	fclose(inf);
	fclose(outf);
}