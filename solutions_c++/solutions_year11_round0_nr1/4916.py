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

int CountLines(char *filename)//获取文件的行数
{
	ifstream ReadFile;
	int n=0;
	string temp;
	ReadFile.open(filename,ios::in);//ios::in 表示以只读的方式读取文件
	if(ReadFile.fail())//文件打开失败:返回0
	{
		 return 0;
	}
	else//文件存在,返回文件行数
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
	cout<<"请输入要打开的文件名:"<<endl;
	cin>>filename;
	file.open(filename,ios::in);

	 ofstream in;
     in.open("output.out",ios::trunc); //ios::trunc表示在打开文件前将文件清空,由于是写入,文件不存在则创建


	if(file.fail())
	{
		cout<<"文件不存在."<<endl;
		file.close();
		cin.get();
		cin.get();
	}
	else//文件存在
	{
		LINES=CountLines(filename);
		int *tc=new int[LINES];  
		int i=0; 
		while(!file.eof()) //读取数据到数组,file.eof()判断文件是否为空
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
							//	Btagnum=Bp->bunum;//B标志保留原地
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
	in.close();//关闭文件
	file.close(); //关闭文件	
}