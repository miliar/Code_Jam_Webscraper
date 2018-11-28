#include<fstream.h>
#include<conio.h>


char sword[5000][15];




void main()
{
int inocase,inoletter,inoword,iitrnocase,iitrnoword,icount,iitrstr,iitrnoletter,iflag;
char str[2000];
ifstream in;
ofstream out;
in.open("input.in");
out.open("output.txt");

//clrscr();
in>>inoletter>>inoword>>inocase;
for(iitrnoword=0;iitrnoword<inoword;iitrnoword++)
in>>sword[iitrnoword];
for(iitrnoword=0;iitrnoword<inoword;iitrnoword++)
//cout<<"\n"<<sword[iitrnoword];


for(iitrnocase=1;iitrnocase<=inocase;iitrnocase++)
{
icount=0;
in>>str;

for(iitrnoword=0;iitrnoword<inoword;iitrnoword++)
{
	iitrstr=0;
    for(iitrnoletter=0;iitrnoletter<inoletter;iitrnoletter++)
	{       
	
			if(str[iitrstr]=='(')
			{
				iflag=0;
				iitrstr++;
				while(str[iitrstr]!=')')
				{
				//	cout<<"\n"<<str[iitrstr]<<"=="<<sword[iitrnoword][iitrnoletter]<<"   "<<iflag<<"  "<<iitrnoletter;
					if(str[iitrstr++]==sword[iitrnoword][iitrnoletter])
						iflag=1;
					
					
				
				}	

				iitrstr++;
				if(iflag==0)
					break;

				
			}
			
			else 
			{
				//cout<<"\n"<<str[iitrstr]<<"=="<<sword[iitrnoword][iitrnoletter];
				if(str[iitrstr++]!=sword[iitrnoword][iitrnoletter])
				   break;
			}

		

		
	}
 
	if(iitrnoletter==inoletter)
        icount++;


}
//cout<<"\n"<<str;
cout<<"Case #"<<iitrnocase<<": "<<icount<<"\n";
out<<"Case #"<<iitrnocase<<": "<<icount<<"\n";

}
getch();

out.close();
in.close();
getch();
}