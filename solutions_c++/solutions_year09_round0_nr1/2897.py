#include <iostream>
#include <fstream>
#include <exception>
#include <vector>

using namespace std;
unsigned L,D,N;
struct testInput
{
	vector<char*> kelimeler;
	
};
class tNode
{
	vector<tNode*> childs;
	char elem;
public:
	tNode(char c)
	{
		this->elem=c;
	};
	inline char getElem()
	{
		return elem;
	}
	void addWord(char* data)
	{
		if((*data)=='\0') throw std::exception("olmadi.");
		for(unsigned i=0;i<childs.size();i++)
		{
			if(childs[i]->getElem()==data[0]&& data[1]=='\0')
			{
				return;
			}
			else if(childs[i]->getElem()==data[0]&& data[1]!='\0')
			{
				childs[i]->addWord(data+1);
				return;
			}

		};
		tNode* temp=new tNode(data[0]);
		childs.push_back(temp);
		if(data[1]=='\0') return;
		temp->addWord(data+1);
		return;
	};
	int find(vector<char*> test,int pos)
	{
		
       if(pos==L)
	   {
		   int totalnum=0;
		   char* currentchar=test[pos];

		   for(unsigned i=0;currentchar[i]!='\0';i++)
		   {
			   if(currentchar[i]==this->elem) return 1;
		   };
		   return totalnum;
	   }
	   else
	   {
		   bool found=false;
			char* currentchar=test[pos];
			 for(unsigned i=0;currentchar[i]!='\0';i++)
		   {
			   if(currentchar[i]==this->elem)
			   {
				   found=true;
				   break;
			   };
		   };
			 if(found==false)return 0;
				 int totalnum=0;
				 for(unsigned j=0;j<childs.size();j++)
				 {
					 totalnum+=childs[j]->find(test,pos+1);
				 }
				 return totalnum;

	   };
	};
};	



int main(void)
{
	tNode* mainNode=new tNode('A');
	ifstream in("A-large.in");
	ofstream out("output.txt");
	char* temp=new char[5000];
	in.getline(temp,5000);
	unsigned pos1=0,pos2=0;
	while(temp[pos1]!=' ')
	{
		pos1++;
	}
	pos2=pos1+1;
	while(temp[pos2]!=' ')
	{
		pos2++;
	}

	L=atoi(temp);
	D=atoi(temp+pos1+1);
	N=atoi(temp+pos2+1);
	
	for(unsigned i=0;i<D;i++)
	{
		in.getline(temp,5000);
		mainNode->addWord(temp);
	};
	char* tt=new char[2];
	tt[0]='A';
	tt[1]='\0';
	for(unsigned i=0;i<N;i++)
	{
		vector<char*> temm(L+1);
		temm[0]=tt;
		unsigned current=0;
		current++;
		in.getline(temp,5000);
		char*temp2=temp;
		
		while((*temp2)!='\0')
		{
			if(temp2[0]!='(')
			{
				char* a=new char[2];
				a[0]=temp2[0];
				a[1]='\0';
				temm[current]=a;
				current++;
				temp2++;
			}
			else
			{
				temp2++;
				unsigned mmpos=0;
				while(temp2[mmpos]!=')')
					mmpos++;
				char* a=new char[mmpos+1];
				a[mmpos]='\0';
				for(unsigned i=0;i<mmpos;i++)
				{
					a[i]=temp2[i];
				}
				temm[current]=a;
				current++;
				temp2+=mmpos+1;

			}
		};
		out<<"Case #"<<i+1<<": "<<mainNode->find(temm,0)<<endl;
	}





/*
	char* data1="musta";
	char* data2="mustf";
	
	temp->addWord(data1);
	temp->addWord(data2);
	char aa[6][3]={'\0'};
	aa[0][0]='A';
	aa[1][0]='m';
	aa[2][0]='u';
	aa[3][0]='s';
	aa[4][0]='t';
	aa[5][0]='a';
	vector<char*> temp1;
	for(unsigned i=0;i<6;i++)
		temp1.push_back(aa[i]);
	cout<<temp->find(temp1,0)<<endl;
	*/
	
	return 0;

};