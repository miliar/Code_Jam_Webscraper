#include <fstream>
#include <iostream>
using namespace std;

int l,d,n;
char exist[5000][16];
char testchar[15][26];
bool testcharbool[15][26]={0};
int testcharno[15];
int Pos[15];
int current,last;

int mystrcmp(char *sstr1,char *sstr2,int checknum)
{
	char str1[20],str2[20];
	strcpy(str1,sstr1);
	strcpy(str2,sstr2);
	str1[checknum]=0;
	str2[checknum]=0;
	return strcmp(str1,str2);
}

bool isAllowed(char *tocheck,int checknum=15)
{
	/*
	for(int i=0;i<d;i++)
	{
		if(strcmp(exist[i],tocheck)==0)
		{
			return true;
		}
	}
	return false;
	*/
	int low=0,high=d-1;
	int mid;
	while(low<=high)
	{
		mid=(low+high)/2;
		if(mystrcmp(exist[mid],tocheck,checknum)<0)
		{
			low=mid+1;
		}
		else if(mystrcmp(exist[mid],tocheck,checknum)>0)
		{
			high=mid-1;
		}
		else
		{
			return true;
		}
	}
	return false;
}

int main()
{
	ifstream fin("A-small-attempt1.in",ios::in);
	ofstream fout("output.txt",ios::out);
	int i,j,k;
	int iv[15];
	char tempstring[16];
	char tempinput[421];
	int currentcount;
	bool needp;
	bool skip;
	fin>>l>>d>>n;
	fin>>exist[0];
	for(j=0;j<l;j++)
	{
		testcharbool[j][exist[0][j]-'a']=true;
	}
	last=0;
	for(i=0;i<d-1;i++)
	{
		current=0;
		fin>>tempstring;
		for(j=0;j<l;j++)
		{
			testcharbool[j][tempstring[j]-'a']=true;
		}
		while(strcmp(tempstring,exist[current])>0&&exist[current][0]!=0)
		{
			current++;
		}
		for(j=last;j>=current;j--)
		{
			strcpy(exist[j+1],exist[j]);
		}
		strcpy(exist[current],tempstring);
		last++;
	}
	for(i=0;i<n;i++)
	{
		fout<<"Case #"<<i+1<<": ";
		//input
		if(i==4)
		{
			int bp=1;
		}
		fin>>tempinput;
		for(j=0;j<15;j++)
		{
			testcharno[j]=0;
		}
		k=0;
		needp=false;
		for(j=0;j<strlen(tempinput);j++)
		{
			if(tempinput[j]=='(')
			{
				needp=true;
			}
			if(tempinput[j]==')')
			{
				needp=false;
				k++;
			}
			if(tempinput[j]<='z'&&tempinput[j]>='a')
			{
				if(testcharno[k]==0)
				{
					tempstring[k]=tempinput[j];
				}
				if(testcharbool[k][tempinput[j]-'a'])
				{
					testchar[k][testcharno[k]++]=tempinput[j];
				}
				if(!needp)
				{
					k++;
				}
			}
		}
		tempstring[k]='\0';
		//test
		currentcount=0;
		current=0;
		last=l-1;
		for(j=0;j<l;j++)
		{
			Pos[j]=0;
		}
		if(i==4)
		{
			int bp=1;
		}
		while(1)
		{
			skip=false;
			for(current=1;current<last;current++)
			{
				if(!isAllowed(tempstring,current+1))
				{
					skip=true;
					break;
				}
			}
			if(!skip)
			{
				current=last;
				while(Pos[current]>=testcharno[current])
				{
					current--;
				}
				if(current<0)
				{
					break;
				}
				if(current==last)
				{
					for(Pos[last]=0;Pos[last]<testcharno[last];Pos[last]++)
					{
						tempstring[last]=testchar[last][Pos[last]];
						if(isAllowed(tempstring))
						{
							currentcount++;
						}
					}
					continue;
				}
				Pos[current]++;
				if(Pos[current]>=testcharno[current])
				{
					continue;
				}
				tempstring[current]=testchar[current][Pos[current]];
				for(k=last;k>current;k--)
				{
					Pos[k]=0;
					tempstring[k]=testchar[k][0];
				}
			}
			else
			{
				Pos[current]++;
				while(Pos[current]>=testcharno[current]&&current>0)
				{
					current--;
					Pos[current]++;
				}
				if(current<0||(current==0&&Pos[current]>=testcharno[current]))
				{
					break;
				}
				tempstring[current]=testchar[current][Pos[current]];
				for(k=last;k>current;k--)
				{
					Pos[k]=0;
					tempstring[k]=testchar[k][0];
				}
			}
		}

		//out
		fout<<currentcount<<endl;
	}
	system("pause");
	return 0;
}