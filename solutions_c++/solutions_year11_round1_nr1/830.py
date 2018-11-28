#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,i,pd,pg,g,d;
	string n;
	bool b;
	cin>>t;
	for(int f=1;f<=t;f++){
		cout<<"Case #"<<f<<": ";
		b=0;
		cin>>n>>pd>>pg;
		if((pg==100&&pd!=pg)||(pg==0&&pg!=pd)){
			cout<<"Broken"<<endl;
			continue;;
		}
		if(n.length()>=3){
			cout<<"Possible"<<endl;
			continue;;	
		}
		int nn;
		if(n.length()==1)
		nn=n[0]-'0';
		else if(n.length()==2)
		nn=(n[0]-'0')*10+n[1]-'0';
		for(i=1;i<=nn;i++)
			if((i*pd)%100==0){
				b=1;
				break;
			}
		if(!b)
		cout<<"Broken"<<endl;
		else 
		cout<<"Possible"<<endl;
	}
	return 0;
}

