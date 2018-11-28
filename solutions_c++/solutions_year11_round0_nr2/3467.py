#include <fstream>
#include <cstdio>
#include <cstring>


using namespace std;

char base[8]={'Q','W', 'E', 'R', 'A', 'S', 'D', 'F'};
bool opposed[8][8];
bool bcombine[8][8];


void SetZero()
{
	for(int i=0;i<8;i++)
	{
		for(int j=0;j<8;j++)
		{
			opposed[i][j]=false;
			bcombine[i][j]=false;
		}
	}
}

int Hash(char c)
{
	for(int i=0;i<8;i++)
		if(c==base[i])
			return i;
	return -1;
}

int Find(char c,char str[],int n)
{
	int u=Hash(c);
	if(u==-1)return -1;	
	for(int i=0;i<n;i++)
	{
		int v=Hash(str[i]);
		if(v==-1)continue;
		else if(opposed[u][v])
			return i;
	}
	return -1;
}

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("test.out");
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		SetZero();
		char str[108];
		char result[108];
		char ccombine[8][8];
		int C;
		int D;
		int N;			
		char cbasei;
		char cbasej;
		char cnonbase;
		int ibasei;
		int ibasej;
		fin>>C;
		for(int x=1;x<=C;x++)
		{
			fin>>cbasei>>cbasej>>cnonbase;
			ibasei=Hash(cbasei);
			ibasej=Hash(cbasej);
			bcombine[ibasei][ibasej]=true;ccombine[ibasei][ibasej]=cnonbase;
			bcombine[ibasej][ibasei]=true;ccombine[ibasej][ibasei]=cnonbase;
		}
		fin>>D;
		for(int y=1;y<=D;y++)
		{
			fin>>cbasei>>cbasej;
			ibasei=Hash(cbasei);
			ibasej=Hash(cbasej);
			opposed[ibasei][ibasej]=true;
			opposed[ibasej][ibasei]=true;
		}
		fin>>N;
		for(int z=0;z<N;z++)
			fin>>str[z];
		str[z]='\0';
		
		
		//模拟元素的调用
		int k=0;
		ibasei=Hash(str[0]);
		result[k]=str[0];
		result[k+1]='\0';
		for(int j=1;j<N;j++)
		{
			ibasej=Hash(str[j]);
			if(ibasej==-1)//str[j]是非基本元素
			{
				result[++k]=str[j];
				result[k+1]='\0';
				ibasei=ibasej;
			}
			else//str[j]是基本元素
			{
				if(ibasei==-1 || !bcombine[ibasei][ibasej])
				{
					int index=Find(str[j],result,k+1);
					if(index==-1)
					{
						result[++k]=str[j];
						result[k+1]='\0';
						ibasei=ibasej;
					}
					else
					{						
						result[0]='\0';
						k=-1;
						ibasei=-1;
					}
				}				
				else
				{
					cnonbase=ccombine[ibasei][ibasej];
					result[k]=cnonbase;
					result[k+1]='\0';
					ibasei=Hash(cnonbase);
				}
			}
		}
		result[k+1]='\0';
		fout<<"Case"<<' '<<'#'<<i<<':'<<' '<<'[';
		int len=strlen(result);
		int m=0;
		while(m<len-1)
			fout<<result[m++]<<','<<' ';
		if(m<len)
			fout<<result[m];
		fout<<']'<<endl; 
	}
	return 0;
}