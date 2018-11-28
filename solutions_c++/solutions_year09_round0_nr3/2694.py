#include<iostream.h>
#include<fstream.h>
#include<string.h>

char s[20]="welcome to code jam";
int result_number;

int isthere(char ch, char* str)
{
	for(int i=0;i<strlen(str);i++)
		if(str[i]==ch)
			return (i+1);
	return 0;
}

void find(char *str,int now)
{
	if(now==19)
	{
		result_number++;
		if(result_number>9999)
			result_number%=10000;
		return;
	}

	if(*str=='\0')
	{
		return;
	}

	for(int i=0;i<strlen(str);i++)
	{
		if(str[i]==s[now])
			find(str+i+1,now+1);
	}
}


void main()
{
	int i,j,k,num=0;
	int now;
	char *text,*temp;
	ifstream in("C-small-attempt1.in",ios::nocreate);
	ofstream out("C-small-attempt1.out");
	in>>num;
	in.get();
	text=new char[501];



	for(i=0;i<num;i++)
	{
		result_number=0;
		in.getline(text,501);
//		cout<<text<<endl;

		for(temp=text;*temp!='\0';)
		{
			if(!isthere(*temp,s))
			{
				for(j=0;j<strlen(temp)+1;j++)
					temp[j]=temp[j+1];
				continue;
			}
			temp++;
		}

		for(j=0;text[j]!='\0'&&text[j]!='w';j++);
		if(text[j]=='w')
		{
			int value=strlen(text);
			for(k=0;k<value-j+1;k++)
				text[k]=text[k+j];
		}
		else if(text[j]=='\0')
			text[0]='\0';

		find(text,0);

		result_number%=10000;
		//out
		out<<"Case #"<<(i+1)<<": ";
		if(result_number)
		{
			for(int ifinal=result_number;ifinal<1000;ifinal*=10)
			{
				out<<'0';
			}
		}
		else
		{
			out<<"000";
		}
		out<<result_number<<endl;
	}
	in.close();
	out.close();
}
