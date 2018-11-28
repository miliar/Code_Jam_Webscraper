#include<fstream>
#include<string>
using namespace std;
void function(int n,int* num,int& count,string str,string stdstr,int length);
int main()
{
	fstream fin,fout;
	fin.open("C-small-attempt3.in",ios::in);
	fout.open("C-small3.out",ios::out);
	int N;
	fin>>N;
	fin.get();
	string str;
	string stdstr="welcome to code jam";
	int num[20];
	int count;
	int i,j,l;
	for(i=0;i<N;i++)
	{
		count=0;
		getline(fin,str);
		l=str.length();
		for(j=0;j<l-18;j++)
		{
			num[0]=j;
			function(0,num,count,str,stdstr,l);
		}
		fout.fill('0');
		fout<<"Case #"<<i+1<<": ";
		fout.width(4);
		fout<<count;
		fout<<endl;
	}
	return 0;
}
void function(int n,int* num,int& count,string str,string stdstr,int length)
{
	if(n<19)
	{
		if(str[num[n]]==stdstr[n])
		{
			if(n<18)
			{
				for(num[n+1]=num[n]+1;num[n+1]<length+n-17;num[n+1]++)
				{
					function(n+1,num,count,str,stdstr,length);
				}
			}
			else if(n==18)
			{
				for(;num[n]<length;num[n]++)
				{
					if(str[num[n]]==stdstr[n])
					{
						count++;
					}
				}
				return;
			}
		}
	}
}
