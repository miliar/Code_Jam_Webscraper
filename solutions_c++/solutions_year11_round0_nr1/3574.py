#include <iostream>
#include <fstream>
#include <string>
#include <cctype>
#include <stack>
using namespace std;
int main()
{
	freopen("D:\\codejam\\A-large.in","rt",stdin);
	freopen("D:\\codejam\\A-large.out","wt",stdout);
	int T;
	cin>>T;
	for (int i=1;i<=T;i++){
		int N,apos=1,bpos=1,Ca=0,Cb=0,time=0;
		char color='A';
		cin>>N;
		for (int j=1;j<=N;j++)
		{
			int num,temp;
			do{cin.get(color);}while(isspace(color));
			cin>>num;
			switch(color)
			{
			case 'O': temp=num<=apos?apos-num+1:num-apos+1;
					  if(Ca==0) 
					  {
						  Cb=Cb+temp;
						  time=time+temp;
					  }
					  else if(Ca>=temp) 
					  {
						  Ca=0;
						  time++;
						  Cb++;
					  }
					  else {
						Cb=Cb+temp-Ca;
						time=time+temp-Ca;
						Ca=0;
					  }
					  apos=num;
					  break;
			case 'B': temp=num<=bpos?bpos-num+1:num-bpos+1;
					  if(Cb==0) 
					  {
						  Ca=Ca+temp;
						  time=time+temp;
					  }
					  else if(Cb>=temp) 
					  {
						  Cb=0;
						  time++;
						  Ca++;
					  }
					  else {
						Ca=Ca+temp-Cb;
						time=time+temp-Cb;
						Cb=0;
					  }
					  bpos=num;
					  break;
			}
			
		}
		cout<<"Case #"<<i<<": "<<time<<endl;
	}
}