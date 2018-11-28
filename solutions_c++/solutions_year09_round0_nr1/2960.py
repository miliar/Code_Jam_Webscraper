#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;
int** allNum;
int jugdeNum=0;
ifstream fin("A-large.in",ios::binary);
ofstream fout("A-large.out",ios::binary);
bool myjudge(string str1,string str2)
{
	return (str1[jugdeNum]<str2[jugdeNum]);
}
void createDict(vector<string> &dict,int D)
{
	string temp;
	int letterNum=0;
	int i=0;
	int j=0;
	for (i=0;i<D;i++)
	{
		fin>>temp;
		dict.push_back(temp);
		for (j=0;j<temp.size();j++)
		{
			letterNum = (char)temp[j]-'a';
			allNum[j][letterNum]+=1;
		}
	}
}
int findHead(vector<string> &dict,char letter,int pos)
{
	int i=0;
	string str;
	for (i=0;i<dict.size();i++)
	{
		str=dict[i];
		if (str[pos]==letter)
		{
			return i ;
		}
	}
}
bool ReallyMatch(string &dict,vector<string> &rest,string strComp)
{
	int i=0;
	int j=0;
	for (i=0;i<strComp.size();i++)
	{
		if (strComp[i]=='$')
		{
			if(rest[j].find(dict[i])==string::npos)
			{
				return false;
			}
			j++;
		}
	}
	return true;
}
int BasicMatch(vector< string > &dict,vector<string> rest,string strComp)
{
	int i=0;
	int head;
	int j=0;
	while (strComp[i]=='$')
	{
		i++;
	}
	jugdeNum=i;
	sort(dict.begin(),dict.end(),myjudge);
	//cout<<"hello"<<endl;
	int selcount = 0;
	if(i==strComp.size())
	{
	    head=0;
	    selcount = dict.size();
    }
    else
    {
	head=findHead(dict,strComp[i],i);
	selcount=allNum[i][strComp[i]-'a'];
    }
    int matchNum=0;
	string test;
	//cout<<"head"<<head<<"  "<<"selecount"<<selcount<<endl;
	for (j=head;j<head+selcount;j++)
	{
		test = strComp;
		for (int k=0;k<test.size();k++)
		{
			if (test[k]=='$')
			{
				test[k]=(dict.at(j))[k];
			}
		}
		if (test==dict[j])
		{
			if (ReallyMatch(dict[j],rest,strComp))
			{
				matchNum++;
			}

		}
	}
	return matchNum;

}
void workOut(vector< string > &dict,int N,int D)
{
	int i=0;
	int j=0;
	int repSt=0;
	int repEn=0;
	string str;

	for (i=0;i<N;i++)
	{

		fin>>str;
		vector<string> rest;
		while((repSt=str.find('('))!=string::npos&&(repEn=str.find(')'))!=string::npos)
		{
		    rest.push_back(str.substr(repSt+1,repEn-repSt-1));
		    str.replace(repSt,repEn-repSt+1,"$");
		    //cout<<str<<endl;
		    /*
		for (j=0;j<str.size();j++)
		{
			if (str[j]=='(')
			{
				repSt=j;
			}
			if (str[j]==')')
			{
				repEn=j+1;
				rest.push_back(str.substr(repSt,repEn));
				str.replace(repSt,repEn,"$");
				break;
			}
		}
		*/
		}
		//for(int x=0;x<rest.size();x++)
		//cout<<rest[x]<<endl;
		//cout<<str<<endl;
		//printf("Case# %d: %d\n",i,BasicMatch(dict,rest,str));
		fout<<"Case #"<<i+1<<": "<<BasicMatch(dict,rest,str)<<endl;
		rest.empty();
	}


}

int main()
{
/*
	vector< string > dict;
	dict.push_back("acahs");
	dict.push_back("abdss");
	dict.push_back("adeea");
	dict.push_back("cdssa");
	jugdeNum =2;
	sort(dict.begin(),dict.end(),myjudge);
	for (int i=0;i<dict.size();i++)
	{
		cout<<dict[i]<<endl;
	}
*/

	int L=0;
	int D=0;
	int N=0;
	int i=0;
	int j=0;

	fin>>L;
	fin>>D;
	fin>>N;
	//scanf("%d",&L);
	//scanf("%d",&D);
	//scanf("%d",&N);
	vector< string > dict;
	int** ppNum = (int**)malloc(L*sizeof(int*));
	for (i=0;i<L;i++)
	{
		ppNum[i] = (int*)malloc(26*sizeof(int));
	}
	allNum = ppNum;
	createDict(dict,D);
	workOut(dict,N,D);
	for(i=0;i<L;i++)
	{
	    if(ppNum[i])
        free(ppNum[i]);
    }
    fin.close();
    fout.close();
//	system("PAUSE");
	return 0;
}
