#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
	int p,r;
	cin>>p;
	r=p;
	while(p--)
	{
		string str,st="";
		/*	for(int i=0;i<6;i++)
		{
			cin>>a[i];
		}*/
		cin>>str;
		int f=0,min=INT_MAX,in,i,t;
		for(i=str.length()-1;i>0;i--)
		{
			if(str[i]>str[i-1])
			{
				t=int(str[i-1]-48);
				//swap(str[i],str[i-1]);				
				f=1;
				break;
			}	
		}
		if(f)
		{
			for(int j=i;j<str.length();j++)
			{
				if(int(str[j]-48)<min&&int(str[j]-48)>t)
				{	min=int(str[j]-48);
					in=j;
				}
			}
			swap(str[i-1],str[in]);
			for(int k=i;k<str.length()-1;k++)
			{
				for(int j=k+1;j<str.length();j++)
				{
					if(str[k]>str[j])
						swap(str[k],str[j]);
				}
			}
		}
		else 
		{
			int c=0,t=str.length()-1;
			while(str[t--]=='0'){c++;}
			t++;
			st+=str[t];
			while(c--)
				st+='0';
			st+='0';
			t--;
			for(int i=t;i>=0;i--)
			{
				st+=str[i];
			}
			//cout<<st;
			str=st;
		}
		//cout<<r<<p<<endl;
		cout<<"Case #"<<r-p<<": "<<str<<endl;
	}
		
//    system("pause");
    return 0;
}
