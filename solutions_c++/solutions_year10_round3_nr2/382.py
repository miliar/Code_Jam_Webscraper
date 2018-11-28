#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<math.h>

using namespace std;


int main()
{
	int notimes;
	scanf("%d",&notimes);
	

	int L,P,C;
	for(int cp=1;cp<=notimes;cp++ )
	{
		cin>>L>>P>>C;
		int coun=0,xx;
		int temp=P;
		xx=(temp+C-1)/C;
		while(xx>L){
			coun++;
			temp=xx;
			xx=(temp+C-1)/C;
		}
		//coun+=2;
		//cout<<coun<<endl;
		int mans;
		if(coun>0){
			float ans=(log10(coun)*1.0)/(log10(2))+1;
			mans=floor(ans);
		}
		else mans=0;
		//mans=ans;
			
		cout<<"Case #"<<cp<<": "<<mans<<endl;
	}
	return 0;
}
