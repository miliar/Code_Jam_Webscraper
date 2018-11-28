#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
	char c[27]={"yhesocvxduiglbkrztnwjpfmaq"};
	char str[101];
	char a;
	FILE *fp1,*fp2;
	int n,i,j=1;
	fp1=fopen("A-small-attempt0.in","r");
	fp2=fopen("A-small-attempt0.out","w");
	fscanf(fp1,"%d",&n);
	fgetc(fp1);
	while(n--)
	{
	a=fgetc(fp1);
	for(i=0;a!='\n';i++)
	{
		str[i]=a;
		a=fgetc(fp1);
	}
	str[i]='\0';
	cout<<str<<endl;
	for(i=0;str[i]!='\0';i++)
	{
		switch((int)(str[i]-'a'))
		{
		case 0:str[i]=c[0];break;
		case 1:str[i]=c[1];break;
		case 2:str[i]=c[2];break;
		case 3:str[i]=c[3];break;
		case 4:str[i]=c[4];break;
		case 5:str[i]=c[5];break;
		case 6:str[i]=c[6];break;
		case 7:str[i]=c[7];break;
		case 8:str[i]=c[8];break;
		case 9:str[i]=c[9];break;
		case 10:str[i]=c[10];break;
		case 11:str[i]=c[11];break;
		case 12:str[i]=c[12];break;
		case 13:str[i]=c[13];break;
		case 14:str[i]=c[14];break;
		case 15:str[i]=c[15];break;
		case 16:str[i]=c[16];break;
		case 17:str[i]=c[17];break;
		case 18:str[i]=c[18];break;
		case 19:str[i]=c[19];break;
		case 20:str[i]=c[20];break;
		case 21:str[i]=c[21];break;
		case 22:str[i]=c[22];break;
		case 23:str[i]=c[23];break;
		case 24:str[i]=c[24];break;
		case 25:str[i]=c[25];break;
		default:str[i]=' ';
		}
	}
	fprintf(fp2,"Case #%d: %s\n",j++,str);
	}
	return 0;
}
