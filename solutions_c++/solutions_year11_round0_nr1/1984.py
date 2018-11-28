#include <iostream>
#include<sstream>

#include <cmath>
using namespace std;

int o[110],b[110];
int main ()
{
	int t,n;
	int temp1=0,temp2=0,sum=0;
	bool oflag=false,bflag=false;
	char ch;
	char str[110];

	freopen("C:\\Users\\NAZI\\Desktop\\A-large.in", "rt", stdin);
	freopen("C:\\Users\\NAZI\\Desktop\\A-large.out", "wt", stdout);
	
	cin>>t;

	o[0]=1;
	b[0]=1;
	for (int i=0;i<t;i++)
	{//1
		cin>>n;
		for(int j=1;j<=n;j++)
		{//2
			cin>>ch;
			if(ch=='O'&&j==1)
			{
				oflag=true;
			}
			if(ch=='B'&&j==1)
			{
				bflag=true;
			}

			if(ch=='O')
			{
				cin>>o[j];
				str[j]=ch;//char shun xu
			}
			if(ch=='B')
			{
				cin>>b[j]; 
				str[j]=ch;//char shun xu
			}
		}//2

		if(oflag==true)
		{//oflag
			sum=o[1];
			temp1=sum;
			oflag=false;

			for(int p=2;p<=n;p++)
			{//p loop
				if(str[p]==str[p-1])
				{///前后一致
					if(str[p]=='O')
					{
						sum+=abs(o[p]-o[p-1])+1;
						temp1+=abs(o[p]-o[p-1])+1;
						
					}
					if(str[p]=='B')
					{
						sum+=abs(b[p]-b[p-1])+1;
						temp2+=abs(b[p]-b[p-1])+1;
						
					}
				}///前后一致
				else///////前后不一致
				{
					if(str[p]=='O')
					{///BO
						int q=1;
						while( str[p-q]!='O')
						{
							++q;
							if(p-q==0)
							{
								break;
							}
						}

						if( temp2>=abs(o[p]-o[p-q]) )
						{
							sum+=1;
							temp1=1;
						}
						else
						{
							sum+=abs(o[p]-o[p-q])-temp2+1;
							temp1=abs(o[p]-o[p-q])-temp2+1;
						}

					}////BO
					if(str[p]=='B')
					{//OB
						int q=1;
						while(str[p-q]!='B')
						{
							q++;
							if(p-q==0)
							{
								break;
							}
						}

						if(temp1>=abs(b[p]-b[p-q]) )
						{
							sum+=1;
							temp2=1;
						}
						else
						{
							sum+=abs(b[p]-b[p-q])-temp1+1;
							temp2=abs(b[p]-b[p-q])-temp1+1;
						}
					}//OB
				}//前后不一致
			}//p loop
		}//oflag
		if(bflag==true)
		{//bflag
			sum=b[1];
			temp2=sum;
			bflag=false;

			for(int p=2;p<=n;p++)
			{//p loop
				if(str[p]==str[p-1])
				{///前后一致
					if(str[p]=='O')
					{
						sum+=abs(o[p]-o[p-1])+1;
						temp1+=abs(o[p]-o[p-1])+1;

					}
					if(str[p]=='B')
					{
						sum+=abs(b[p]-b[p-1])+1;
						temp2+=abs(b[p]-b[p-1])+1;

					}
				}///前后一致
				else///////前后不一致
				{
					if(str[p]=='O')
					{///BO
						int q=1;
						while( str[p-q]!='O')
						{
							++q;
							if(p-q==0)
							{
								break;
							}
						}

						if( temp2>=abs(o[p]-o[p-q]) )
						{
							sum+=1;
							temp1=1;
						}
						else
						{
							sum+=abs(o[p]-o[p-q])-temp2+1;
							temp1=abs(o[p]-o[p-q])-temp2+1;
						}

					}////BO
					if(str[p]=='B')
					{//OB
						int q=1;
						while(str[p-q]!='B')
						{
							q++;
							if(p-q==0)
							{
								break;
							}
						}

						if(temp1>=abs(b[p]-b[p-q]) )
						{
							sum+=1;
							temp2=1;
						}
						else
						{
							sum+=abs(b[p]-b[p-q])-temp1+1;
							temp2=abs(b[p]-b[p-q])-temp1+1;
						}
					}//OB
				}//前后不一致
			}//p loop
		}//bflag

		cout<<"Case #"<<i+1<<": "<<sum<<endl;
		sum=0;temp1=0;temp2=0;

	}//1

	return 0;
}

