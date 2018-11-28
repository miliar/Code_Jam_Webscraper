

#include<stdio.h>
#include<conio.h>
#include<iostream.h>

void main()
{

int t;
int n,s,p,score,all,er;
int i=0,result=0;
cin>>t;

while(t--)
{
	cin>>n>>s>>p;
	cout<<"n S P : "<<n<<" "<<s<<" "<<p<<endl;
	 result=0;
	 while(n--)
	{
	cin>>score;
	all=score/3;
	er=score%3;

	if(all>=p){result++; }
	if((p-all)==1&&er==0&&s){ s--; result++;}
	if((p-all)==1&&er>0){ result++;}
	if((p-all)==2&&er==2&&s){ s--; result++;}
       //	if((p-all)=2&&er==1&&s){ s--; result++}

	}
	cout<<"Case #"<<++i<<": "<<result<<endl;


}


}

