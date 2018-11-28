

#include <iostream>
#include <string>
#include <stack>
#include <fstream>

using namespace std;


int N;
int strNum;
int* flag;
string* strArray;
int curStrNum;

int getloc(string str)
{
	for(int i=0;i<strNum;i++)
	{
		if(str==strArray[i])
			return i;
	}
}

int myfind(int before)
{
	int i;
	int loc=-1;
	string str;
	
	for(i=0;i<strNum;i++)
	{
		flag[i]=0;
	}
	
	i=0;
	if(before>-1)
	{
		//cout<<"helll:"<<before<<endl;
		flag[before]=1;
		i=1;
	}

	cin.sync();
	for(;curStrNum<N;)//&&loc!=before
	{
	    char s[110];
		cin.getline(s,110,'\n');
		string str(s);
	   
		curStrNum++;
		
		loc=getloc(str);
		
		if(flag[loc]==0)
		{
			if(i==strNum-1)
			{
				return loc;
			}
		
			flag[loc]=1;
			i++;
			//cout<<str<<"\t"<<i<<endl;
		}
	}

	return -1;

	
	/*if(loc==before)
	{
		cout<<"i beofer:"<<before<<endl;
		return before;
	}
	else
	{*/
	/*	for(i=0;i<strNum;i++)
		{
			if(flag[i]==0)
			{
				cout<<"i:"<<i<<endl;
				return i;
			}
		}
	//}
	cout<<"ERROR"<<endl;*/
}
int main()
{
	//ifstream in("A-small-attempt1.in");
	ofstream out("answer.txt");
	int total;
	cin>>total;
	//in>>total;
	
	int n=0,i;
	int before;
	int count;
	
	while(n++<total)
	{
		before=-2;
		count=0;
		cin>>strNum;
		strArray=new string[strNum];
		flag=new int[strNum];
	
	
		cin.sync();
		for(i=0;i<strNum;i++)
		{
			char s[110];
		    cin.getline(s,110,'\n');
		    string str(s);
			strArray[i]=str;
			//getline(cin,strArray[i]);
		}
		
		
		cin>>N;
		
		curStrNum=0;
		
		while(curStrNum<N)
		{
			
			before=myfind(before);//before
			//cout<<"before:"<<before<<endl;
		    if(before>-1)
			{
				count++;
			}
			else
				break;
		}
	
		
		out<<"Case #"<<n<<": "<<count<<endl;
		//delete strArray;
		//delete flag;
	}
	
	
	return 0;
}