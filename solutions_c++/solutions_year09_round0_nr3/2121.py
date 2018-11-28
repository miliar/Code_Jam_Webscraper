#include <iostream>
#include <cstdio>
#include <conio.h>
using namespace std;




int main (void)
	{
	int N,i,j,m[80],OK,l,x, Lref,count,stop,k,Lsmall,contatore,migliaia,centinaia,decine,unita;
	char str[80],newstr[80];
	const char ref[20]="welcome to code jam";
	Lref=strlen(ref);
//	for(x=0;x<19;x++)
//		cout << "ref[" << x<< "]= " << ref[x] << "\n";

	cin >> N;
	//N=1;
	gets(str);
	for(x=1;x<=N;x++){
	gets(str);
	l=strlen(str);
//	cout << "Lref="<<Lref<<"l="<<l;
//	cout << "Case #" << x << ": " << str << "\n";
//		for(i=0;i<l;i++)
//		cout << "str[" << i << "] = " << str[i] << "\n";

		count=0;
		stop=1;
		for(i=0;stop;i++)
			if(str[i]==ref[0])
				stop=0;
		i--;
		for(;i<l;i++){
			OK=0;
			for(j=0;j<Lref;j++)
				{
				if(str[i]==ref[j]) {OK=1;
//				cout <<"\n"<<str[i]<<" "<<ref[j]<< " "<<OK;
					}
				}
				if(OK==1){
					newstr[count]=str[i];
					count++;
					}
			}
		
//		for(i=0;i<count;i++) cout << newstr[i];
		Lsmall=count;


		contatore=0;
		for(m[0]=0;m[0]<Lsmall;m[0]++)
			if(newstr[m[0]]==ref[0])

		for(m[1]=m[0]+1;m[1]<Lsmall;m[1]++)
			if(newstr[m[1]]==ref[1])

		for(m[2]=m[1]+1;m[2]<Lsmall;m[2]++)
			if(newstr[m[2]]==ref[2])

		for(m[3]=m[2]+1;m[3]<Lsmall;m[3]++)
			if(newstr[m[3]]==ref[3])

		for(m[4]=m[3]+1;m[4]<Lsmall;m[4]++)
			if(newstr[m[4]]==ref[4])

		for(m[5]=m[4]+1;m[5]<Lsmall;m[5]++)
			if(newstr[m[5]]==ref[5])

		for(m[6]=m[5]+1;m[6]<Lsmall;m[6]++)
			if(newstr[m[6]]==ref[6])

		for(m[7]=m[6]+1;m[7]<Lsmall;m[7]++)
			if(newstr[m[7]]==ref[7])

		for(m[8]=m[7]+1;m[8]<Lsmall;m[8]++)
			if(newstr[m[8]]==ref[8])

		for(m[9]=m[8]+1;m[9]<Lsmall;m[9]++)
			if(newstr[m[9]]==ref[9])

		for(m[10]=m[9]+1;m[10]<Lsmall;m[10]++)
			if(newstr[m[10]]==ref[10])

		for(m[11]=m[10]+1;m[11]<Lsmall;m[11]++)
			if(newstr[m[11]]==ref[11])

		for(m[12]=m[11]+1;m[12]<Lsmall;m[12]++)
			if(newstr[m[12]]==ref[12])

		for(m[13]=m[12]+1;m[13]<Lsmall;m[13]++)
			if(newstr[m[13]]==ref[13])

		for(m[14]=m[13]+1;m[14]<Lsmall;m[14]++)
			if(newstr[m[14]]==ref[14])

		for(m[15]=m[14]+1;m[15]<Lsmall;m[15]++)
			if(newstr[m[15]]==ref[15])

		for(m[16]=m[15]+1;m[16]<Lsmall;m[16]++)
			if(newstr[m[16]]==ref[16])

		for(m[17]=m[16]+1;m[17]<Lsmall;m[17]++)
			if(newstr[m[17]]==ref[17])

		for(m[18]=m[17]+1;m[18]<Lsmall;m[18]++)
			if(newstr[m[18]]==ref[18])

			{
				contatore++;
				if(contatore>10000)
					contatore=contatore-10000;
			}
			
	migliaia=contatore/1000;
	centinaia=(contatore-migliaia*1000)/100;
	decine=(contatore-migliaia*1000-centinaia*100)/10;
	unita=contatore%10;
//	cout << "m"<<migliaia<<"c"<<centinaia<<"d"<<decine<<"u"<<unita;


	cout << "Case #" << x << ": " << migliaia<<centinaia<<decine<<unita << "\n";
//	getch();
		}
	}