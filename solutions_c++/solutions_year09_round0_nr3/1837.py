

#include <iostream>
#include <vector>
#include <map>
#include <set>

#include <string>

using namespace std;
#define for if(true)for
struct LDN_Cal
{

	map<char, struct LDN_Cal*>m_dic;
	void refine(const char *pCh, const int &len)
	{
		if(len<1)
		{
			return;
		}
		if(m_dic.find(pCh[0])==m_dic.end())
		{
			m_dic[pCh[0]]=new LDN_Cal;
		}
		 m_dic[pCh[0]]->refine(&(pCh[1]), len-1);
	}
	int find(const char *pCh, const int &len)
	{
		if(0==len)
		{
			return 1;
		}
		vector<LDN_Cal*>localcal;
		if(pCh[0]=='(')
		{
			int i=1;
			while(pCh[i]!=')')
			{
				map<char, LDN_Cal*>::iterator it = m_dic.find(pCh[i]);
				++i;
				if(it==m_dic.end())
				{
					continue;
				}	
				localcal.push_back(it->second);
			}
			++i;
			int n = 0;
			for(int j=0;j<localcal.size();++j)
			{
				n+=localcal[j]->find(&(pCh[i]), len -i);
			}
			return n;
		}

		map<char, LDN_Cal*>::iterator it = m_dic.find(pCh[0]);
		if(it==m_dic.end())
		{
			return 0;
		}
		
		return it->second->find(&(pCh[1]), len-1);

	}

};
	const char * g_welcometocodejam="welcome to code jam";
	int g_len =19;
struct welcometocodejam
{
	static int find(int cur, const char*pch, int len)
	{
		if(cur ==19)
		{
			return 1;
		}
		if(len<19-cur)
		{
			return 0;
		}
		int n=0;
		for(int i=0;i<len;++i)
		{
			if(g_welcometocodejam[cur] == pch[i])
			{
				n+=find(cur+1, &pch[i+1],len-i-1);
			}
		}
		return n;
	}
};
#include <stdlib.h>
int main()
{
	
	int num=0;
	FILE* pfile1 = fopen("test2.txt","r");
	FILE* pfile2 = fopen("result2.txt","w");
	fscanf(pfile1,"%d",&num);
	cout<<num<<endl;
	char inch[1000]="";
	fgets(inch, 1000,pfile1);
	for(int i=0;i<num;++i)
	{
		fgets(inch, 1000,pfile1);
		int n = welcometocodejam::find(0, inch, strlen(inch));
		//cout<<inch<<"Case #%d: %d\n"<<i+1<< n<<endl;
		fprintf(pfile2,"Case #%d: %04d\n",i+1, n);
	}
		fclose(pfile1);
	fclose(pfile2);
	return 0;
	    FILE* m_pfile = fopen("test.txt","r");
	LDN_Cal rootset;
	int l,d,n;
	cout<<"scanf l d n"<<endl;
	fscanf(m_pfile,"%d %d %d",&l,&d,&n);
	if(l<1 || l>15)
	{
		printf("l is %d\n",l);
		return 0;
	}

	if(d<1 || d>5000)
	{
		printf("d is %d\n",d);
		return 0;
	}
	if(n<1 || n>500)
	{
		printf("n is %d\n",n);
		return 0;
	}
	char pTmp[24]={0};
	cout<<"scanf "<<d<<" pTmp "<<endl;
	for(int i=0;i<d;++i)
	{
		fscanf(m_pfile,"%s", pTmp);
		rootset.refine(pTmp,l);
	}
vector<int>ret;
ret.resize(n);
char tmp[1024];
	for(int i=0;i<n;++i)
	{
		fscanf(m_pfile,"%s", tmp);
		int len = strlen(tmp);
		ret[i]=rootset.find(tmp, len);

	}
		    FILE* pfile = fopen("result.txt","w");

	for(int i=0;i<n;++i)
	{
		fprintf(pfile,"Case #%d: %d\n",i+1, ret[i]);

	}
	fclose(m_pfile);
	fclose(pfile);
    return 0;


}


