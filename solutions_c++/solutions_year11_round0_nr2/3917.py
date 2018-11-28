#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;
struct list
{
	list *front;
	list *back;
	char c;	
};
int comb_check(list *,list *,string,string,int);
int oppose_check(list *,list *,string,string,int);
string base="QWERASDF";
int main()
{
	vector <string> storeCom,storeOpp;
	int nCases,nCom,nOpp,nSeq;
	string iSeq;
	cin>>nCases;
	
	for(int j=0;j<nCases;++j)
	{
		string comHold,oppHold;
		cin>>nCom;
		
		storeCom.clear();
		storeOpp.clear();
		
		for (int i=0;i<nCom; ++i)
		{
			string temp;
			cin>>temp;
			comHold=comHold+temp;
			storeCom.push_back(temp);			
		}
	
		cin>>nOpp;
	
		for(int k=0;k<nOpp;++k)
		{
			string temp;
			cin>>temp;
			oppHold=oppHold+temp+'X';
			storeOpp.push_back(temp);
		}
		cin>>nSeq>>iSeq;
		//cout<<"comHold:"<<comHold<<endl<<"oppHold:"<<oppHold<<endl;
		//cout<<"iSeq:"<<iSeq<<endl;
		list *start,*end,*prev=NULL;
		start=new list;
		end=new list;
		start->c=iSeq[0];
		start->back=NULL;
		start->front=NULL;
		end=start;
		
		for(int i=1;i<nSeq;++i)
		{
			
			//check for combination
			int flag=comb_check(start,end,comHold,iSeq,i);
			//check for opposition if combination not found
			if(!flag)
			{
				int flag1=oppose_check(start,end,oppHold,iSeq,i);
				if(flag1)
				{
					if(i+1<nSeq)
					{
					//cout<<"end-- found d"<<end->c<<endl;
					start->c=iSeq[++i];
					start->front=NULL;
					start->back=NULL;
					end=start;
					}
					else
					start=NULL,end=NULL;
				}
				else
				{
					list *p=new list;
					p->c=iSeq[i];
					p->back=end;
					p->front=NULL;
					prev=end;
					end->front=p;
					end=p;		
					//cout<<"end--no c & d"<<end->c<<endl;

				}
			}
			//cout<<"end at end"<<end->c<<endl;
				
			

		}
		//Search combination string --- both
		
		list *p=start;
		vector <char> result;
		while(p!=NULL)
		{	
			//cout<<p->c;
			result.push_back(p->c);
			p=p->front;
		}

		cout<<"Case #"<<j+1<<": [";
		if(result.size()!=0)
		{
			for(int m=0;m<result.size()-1;m++)
			cout<<result[m]<<", ";
			cout<<result[result.size()-1];
		}
		cout<<"]"<<endl;

		start=NULL;
		end=NULL;
		//put first element in the start of the list
		
		
		
		
		
	}
	
	
	return 0;
}

int comb_check(list *start,list *end,string comHold,string iSeq,int i)
{			
		size_t found1=base.find(end->c);
		if(found1!=string::npos)
		{
			string temp="";
			temp=temp+end->c + iSeq[i];
			//cout<<"temp:"<<temp<<endl;
			size_t found;
			found=comHold.find(temp);
			if(found==string::npos)
			{	string temp="";
				temp=temp+iSeq[i] + end->c;
				found=comHold.find(temp);
				if(found==string::npos)
				{
					return 0;
				}
				else
				{
				end->c=comHold[found+2];
				iSeq[i]=end->c;
				//cout<<"end--found c"<<end->c<<endl;
				}
			}
			else
			end->c=comHold[found+2];
			return 1;
		}
		else
		return 0;

}


int oppose_check(list *start,list *end,string oppHold,string iSeq,int i)
{
		list *p=start;
		
	while(p!=NULL)
	{	
		size_t found;
		string temp="";
		temp=temp + p->c + iSeq[i];
		found=oppHold.find(temp);
		//cout<<"temp in d:"<<temp<<endl;
		if(found==string::npos)
		{
			string temp="";
			temp=temp+iSeq[i] + p->c;
			found=oppHold.find(temp);
			if(found==string::npos)
			p=p->front;
			else
			return 1;
		}
		else
		return 1;
		
	}
	return 0;
}