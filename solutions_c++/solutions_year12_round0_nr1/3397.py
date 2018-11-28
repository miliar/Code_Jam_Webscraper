#include<stdio.h>
#include<fstream>
int main()
{
	int c;
	int j=0;
	int count=0;
	int t=0;
	char ip_word[101];
	char op_word[101];
	char intro[7]={'C','a','s','e',' ','#','\0'};
	int mapping[26]={25,8,5,19,15,3,22,24,4,21,9,7,12,2,11,18,26,20,14,23,10,16,6,13,1,17};
	FILE*input=fopen("A-small-attempt1.in","r");
	//FILE*input=fopen("input.txt","r");
	FILE*output=fopen("output.txt","w");
	 if (input==NULL) 
		 printf("Error opening file");
	 else
	 {
		 fgets(ip_word,3,input);
		 for(int m=0;m<3;m++)
		 {
			 if(ip_word[m]=='\n'|| ip_word[m]==NULL||ip_word[m]==10)
			 {
				 break;
			 }
			 else
				 count++;
		 }
		 if(count==2)
			 t=(ip_word[0]-48)*10+(ip_word[1]-48);
		 else
			  t=ip_word[0]-48;
		 for(int i=0;i<t;i++)
		 {
			 j=0;
			 fgets(ip_word,101,input);
			 if(ip_word[0]==10)
			 {
				 fgets(ip_word,100,input);
			 }
			 while(ip_word[j]!='\n'&& ip_word[j]!=NULL)
			 {
				 if(ip_word[j]==' ')
				 {
					 op_word[j]=' ';
					 j++;
				 }
				 else
				 {
					 op_word[j]=(char)(mapping[(int)(ip_word[j])-96-1]+96);
					 j++;
				 }
			 }

			 op_word[j]='\0';
			 j++;

			 fputs(intro,output);
			 if(i>=9)
			 {
				 fputc(((i+1)/10)+48,output);
				 fputc(((i+1)%10)+48,output);
				 
			 }
			 else
			 {
				 fputc(i+1+48,output);
			 }
			 fputs(": ",output);
			 fputs(op_word,output);
			 fputc('\n',output);
			 op_word[0]='\0';
			 

		 }

	 }
    fclose (input);
    

}