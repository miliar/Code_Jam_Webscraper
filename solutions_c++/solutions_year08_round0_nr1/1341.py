#include <iostream>
#include <map>
#include <string>

using namespace std;

int findzero(map<string,int> search);
//void setzero(map<string,int> search);

int main()
{
	//freopen("A-small.in","r",stdin);
	//freopen("res.txt","w",stdout);
	int n, s, q, total,casenum=0, temp;
	string *sname;
	char sername[100];
	map<string,int> search;
	map<string,int>::iterator ite1;
	cin>>n;
	
	while( n-- > 0)
	{
		total=0;
		casenum++;
		search.clear();
		cin>>s;
		temp=s;
		gets(sername);
		while(s-- > 0)
		{
			gets(sername);
			sname=new string(sername);
			search.insert(map<string,int>::value_type(*sname,0));
			delete sname;
		}
		
		cin>>q;
		if(q<temp)
		{
			cout<<"Case #"<<casenum<<": 0"<<endl;
			continue;
		}
		gets(sername);
		while(q-- >0)
		{
			gets(sername);
			sname=new string(sername);
			//cout<<++search[*sname]<<' ';
			++search[*sname];
			if( findzero(search) )
			{
				++total;
				for(ite1=search.begin(); ite1!=search.end(); ite1++)
				{
					ite1->second = 0;
				}
				++search[*sname];
			}
			delete sname;
		}
		cout<<"Case #"<<casenum<<": "<<total<<endl;
	}

	return 0;
}
int findzero(map<string,int> search)
{
	map<string,int>::iterator ite1;
	for(ite1=search.begin(); ite1!=search.end(); ite1++)
	{
		if(ite1->second == 0)
			break;
	}
	if( ite1==search.end() )
		return 1;
	else
		return 0;
}

void setzero(map<string,int> search)
{
	map<string,int>::iterator ite1;
	for(ite1=search.begin(); ite1!=search.end(); ite1++)
	{
		ite1->second = 0;
	}
}
