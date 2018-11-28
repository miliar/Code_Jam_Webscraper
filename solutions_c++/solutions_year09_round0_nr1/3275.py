#include<iostream.h>
#include<fstream.h>
#include<string.h>

	int l,d,n,result_number=0;
	int i,j,k,temp_number;
	char* temp;
	char* language;
	char **dict;
	char **anal;
	char *to_cont;
	bool dictflag;

	void contrast(char*);

bool isthere(int ci,char c)		
{
	bool flagcic=0;
	for(int cic=0;cic<d;cic++)
	{
		if(c==dict[cic][ci])
		{
			flagcic=1;
			break;
		}
	}
	return flagcic;
}

bool ishere(char* str,char c)
{
	bool flagcic=0;
	for(int cic=0;cic<strlen(str);cic++)
	{
		if(c==str[cic])
		{
			flagcic=1;
			break;
		}
	}
	return flagcic;
}

void main()
{
	ifstream in("A-small-attempt1.in",ios::nocreate);
	ofstream out("A-small-attempt1.out");
	in>>l;
	in>>d;
	in>>n;

	dict=new char*[d];
	for(i=0;i<d;i++)
	{
		dict[i]=new char[l+1];
		in>>dict[i];
	}

	language=new char[l*(l+2)+1];

	anal=new char*[l];
	for(i=0;i<l;i++)
	{
		anal[i]=new char[l+1];
	}


	for(i=0;i<n;i++)
	{
		in>>language;
		result_number=0;

		//initialize anal[i]
		temp=language;
		for(int anal_num=0;anal_num<l;anal_num++)
		{
			if(*temp=='(')
			{
				temp_number=1;
				char tempcharc;
				int temp_anal_longth=0;
				while(*(temp+temp_number)!=')')
				{
					tempcharc=*(temp+temp_number);
					if(isthere(anal_num,tempcharc))
					{
						anal[anal_num][temp_anal_longth]=tempcharc;
						temp_anal_longth++;
					}
					temp_number++;
				}
				anal[anal_num][temp_anal_longth]='\0';
				temp+=(temp_number+1);
			}
			else
			{
				if(isthere(anal_num,*temp))
				{
					anal[anal_num][0]=*temp;
					anal[anal_num][1]='\0';
				}
				else
				{
					anal[anal_num][0]='\0';
				}
				temp++;
			}
		}


		
		//contrast
		to_cont=new char[l+1];	
		to_cont[l]='\0';

		bool zeroflag=0;
		for(j=0;j<l;j++)
		{
			if(strlen(anal[j])==0)
				zeroflag=1;
		}
		if(zeroflag==0)
		{
			for(j=0;j<d;j++)
			{
				dictflag=1;
				for(k=0;k<l;k++)
				{
					if(ishere(anal[k],dict[j][k])==0)
					{
						dictflag=0;
						break;
					}
				}
				if(dictflag) result_number++;
			}
		}
		
		out<<"Case #"<<(i+1)<<": "<<result_number<<endl;
	}

	in.close();
	out.close();
}