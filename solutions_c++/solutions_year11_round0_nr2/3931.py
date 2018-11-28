// MagicKa.cpp : 定义控制台应用程序的入口点。
#include<iostream>
#include<fstream>
using namespace std;
struct print
{
	int mlen;
	char output[100];
};
struct form
{
	char base1;
	char base2;
	char ele;
};
struct oppose
{
	char oppo1;
	char oppo2;
};

int InOppo(char a,oppose *moppo,int n)
{
	for(int i=0;i<n;i++)
	{
		if(moppo[i].oppo1==a)
			return i;
		else if(moppo[i].oppo2==a)
			return i;
	}
	return -1;
}
int InForm(char a,form *mform,int n)
{
	for(int i=0;i<n;i++)
	{
		if(mform[i].base1==a)
			return i;
		else if(mform[i].base2==a)
			return i;
	}
	return -1;
}
bool IsOppo(char a,char b,oppose* moppo,int n)
{
	int num=InOppo(a,moppo,n);
	if(num!=-1)
	{
		if(a==moppo[num].oppo1)
		{
			if(b==moppo[num].oppo2)
				return true;
		}
		else if(b==moppo[num].oppo1)
			return true;
		return false;
	}
	return false;
}
char IsForm(char x,char y,form *mform,int n)
{
	int num=InForm(x,mform,n);
	if(num!=-1)
	{
		if(mform[num].base1==x)
		{
			if(mform[num].base2==y)
				return mform[num].ele;
		}
		else if(mform[num].base1==y)
			return mform[num].ele;
		return 'a';
	}
	return 'a';
}
form mform[36];
oppose moppo[28];
int main()
{
	ifstream cin("B-small-attempt3.in");
	int T,C,D,N;
	cin>>T;
	int i,j,k;
	print mprint[100];
	for(i=0;i<T;i++)
	{
		mprint[i].mlen=0;
		cin>>C;
		if(C!=0)
		{
			for(j=0;j<C;j++)
				cin>>mform[j].base1>>mform[j].base2>>mform[j].ele;
		}
		cin>>D;
		if(D!=0)
		{
			for(j=0;j<D;j++)
				cin>>moppo[j].oppo1>>moppo[j].oppo2;
		}
		cin>>N;
		char *p3=new char[N];
		for(j=0;j<N;j++)
			cin>>p3[j];
		for(j=0;j<N;j++)
		{
			if(j==0)
			{
				mprint[i].output[j]=p3[j];
				mprint[i].mlen++;
			}
			else
			{
				char mch=IsForm(p3[j],mprint[i].output[mprint[i].mlen-1],mform,C);
				if(mch!='a')  //可以炼制
				{
					mprint[i].output[mprint[i].mlen-1]=mch;// 继续炼制
					while(mprint[i].mlen>=2)
					{
						mch=IsForm(mprint[i].output[mprint[i].mlen-1],mprint[i].output[mprint[i].mlen-2],mform,C);
						if(mch!='a')
						{
							mprint[i].mlen--;
							mprint[i].output[mprint[i].mlen-1]=mch;
						}
						else
							break;
					}
				}
				else //不能炼制
				{
					for(k=0;k<mprint[i].mlen;k++)
					{
						if(IsOppo(p3[j],mprint[i].output[k],moppo,D)) //相反
							break;
					}
					if(k!=mprint[i].mlen)
					{
						mprint[i].mlen=0;
					}
					else
					{
						mprint[i].output[mprint[i].mlen]=p3[j];
						mprint[i].mlen++;
					}
				}
			}
		}
	}
	/*for(i=0;i<T;i++)
	{
		cout<<"Case #"<<i+1<<": [";
		for(k=0;k<mprint[i].mlen;k++)
		{
			if(k==mprint[i].mlen-1)
				cout<<mprint[i].output[k];
			else
				cout<<mprint[i].output[k]<<",";
		}
		cout<<"]"<<endl;
	}*/

	ofstream fout;
	fout.open("b.txt");
	for(i=0;i<T;i++)
	{
		fout<<"Case #"<<i+1<<": [";
		for(k=0;k<mprint[i].mlen;k++)
		{
			if(k==mprint[i].mlen-1)
				fout<<mprint[i].output[k];
			else
				fout<<mprint[i].output[k]<<", ";
		}
		fout<<"]"<<endl;
	}
	return 0;
}
		
		
