#include<iostream.h>
#include<math.h>
#include <fstream>
#include <string>
using namespace std;
struct node
{
	char ch;
	int bunum;
	int seq;
	node *next;
	node(){next=NULL;}
	node(char c,int b,int s,node *n=NULL);
};
node::node(char c,int b,int s,node *n)
{
	ch=c;
	bunum=b;
	seq=s;
	next=n;
}
class linkqueue
{
private:
	node *first,*rear;
public:
	linkqueue(){first=NULL;rear=NULL;}
	~linkqueue();
	node* retfist();
	void insert(node &seq);
	void delqueue();
};

linkqueue::~linkqueue()
{
	if(first!=NULL)
	{
		delqueue();
	}
	else return;
}
node* linkqueue::retfist( )
{
	return first;
}
void linkqueue::insert(node &seq)
{
	if(first==NULL)
	{
		first=rear=new node(seq.ch,seq.bunum,seq.seq,NULL);
	}
	else
	{
		node *p=rear;
		rear=rear->next=new node(seq.ch,seq.bunum,seq.seq,NULL);
	}
}
void linkqueue::delqueue()
{
	if(first==NULL) return;
	else
	{
		node *p=first;
		first=first->next;
		delete p;
	}
}

int CountLines(char *filename)//��ȡ�ļ�������
{
	ifstream ReadFile;
	int n=0;
	string temp;
	ReadFile.open(filename,ios::in);//ios::in ��ʾ��ֻ���ķ�ʽ��ȡ�ļ�
	if(ReadFile.fail())//�ļ���ʧ��:����0
	{
		 return 0;
	}
	else//�ļ�����,�����ļ�����
	{
		while(getline(ReadFile,temp))
		{
			n++;
		}
		return n;
	}
	ReadFile.close();
}

void main()
{
	int time,Otagnum,Btagnum;
	ifstream file; 
	int LINES;
	char filename[512];
	cout<<"������Ҫ�򿪵��ļ���:"<<endl;
	cin>>filename;
	file.open(filename,ios::in);

	 ofstream in;
     in.open("output.out",ios::trunc); //ios::trunc��ʾ�ڴ��ļ�ǰ���ļ����,������д��,�ļ��������򴴽�


	if(file.fail())
	{
		cout<<"�ļ�������."<<endl;
		file.close();
		cin.get();
		cin.get();
	}
	else//�ļ�����
	{
		LINES=CountLines(filename);
		int *tc=new int[LINES];  
		int i=0; 
		while(!file.eof()) //��ȡ���ݵ�����,file.eof()�ж��ļ��Ƿ�Ϊ��
		{ 
			file>>tc[i];
			time=0;
			Otagnum=1;
			Btagnum=1;
			linkqueue O,B;
			if(i>0)
			{
				char *ch=new char[tc[i]];
				int *num=new int[tc[i]];
				//cout<<tc[i]<<" ";
				for(int j=0;j<tc[i];j++)
				{
					file>>ch[j];
					file>>num[j];
				}

		
				for(j=0;j<tc[i];j++)
				{
					if(ch[j]=='O'||ch[j]=='o')
					{
						node p(ch[j],num[j],j,NULL);
						O.insert(p);				
					}
					else 
					{
						node p(ch[j],num[j],j,NULL);
						B.insert(p);
					}
				}

	

	
				while(O.retfist()!=NULL&&B.retfist()!=NULL)
				{
					node *Op=O.retfist(),*Bp=B.retfist();
					if(Op->seq<Bp->seq)
					{
						if(Op->bunum<Bp->bunum)
						{
							for(int i=0;i<=abs(Op->bunum-Otagnum);i++)
							{
								time++;
								if(Btagnum>Bp->bunum)
								{
			    					Btagnum--;
								}
								if(Btagnum<Bp->bunum)
								{
									Btagnum++;
								}
							}
							Otagnum=Op->bunum;
							O.delqueue();
						}
						else
						{
							for(int i=0;i<=abs(Op->bunum-Otagnum);i++)
							{
								time++;
								if(Btagnum>Bp->bunum)
								{
			    					Btagnum--;
								}
								if(Btagnum<Bp->bunum)
								{
									Btagnum++;
								}
							}
							Otagnum=Op->bunum;
							//if(Btagnum<Bp->bunum)
							//{
							//	Btagnum=Bp->bunum;//B��־����ԭ��
							//}
						//	else
						//{
							//	Btagnum=Bp->bunum-abs(Bp->bunum-Btagnum);
							//}
							O.delqueue();
						}
					}
					else
					{
						if(Bp->bunum<Op->bunum)
						{
							for(int i=0;i<=abs(Bp->bunum-Btagnum);i++)
							{
								time++;
								if(Otagnum>Op->bunum)
								{
									Otagnum--;
								}
								if(Otagnum<Op->bunum) 
								{
									Otagnum++;
								}
							}
							Btagnum=Bp->bunum;
					
							B.delqueue();
						}
						else
						{
							for(int i=0;i<=abs(Bp->bunum-Btagnum);i++)
							{
								time++;
								if(Otagnum>Op->bunum)
								{
									Otagnum--;
								}
								if(Otagnum<Op->bunum) 
								{
									Otagnum++;
								}
							}
							Btagnum=Bp->bunum;
							B.delqueue();
						}
					}
	
				}
				while(O.retfist()!=NULL&&B.retfist()==NULL)
				{
					node *Op=O.retfist();
					for(int i=0;i<=abs(Op->bunum-Otagnum);i++)
					{
						time++;
					}
					Otagnum=Op->bunum;
					O.delqueue();
				}
		
				while(O.retfist()==NULL&&B.retfist()!=NULL)
				{
					node *Bp=B.retfist();
					for(int i=0;i<=abs(Bp->bunum-Btagnum);i++)
					{
						time++;
					}
					Btagnum=Bp->bunum;
					B.delqueue();
				}
				if(i<=20)
				{
				in<<"Case #"<<i<<": "<<time<<"\n";
				}
			}
			i++;
		}
		 
	} 
	in.close();//�ر��ļ�
	file.close(); //�ر��ļ�	
}