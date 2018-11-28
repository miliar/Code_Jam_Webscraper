#include <fstream>
#include <string>

using namespace std;

static ofstream out("out.txt");
static ifstream in("A-large.in");


static string Dic[5000];
static string wordList[15];
static int visited[15][26];

void ReadDic(int N)
{
	int i;
	
	for(i=0;i<N;++i)
	{
		in >> Dic[i];
	}
}

int ReadWordList(int L)
{
	int i,length;
	int index(0),flag(0);
	string str,tmp;
	
	in >> str;
	length=str.length();
	for(i=0;i<length;++i)
	{
		if(str[i]=='(')
		{
			tmp="";
			flag=1;
		}
		else
			if(str[i]==')')
			{
				flag=0;
				wordList[index++]=tmp;
			}
			else
			{
				if(!flag)
				{
					tmp=str[i];
					wordList[index++]=tmp;
				}
				else
				{
					tmp+=str[i];
				}
			}
	}
	
	return index;
}

void UpdateInfo(int L)
{
	int i,j;
	int length;

	for(i=0;i<15;++i)
	{
		for(j=0;j<26;++j)
		{
			visited[i][j]=0;
		}
	}

	for(i=0;i<L;++i)
	{
		length=wordList[i].size();
		for(j=0;j<length;++j)
		{
			visited[i][wordList[i][j]-'a']=1;
		}
	}
}

int GetWordNum(int D, int L)
{
	int i,j;
	int Num(0);
	int length;

	for(i=0;i<D;++i)
	{
		length=Dic[i].size();
		if(length!=L)
			break;

		for(j=0;j<length;++j)
		{
			if(!visited[j][Dic[i][j]-'a'])
				break;
		}
		if(j==length)
			Num++;
	}

	return Num;
}

int main()
{
	int L,D,N;
	int Num,i;

	in >> L >> D >> N;
	ReadDic(D);
	for(i=0;i<N;++i)
	{
		ReadWordList(L);
		UpdateInfo(L);
		Num=GetWordNum(D, L);
		out << "Case #" << i+1 << ": " << Num << endl;
	}

	return 0;
}