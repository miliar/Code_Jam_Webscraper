#include<iostream>
#include<math.h>
#include<string.h>
//#include<conio.h>
using namespace std;
//static char *contained;
class Pattern{
	char ch;
	Pattern *next;
	public:
	Pattern(){//CONSTRUCTOR
		ch='\0';
		next=NULL;
	}

	void add(char c,int k=1){
		if(k==0)
        	{
	             ch=c;
		     next=0;
		}

		else
		{
			Pattern *temp=this;
			while(temp->next!=0)
			{
		//		cout<<ch<<' '<<temp->next->ch<<endl;
				temp=temp->next;
			}
			temp->next=new Pattern;
			temp->next->ch=c;
			temp->next->next=0;
		}
	
	}
	int check(char c)
	{
		Pattern *temp=this;
		while(temp!=0)
		{
		//	cout<<ch<<' '<<c<<endl;
			if(temp->ch==c)
			{
		//		cout<<endl;
				return 0;
			}
			temp=temp->next;
		}
		return 1;
	}
	
};

int main()
{
	Pattern *p;
	int L,D,N,i;
	char zz;
	list *pt;
	list *str;
	list<char>::iterator s;
	list<string> *pat;
	cin>>L>>D>>N;
	str=new list<char>[D];
	pt=new list<string>[N];
	p=new Pattern[N];
	
/*	for(i=0;i<D;i++)
	{
		str[i]=new char[L];
	}
	for(i=0;i<N;i++)
		pt[i]=new char[400];*/

	int n,j,l,l1,cnt=0,flag=0;
	
	for(i=0;i<D;i++)
	 {
		 cin>>zz;
		 str[i].push_back(zz);
	 }
	for(i=0;i<N;i++)
	  for(int y=0;y<L;y++)
        	{
			cin>>zz;
			pt[i].push_back(zz);
		}
	
	for(int m=0;m<N;m++)
	{
		////////////////////l=strlen(pt[m]);
		//l1=strlen(str[m]);
	//	for(i=0,j=0;pt!=j<L&&i<l;i++,j++)
		for(pat=pt.begin(),s=str[m].begin();pat!=pt.begin()&&s!=str[m].begin
		{
			if(pt[m][i]!='(')
			{
				p[j].add(pt[m][i],0);
		//		cout<<"success"<<pt[m][i]<<endl;


			}
			else
			{
				static int flg=1;
				i++;
				while(pt[m][i]!=')'&&i<l)
				{
					if(flg)
                                          {
						p[j].add(pt[m][i],0);
		//				cout<<"success in else if"<<pt[m][i]<<endl;
					}	
					else
					{
					p[j].add(pt[m][i]);
		//			cout<<"success in else else"<<pt[m][i]<<endl;
					}
					i++;
					flg=0;
				}
				
				flg=1;
			}
		}
		//cout<<"hai"<<endl;
		static int flag=-1;
		for(int z=0;z<D;z++)
		{
		for(int t=0;t<L;t++)
		{
			flag+=p[t].check(str[z][t]);
			
			if(flag)
			{
		//		cout<<endl<<str[z]<<endl;
				break;
			}
		}
		if(flag==0)
		{
		//	cout<<endl;
			cnt++;
		}
		flag=0;
		}
		cout<<"Case #"<<m+1<<": "<<cnt<<endl;
		delete p;
		p=0;
		cnt=0;
		p=new Pattern[D];
	}

}
