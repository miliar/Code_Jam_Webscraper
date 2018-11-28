#include <iostream>
using namespace std;
struct Node
{
	int time;
	int flag;
	Node * next;
}*sa,*sb,*np,*nnp;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int N,T,A,B,i,j,k,m,flag,timea,timeb,ansa,ansb,cura,curb;
	char tmpa[10],tmpb[10];
	cin>>N;
	for(i=1;i<=N;i++)
	{
		cin>>T>>A>>B;
		cin.getline(tmpa,20);
		for(k=0;k<2;k++)
		{
			if(k==0)
			{
				m=A;
				flag=1;
			}
			else
			{
				m=B;
				flag=-1;
			}
			for(j=0;j<m;j++)
			{
				if(k==0)
				{
					cin.getline(tmpa,10,' ');
					cin.getline(tmpb,10);
					timea=(tmpa[0]-'0')*10+(tmpa[1]-'0');
					timea=timea*60;
					timea+=(tmpa[3]-'0')*10+(tmpa[4]-'0');
					timeb=(tmpb[0]-'0')*10+(tmpb[1]-'0');
					timeb=timeb*60;
					timeb+=(tmpb[3]-'0')*10+(tmpb[4]-'0')+T;
				}
				else
				{
					cin.getline(tmpb,10,' ');
					cin.getline(tmpa,10);
					timea=(tmpa[0]-'0')*10+(tmpa[1]-'0');
					timea=timea*60;
					timea+=(tmpa[3]-'0')*10+(tmpa[4]-'0')+T;
					timeb=(tmpb[0]-'0')*10+(tmpb[1]-'0');
					timeb=timeb*60;
					timeb+=(tmpb[3]-'0')*10+(tmpb[4]-'0');
				}				
				if(sa==NULL||sa->time>timea)
				{
					np=sa;
					sa=new Node;
					sa->next=np;
					np=sa;					
					np->time=timea;
					np->flag=0;
				}
				else
				{
					np=sa;
					while(np->next!=NULL&&np->next->time<=timea)
						np=np->next;
					if(np->time!=timea)
					{
						nnp=new Node;
						nnp->next=np->next;
						np->next=nnp;
						np=np->next;
						np->time=timea;
						np->flag=0;
					}					
				}
				np->flag-=flag;			
				if(sb==NULL||sb->time>timeb)
				{
					np=sb;
					sb=new Node;
					sb->next=np;
					np=sb;					
					np->time=timeb;
					np->flag=0;
				}
				else
				{
					np=sb;
					while(np->next!=NULL&&np->next->time<=timeb)
						np=np->next;
					if(np->time!=timeb)
					{
						nnp=new Node;
						nnp->next=np->next;
						np->next=nnp;
						np=np->next;
						np->time=timeb;
						np->flag=0;
					}
				}
				np->flag+=flag;
			}
		}
		ansa=ansb=0;
		cura=curb=0;
		while(sa!=NULL)
		{
			cura+=sa->flag;
			if(cura<0)
			{
				ansa-=cura;
				cura=0;
			}
			np=sa;
			sa=sa->next;
			delete np;
		}
		while(sb!=NULL)
		{
			curb+=sb->flag;
			if(curb<0)
			{
				ansb-=curb;
				curb=0;
			}
			np=sb;
			sb=sb->next;
			delete np;
		}
		cout<<"Case #"<<i<<": "<<ansa<<" "<<ansb<<endl;
	}
	return 0;
}