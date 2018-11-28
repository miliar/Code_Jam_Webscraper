#include <iostream>
#include <string>
using namespace std;

struct node
{
	int pos;
	int num;
};

char pattern[]={"welcome to code jam"};
node total[19][500];
int num[19];

void Init()
{
	for (int i=0; i<19; i++)
	{
		for (int j=0; j<500; j++)
		{
			total[i][j].num=-1;
		}
		num[i]=0;
	}
}

void InitNum(int index, int pos)
{
	total[index][num[index]].pos=pos;
	num[index]++;
	if (index==1)
	{
		index=6;
		total[index][num[index]].pos=pos;
		num[index]++;
		index=14;
		total[index][num[index]].pos=pos;
		num[index]++;
		return;
	}
	if(index==3)
	{
		index=11;
		total[index][num[index]].pos=pos;
		num[index]++;
		return;
	}
	if (index==4)
	{
		index=9;
		total[index][num[index]].pos=pos;
		num[index]++;
		index=12;
		total[index][num[index]].pos=pos;
		num[index]++;
		return;
	}
	if (index==5)
	{
		index=18;
		total[index][num[index]].pos=pos;
		num[index]++;
		return;
	}
	if(index==7)
	{
		index=10;
		total[index][num[index]].pos=pos;
		num[index]++;
		index=15;
		total[index][num[index]].pos=pos;
		num[index]++;
		return;
	}
}

int Contain(char ch)
{
	for(int i=0; i<strlen(pattern);i++)
		if(pattern[i]==ch)
			return i;
	return -1;
}

void CountString(const char* str)
{
	for (int i=0; i<strlen(str); i++)
	{
		int pos=Contain(str[i]);
		if (pos>-1)
		{
			InitNum(pos,i);
		}
	}
}

void CalcuteStrings(int index, int pos)
{
//	cout<<index<<" "<<pos<<endl;
	if(index==18)
	{
		if(num[index]==0)
			total[index][pos].num=0;
		total[index][pos].num=1;
	}
	else
	{
		total[index][pos].num=0;
		for(int i=0; i<num[index+1]; i++)
		{
			if (total[index+1][i].pos>total[index][pos].pos)
			{
				while (i<num[index+1])
				{
					if(total[index+1][i].num<0)
						CalcuteStrings(index+1,i);
					total[index][pos].num+=total[index+1][i].num;
					if(total[index][pos].num>10000)
						total[index][pos].num=(total[index][pos].num)%10000;
					i++;
				}
			}
		}
	}
}

int GetNum(char*s)
{
	Init();
	CountString(s);
	int nums=0;
	for (int i=0; i<num[0]; i++)
	{
		CalcuteStrings(0, i);
		nums+=total[0][i].num;
		if(nums>10000)
			nums=(nums)%10000;
	}
	return nums;
}

int main()
{
	//FILE *f=freopen("e:\\C-small-attempt0.in","r",stdin);
	//FILE *fout=freopen("e:\\out.txt","w", stdout);
	int num;
	char text[500];
	cin>>num;
	for (int i=1; i<=num; i++)
	{
		int j=0;
		char ch;
		scanf("%c",&ch);
		while(!(ch==' '||(ch>='a' && ch<='z')))
			scanf("%c",&ch);
		while (ch!='\n')
		{
			text[j++]=ch;
			scanf("%c",&ch);
		}
		text[j]='\0';
		cout<<"Case #"<<i<<": ";
		int num=GetNum(text);
		if(num<10)
			cout<<"0";
		if(num<100)
			cout<<"0";
		if(num<1000)
			cout<<"0";
		cout<<num<<endl;
	}
}