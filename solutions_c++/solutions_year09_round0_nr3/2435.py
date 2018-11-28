#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
ifstream filein("C.in");
ofstream fileout("out.in");
int times(string & mother,string & son)	;
int main()	{
	string son("welcome to code jam");
	string mother;
	int linenum,ans;
	filein>>linenum;
	int size;
	for(int i=0;i<=linenum;i++)	{
		
		size=1000;
		getline(filein,mother);
		if(i==0) continue;
		//filein.getline(mother,600);
		ans=times(mother,son);
		if(ans>9999) ans=ans%10000;
		fileout<<"Case #"<<i<<": ";
		for(int j=3;j>0;j--)	{
			fileout<<(ans/size);
			ans=ans-(ans/size)*size;
			size/=10;
		}
		fileout<<ans<<endl;
	}
	
}

int times(string & mother,string & son)	{
	int num=0;
	if(son.length()==1)	{
		for(int i=0;i<mother.length();i++)	{
			if(son[0]==mother[i])
				num++;
		}
		return num;
	}
	else{
		int pos=0;
		while(-1!=mother.find(son[0],pos)){
			num+=times(mother.substr(mother.find(son[0],pos)+1,mother.length()-mother.find(son[0],pos)-1),son.substr(1,son.length()-1));
			pos=mother.find(son[0],pos)+1;
		}
		return num;
	}

}
