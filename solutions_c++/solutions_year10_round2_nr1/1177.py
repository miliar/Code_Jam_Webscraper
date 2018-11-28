#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
#include<map>

using namespace std;
const int sizeAtt = 100;
ifstream infile("c:/input.txt");
ofstream  outfile("c:/output.txt",ios_base::out);
void checkDirs(int n,int M,int Case)
{
int i=0;
map<string,int> mapDirs;
int pos=0,posPrev=0;
string tempstr,dirName;
int count=0;
//cout<<"Case is "<<Case+1<<endl;
		for(i=0;i<n;i++)
		{
			infile>>dirName;
			mapDirs[dirName]=1;
			pos=dirName.find('/',1);
		//	cout<<"Just started"<<endl;
	//		cout<<dirName<<endl;
			while(pos != string::npos)
			{
		//	cout<<"Pos is "<<pos<<endl;
			tempstr=dirName.substr(0,pos);
		//	cout<<"Temp "<<tempstr<<endl;
			mapDirs[tempstr]=1;
			pos=dirName.find('/',pos+1);
			}
		}

	//	cout<<"Finished processeing"<<endl;

		for(i=0;i<M;i++)
		{
			infile>>dirName;
			if(mapDirs.count(dirName)>0)
			{
				continue;
			}
			mapDirs[dirName]=1;
			count++;
			pos=dirName.rfind('/');
			tempstr=dirName;
			while(pos != string::npos)
			{
			if(pos == 0)
			{
				break;
			}
			tempstr=tempstr.substr(0,pos);
	//		cout<<"Search String is "<<tempstr<<endl;
			if(mapDirs.count(tempstr)>0)
			{
				break;
			}
			mapDirs[tempstr]=1;
			count++;
			pos=tempstr.rfind('/');
	//		cout<<"Pos i "<<pos<<endl;
			}
		}
		outfile<<"Case #"<<Case+1<<": "<<count<<endl;
		cout<<"Case #"<<Case+1<<" "<<count<<endl;
}

int main()
{
	long tCases=0,i=0,ii=0,tempA=0,tempB=0,j=0;
	
	int moveAct =0;
	
	long int cumSum =0;
	
	infile>>tCases;
	int num1=0,num2=0;
	string dirName;
	
	//cout<<"Num Cases"<<tCases<<endl;
	//cout<<"Just Started"<<endl;
	for(ii=0;ii<tCases;ii++)
	{

		infile>>num1>>num2;
	
		checkDirs(num1,num2,ii);
	}
}
