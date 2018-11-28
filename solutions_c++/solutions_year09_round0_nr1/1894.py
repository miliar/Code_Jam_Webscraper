#include<fstream>
#include<string>
using namespace std;
int main()
{
	fstream fin,fout;
	fin.open("A-large.in",ios::in);
	fout.open("A-large.out",ios::out);
	int L,D,N;
	fin>>L>>D>>N;
	int i,j,flag,k,n,count[L];
	string pD[D];
	bool result[L];
	string pPatternStr;
	char *pPattern[L];
	fin.get();
	for(i=0;i<D;i++)
		getline(fin,pD[i]);
	for(i=0;i<N;i++)
	{
		getline(fin,pPatternStr);
		flag=0;
		for(j=0,k=0;j<pPatternStr.length();j++)
		{
			if(pPatternStr[j]=='(')
			{
				flag=1;
				count[k]=0;
			}
			else if(pPatternStr[j]==')')
			{
				flag=0;
				pPattern[k]=new char[count[k]];
				for(n=0;n<count[k];n++)
					pPattern[k][n]=pPatternStr[j-count[k]+n];//?
				k++;
			}
			else
			{
				if(flag==1)
					count[k]++;
				else
				{
					count[k]=1;
					pPattern[k]=new char[1];
					pPattern[k][0]=pPatternStr[j];
					k++;
				}
			}
		}
		int COUNT=0;
		for(j=0;j<D;j++)
		{
			for(k=0;k<L;k++)
			{
				result[k]=false;
				for(n=0;n<count[k];n++)
				{
					if(pD[j][k]==pPattern[k][n])
					{
						result[k]=true;
						break;
					}
				}
			}
			bool temp;
			for(k=0,temp=true;k<L;k++)
				temp=temp&&result[k];
			if(temp)
				COUNT++;
		}
//		for(j=0;j<D;j++)
//			delete[] pPattern[j];
		fout<<"Case #"<<i+1<<": "<<COUNT<<endl;
	}
	return 0;
}
			
						
						
						
	
	
