#include <iostream> 
#include <stdio.h> 
#include <string>
using namespace std;
#define ML 101 //MAXLENGTH

int A,TA,used[ML],change;
string stra[ML];

void panduan (string s)
{
	int i,j;
	for (i=0;i<A;i++)
	{
		if (s==stra[i])
		{
			if (used[i]==0)
			{
				used[i]=1;
				TA--;
				if (TA==0)
				{
				TA=A-1;
				change++;
				for (j=0;j<A;j++)
					used[j]=0;
				used[i]=1;
				}
			}
		
		}
		
	}
            

}

main()
{
	FILE *fp1,*fp2;
	string s,strb[1000];
	char ch,str[ML];
	int totalnumber,No,B;
	int i,j;
	fp1=fopen("A-large.in","r");
    fp2=fopen("output2.txt","w");
    fscanf(fp1,"%d\n",&totalnumber);
	for (No=1;No<=totalnumber;No++)
	{
		fscanf(fp1,"%d\n",&A);
		change=0;TA=A;
		for (i=0;i<A;i++)
		{
			fgets(str,ML,fp1);

	/*		while (ch!='\0')
			{
				str[j]=ch;
				j++;
				fscanf(fp1,"%c",&ch);
				
			}*/


		//	fscanf(fp1,"%s\n",str);
		//	for (j=0;j<ML;j++)
			stra[i]=str;

			used[i]=0;
	/*		for (j=0;j<4;j++)
			{
			fprintf(fp2,"%c",stra[i][j]);
			

			}
	*/		//fprintf(fp2,"\n");
		}
		


		fscanf(fp1,"%d\n",&B);
		for (i=0;i<B;i++)
		{
			fgets(str,ML,fp1);
			strb[i]=str;
		}
		for (i=0;i<B;i++)
		{
			panduan(strb[i]);
			

		}
	
		fprintf(fp2,"Case #%d: %d\n",No,change);

	}

/*		for (i=0;i<B;i++)
		{
			fprintf(fp2,"%c",stra[0][i]);
			

		}*/
	fclose(fp1);
	fclose(fp2);
	


	return 1;
}