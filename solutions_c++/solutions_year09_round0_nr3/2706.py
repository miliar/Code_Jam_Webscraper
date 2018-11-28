#include<fstream.h>
#include<string.h>
#include<stdio.h>

void main()
{
	char inpt[50],outpt[50];
	cout<<"Enter input filename : ";
	cin>>inpt;
	cout<<"Enter output file name : ";
	cin>>outpt;
	fstream fin(inpt,ios::in),fout(outpt,ios::out);
	char str[]="welcome to code jam",txt[32];
	int n,j;
	fin>>n;
	fin.getline(txt,5);
	for(j=0;j<n;j++)
 {
  int ptr[19],count=0,i=0,len;
	fin.getline(txt,32);
	len=strlen(txt);
	ptr[0]=0;
	while(1)
	{
		while(txt[ptr[i]]!=str[i]&&ptr[i]<=len-19+i)
			ptr[i]++;
		if(txt[ptr[i]]==str[i])
		{
			if(i==18)
			{
				if(count==9999)
					count=0;
				else
					count++;
			  ptr[18]++;
			}
			else
			{
				i++;
				ptr[i]=ptr[i-1]+1;
			}
	  }
	  else if(!i)
		break;
	  else
		{
			i--;
			ptr[i]++;
		}
	}
	fout<<"Case #"<<j+1<<": ";
	if(count<1000)
	{
		fout<<"0";
		if(count<100)
		{
			fout<<"0";
			if(count<10)
				fout<<"0";
		}
	}
	  fout<<count<<"\n";
}
fin.close();
fout.close();
}
