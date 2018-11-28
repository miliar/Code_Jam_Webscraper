#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<map>
using namespace std;

string chk="welcome to code jam";
string mainstr;
int ct;

void traverse(char ch,int posn,int orig)
{
	if(posn==(int)chk.size()){ct++;return;}
	for(int i=orig;i<((int)mainstr.length());i++)
	{
		
		if(mainstr[i]==ch)
		{
			if(posn+1<(int)chk.size())
			traverse(chk[posn+1],posn+1,i);
			else 
			traverse('m',posn+1,i);
		}
		
	}
	return;
}
int main()
{
	int no,i=0;
	
 	vector<string> xx;
 	
       	while(getline(cin, mainstr))
       	{
       	xx.push_back(mainstr);
       	
       	}
       	
        
	for(int j=1;j<xx.size();j++)
	{
		ct=0;
		mainstr=xx[j];
		traverse(chk[0],0,0);
		int arr[4],s;
		for(int k=1,s=3;k<10001;k*=10,s--)
		{
			arr[s]=ct%10;
			ct=ct/10;
		}
		cout<<"Case #"<<j<<": ";for(s=0;s<4;s++)cout<<arr[s];cout<<endl;
	}
	return 0;      		
 
}



