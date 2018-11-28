#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
void main()
{
clrscr();
/*
* input file is stored at the location c:\tc\bin\a-small.in
* output file is stored at the location c:\tc\bin\a-smallo.in
*/
FILE *infile,*outfile;
infile = fopen("c:\\tc\\bin\\A-small1.in","r");
outfile = fopen("c:\\tc\\bin\\A-smallo.in","w");
char temp[40],temp2[40];
temp[0]='\0';
temp2[0]='\0';
int total_cases=0,i=0,j,k,turn=0,trainA=0,NA=0,NB=0,maxtrainA=0,maxtrainB=0,trainB=0,stationA[200][2],stationB[200][2];
for(int aaa=1;!feof(infile);)
{

	if(fgets(temp,40,infile)==NULL)
	break;
//	cout<<"\ni :"<<i;
//	puts(temp);
//	cout<<"\n";
	switch(i){
		 case 0:{
			total_cases=atoi(temp);
			cout<<"\ntotal_cases :"<<total_cases;
			i++;break;
			}
		 case 1:{
			turn=atoi(temp);
			cout<<"\nturnaround time :"<<turn;
			i++;
			break;
			}
		 case 2:{
			cout<<temp;
			strcpy(temp,strpbrk(temp,"0123456789\0"));
		  //	cout<<"\n"<<temp<<"***\n";
			strncpy(temp2,temp,j=(strlen(temp)-strlen(strpbrk(temp," \0"))));
			temp2[j]='\0';
			NA=atoi(temp2);
			cout<<"\nNA :"<<NA;
		 //	getch();exit(0);
		 //	cout<<temp;
			strcpy(temp2,strpbrk(temp," \0"));
			strcpy(temp,strpbrk(temp2,"0123456789\0"));

			strncpy(temp2,temp,j=(strlen(temp)-strlen(strpbrk(temp," \0"))));
			temp2[j]='\0';
			NB=atoi(temp2);
		cout<<"\nNB :"<<NB<<"\n";

			i++;j=0;k=0;
			if(NA!=0)
			break;
			}
		 case 3:{
			if(j<NA)
				{
				cout<<"\nStation A:"<<temp<<"***"<<j<<"\n";
				strcpy(temp,strpbrk(temp,"0123456789\0"));
				stationA[j][1]=-1;
				stationA[j][0]=atoi(strncpy(temp2,temp,2))*60;
				strcpy(temp,strpbrk(temp,":\0"));
				strcpy(temp,strpbrk(temp,"0123456789\0"));
				stationA[j][0]+=atoi(strncpy(temp2,temp,2));
				strcpy(temp,strpbrk(temp," \0"));
				strcpy(temp,strpbrk(temp,"0123456789\0"));
				stationB[j][1]=1;
			       //	cout<<"BBB:"<<temp<<"\n";
				stationB[j][0]=atoi(strncpy(temp2,temp,2))*60;
				strcpy(temp,strpbrk(temp,":\0"));
				strcpy(temp,strpbrk(temp,"0123456789\0"));
				stationB[j][0]+=atoi(strncpy(temp2,temp,2))+turn;
				cout<<"\nStation A:"<<stationA[j][0]<<"     stationB:"<<stationB[j][0];
				j++;
				//////////

				}
			if(j==NA)
				{
				i++;
				k=0;
				if(NB!=0)
				break;
				//cout<<"\n\nOne condition is over     i:"<<i<<"\n\n";
				}
			else break;
			}
		 case 4:{
			cout<<" \n   k:"<<k<<"  NB:"<<NB<<"\n";
			if(k<NB)
				{
				cout<<"\nStation B:"<<temp<<"***"<<"\n";
				strcpy(temp,strpbrk(temp,"0123456789\0"));
				stationB[j+k][1]=-1;
				stationB[j+k][0]=atoi(strncpy(temp2,temp,2))*60;
				strcpy(temp,strpbrk(temp,":\0"));
				strcpy(temp,strpbrk(temp,"0123456789\0"));
				stationB[j+k][0]+=atoi(strncpy(temp2,temp,2));
				strcpy(temp,strpbrk(temp," \0"));
				strcpy(temp,strpbrk(temp,"0123456789\0"));
				stationA[j+k][1]=1;
				//cout<<"BBB:"<<temp<<"\n";
				stationA[j+k][0]=atoi(strncpy(temp2,temp,2))*60;
				strcpy(temp,strpbrk(temp,":\0"));
				strcpy(temp,strpbrk(temp,"0123456789\0"));
				stationA[j+k][0]+=atoi(strncpy(temp2,temp,2))+turn;
				cout<<"\nStation B:"<<stationB[j+k][0]<<"     stationB:"<<stationA[j+k][0];
				k++;//////////
				if(k==NB)
					{
					i++;
					cout<<"\nsecond condition is over\n";
					}
				else break;
				}
			}
		 case 5:{  cout<<"\ncase 5:\n";
			for(i=0;i<NA+NB-1;i++)
				for(j=0;j<NA+NB-1-i;j++)
				{
				    if(stationA[j][0]>stationA[j+1][0])
				    {
				    k=stationA[j][0];
				    stationA[j][0]=stationA[j+1][0];
				    stationA[j+1][0]=k;
				    k=stationA[j][1];
				    stationA[j][1]=stationA[j+1][1];
				    stationA[j+1][1]=k;
				    }
				}
			for(i=0;i<NA+NB-1;i++)
				for(j=0;j<NA+NB-1-i;j++)
				{
				    if(stationB[j][0]>stationB[j+1][0])
				    {
				    k=stationB[j][0];
				    stationB[j][0]=stationB[j+1][0];
				    stationB[j+1][0]=k;
				    k=stationB[j][1];
				    stationB[j][1]=stationB[j+1][1];
				    stationB[j+1][1]=k;
				    }
				}
			for(i=0;i<NA+NB;i++)
				cout<<"\nA    "<<floor(stationA[i][0]/60)<<":"<<stationA[i][0]%60<<"     "<<stationA[i][1];
			for(i=0;i<NA+NB;i++)
				cout<<"\nB  "<<floor(stationB[i][0]/60)<<":"<<stationB[i][0]%60<<"     "<<stationB[i][1];
			trainA=0;trainB=0;maxtrainA=0;maxtrainB=0;
			cout<<"maxtrain A:"<<maxtrainA<<"   maxtrainB:"<<maxtrainB<<"\n";
			for(i=0;i<NA+NB;i++)
				{
				cout<<"maxtrain A:"<<maxtrainA<<"   maxtrainB:"<<maxtrainB<<"\n";
				cout<<"train A:"<<trainA<<"   trainB:"<<trainB<<"\n";
				if(stationA[i][1]<0)
				trainA--;
				else
				trainA++;
				if(stationB[i][1]<0)
				trainB--;
				else
				trainB++;
				if(trainA<maxtrainA &&((i==NA+NB-1)||stationA[i][0]!=stationA[i+1][0]))
				maxtrainA=trainA;
				if(trainB<maxtrainB &&((i==NA+NB-1)||stationB[i][0]!=stationB[i+1][0]))
				maxtrainB=trainB;
				}

			fputs("Case #",outfile);
			fputs(itoa(aaa,temp,10),outfile);
			fputs(": ",outfile);
			fputs(itoa(maxtrainA<0?maxtrainA*(-1):0,temp,10),outfile);
			fputs(" ",outfile);
			fputs(itoa(maxtrainB<0?maxtrainB*(-1):0,temp,10),outfile);
			fputs("\n",outfile);
			aaa++;
			i=1;
			cout<<"maxtrain A:"<<maxtrainA<<"   maxtrainB:"<<maxtrainB<<"\n";
		       //	getch();
			}
		 }
	if(aaa>total_cases)
	break;

}
fclose(infile);
fclose(outfile);
//getch();
}

