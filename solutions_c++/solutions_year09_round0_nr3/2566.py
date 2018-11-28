#include<iostream>
#include<string>
#include<iomanip>
using namespace std;

int main()
{
	char cad[31];
	string test = "welcome to code jam";
	char ca2[]="                   ";
	char ca3[]="welcome to code jam";
	int i[19],fin,N,j,cuenta,ini,wya,cnt;
	char tmp[2];
	ini=0;
	tmp[1]='\0';
	cin>>N;
tmp[0]=cin.get();
for(j=0;j<N;j++)
{
cuenta=0;
fin=0;
wya=0;
cnt=0;
while((tmp[0]=cin.get())!='\n' && cnt<30)
{
	if(test.find(tmp)!=string::npos)
	{
		if(tmp[0]=='w')
			wya=1;
		if(wya)
		{
		   cad[fin] = tmp[0];
		   fin++;
		}
	}
	cnt++;
}
cad[fin] = '\0';
   
	for(i[0]=ini;i[0]<fin-18;i[0]++)
	{
	  ca2[0] = cad[i[0]];
	  for(i[1]=i[0]+1;i[1]<fin-17;i[1]++)
	  {
		  ca2[1] = cad[i[1]];
	     for(i[2]=i[1]+1;i[2]<fin-16;i[2]++)
		 {
			 ca2[2] = cad[i[2]];
	        for(i[3]=i[2]+1;i[3]<fin-15;i[3]++)
			{
				ca2[3] = cad[i[3]];
				for(i[4]=i[3]+1;i[4]<fin-14;i[4]++)
				{
					ca2[4] = cad[i[4]];
				   for(i[5]=i[4]+1;i[5]<fin-13;i[5]++)
				   {
					   ca2[5] = cad[i[5]];
				      for(i[6]=i[5]+1;i[6]<fin-12;i[6]++)
					  {
						  ca2[6] = cad[i[6]];
					     for(i[7]=i[6]+1;i[7]<fin-11;i[7]++)
						 {
							 ca2[7] = cad[i[7]];
						    for(i[8]=i[7]+1;i[8]<fin-10;i[8]++)
							{
								ca2[8] = cad[i[8]];
							   for(i[9]=i[8]+1;i[9]<fin-9;i[9]++)
							   {
								   ca2[9] = cad[i[9]];
							      for(i[10]=i[9]+1;i[10]<fin-8;i[10]++)
								  {
									  ca2[10] = cad[i[10]];
								     for(i[11]=i[10]+1;i[11]<fin-7;i[11]++)
									 {
										 ca2[11] = cad[i[11]];
										for(i[12]=i[11]+1;i[12]<fin-6;i[12]++)
										{
											ca2[12] = cad[i[12]];
										   for(i[13]=i[12]+1;i[13]<fin-5;i[13]++)
										   {
											   ca2[13] = cad[i[13]];
										      for(i[14]=i[13]+1;i[14]<fin-4;i[14]++)
											  {
												  ca2[14] = cad[i[14]];
											     for(i[15]=i[14]+1;i[15]<fin-3;i[15]++)
												 {
													 ca2[15] = cad[i[15]];
												    for(i[16]=i[15]+1;i[16]<fin-2;i[16]++)
													{
														ca2[16] = cad[i[16]];
													   for(i[17]=i[16]+1;i[17]<fin-1;i[17]++)
													   {
														   ca2[17] = cad[i[17]];
													      for(i[18]=i[17]+1;i[18]<fin;i[18]++)
														  {
ca2[18] = cad[i[18]];
if(strcmp(ca2,ca3)==0)
{
   cuenta++;
}
if(cuenta>9999)
   cuenta=0;
														  }
													   }
													}
												 }
											  }
										   }
										}
									 }
								  }
							   }
							}
						 }
					  }
				   }
				}
			}
		 }
	  } 
	}
	cout<<"Case #"<<j+1<<": "<<setw(4)<<setfill('0')<<cuenta<<endl;
}
	return 0;
}