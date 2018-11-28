#include<iostream>
#include<string>
#include<vector>
#include<stack>
using namespace std;

struct node{
	char datas[4];
};
int C,D,N;
vector<node> cVec,dVec;

char myFind(char chA,char chB)
{
	for(int i=0;i<C;++i)
	{
		if((cVec[i].datas[0]==chA&&cVec[i].datas[1]==chB)||(cVec[i].datas[0]==chB&&cVec[i].datas[1]==chA))
		{
			return cVec[i].datas[2];
		}
	}
	return '?';
}

void pushCh(stack<char> &stk,char tmpCh)
{
	char tmpCharA;
	if(!stk.empty())
	{
		tmpCharA=stk.top();
		char tmpCharB=myFind(tmpCharA,tmpCh);
		if(tmpCharB=='?')
		{
			//over here
			stk.push(tmpCh);
		}
		else
		{
			stk.pop();
			pushCh(stk,tmpCharB);
		}
	}
	else
	{
		stk.push(tmpCh);
	}
}

string combineData(string strIn)
{
	stack<char> tmpStk;
	int len=strIn.size();
	for(int i=0;i<len;++i)
	{
		if(!tmpStk.empty())
		{
			char tmpCh=tmpStk.top();
			char tmpRes=myFind(strIn[i],tmpCh);
			if(tmpRes=='?')//未能匹配
			{
				tmpStk.push(strIn[i]);
			}
			else
			{
				tmpStk.pop();
				pushCh(tmpStk,tmpRes);
			}
		}
		else
		{
			tmpStk.push(strIn[i]);
		}
	}
	string ansStr;
	stack<char> tmpStk2;
	while(!tmpStk.empty())
	{
		tmpStk2.push(tmpStk.top());
		tmpStk.pop();
	}
	while(!tmpStk2.empty())
	{
		ansStr.push_back(tmpStk2.top());
		tmpStk2.pop();
	}
	return ansStr;
}

struct myPair{
	char ch;
	int i;
	int pos;
	myPair(char ch,int i,int pos)
	{
		this->ch=ch;
		this->i=i;
		this->pos=pos;
	}
};

vector<myPair> opposeMark;
int deFind(char chAim)
{
	int len=opposeMark.size();
	for(int i=0;i<len;++i)
	{
		if(opposeMark[i].ch==chAim)
			return i;
	}
	return -1;
}

myPair add2Mark(char ch)
{
	int len=dVec.size();
	for(int i=0;i<len;++i)
	{
		if(ch==dVec[i].datas[0])
		{
			return myPair(dVec[i].datas[1],1,i);
			//return dVec[i].datas[1];
		}
		if(ch==dVec[i].datas[1])
		{
			return myPair(dVec[i].datas[0],0,i);
			//return dVec[i].datas[0];
		}
	}
	return myPair('?',-1,-1);
}

void shrinkDatas(stack<char> & stk,char chAim)
{
	while(!stk.empty())
	{
		stk.pop();
	}
}
string destroyData(string strIn)
{
	string ans=strIn;
	int len=ans.size();
	stack<char> tmpStk;
	for(int i=0;i<len;++i)
	{
		myPair tmpCh=add2Mark(ans[i]);
		if(tmpCh.ch=='?')
		{
		}
		else
		{
			opposeMark.push_back(tmpCh);//opposeMark中记录那些需要注意的数据
		}
		int ansIndex=deFind(ans[i]);
		if(ansIndex!=-1)	//若找到需要处理的对象,则ans[i]不入栈
		{
			if(opposeMark[ansIndex].i==1)
			{
				shrinkDatas(tmpStk,dVec[opposeMark[ansIndex].pos].datas[0]);
			}
			else
			{
				shrinkDatas(tmpStk,dVec[opposeMark[ansIndex].pos].datas[1]);
			}
		}
		else
		{
			tmpStk.push(ans[i]);
		}
	}
	string ansStr;
	stack<char> stk2;
	while(!tmpStk.empty())
	{
		stk2.push(tmpStk.top());
		tmpStk.pop();
	}
	while(!stk2.empty())
	{
		ansStr.push_back(stk2.top());
		stk2.pop();
	}
	return ansStr;
}

int main()
{
	int t;
	cin>>t;
	string strDatain;
	string combinedStr;
	for(int i=1;i<=t;++i)
	{
		cVec.clear();
		dVec.clear();
		cin>>C;
		for(int j=0;j<C;++j)
		{
			node tmp;
			cin>>tmp.datas;
			cVec.push_back(tmp);
		}
		cin>>D;
		for(int j=0;j<D;++j)
		{
			node tmp;
			cin>>tmp.datas;
			dVec.push_back(tmp);
		}
		cin>>N;
		cin>>strDatain;
		///////////////////
		string strTmp;
		string ansStr;
		for(int d=0;d<N;++d)
		{
			opposeMark.clear();
			strTmp.push_back(strDatain[d]);
			combinedStr=combineData(strTmp);
			strTmp=destroyData(combinedStr);
		}
		printf("Case #%d: [",i);
		if(strTmp.size()!=0)
		{
			for(int t=0;t<strTmp.size()-1;++t)
			{
				cout<<strTmp[t]<<", ";
			}
			cout<<strTmp[strTmp.size()-1]<<"]"<<endl;
		}
		else
			cout<<"]"<<endl;
	}
	return 0;
}