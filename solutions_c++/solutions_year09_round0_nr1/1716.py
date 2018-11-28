#include<vector>
#include<string>
#include<stdlib.h>
using namespace std;
struct ErdosNumber
{
	vector<string> calculateNumbers(vector<string> p)
	{
		vector<string> s;
		int a[101];
		bool l[101][101];
		int i,j,t=0,k,n;
		string tm="";
		for(i=0;i<101;i++)for(j=0;j<101;j++)l[i][j]=false;
		
		for(i=0;i<p.size();i++)
		{
			n=0;
			for(j=0;j<p[i].length();j++)
			{
				if(p[i][j]==' ')
				{
					a[n]=-1;
					for(k=0;k<t;k++)
					{
						if(s[k]==tm)a[n]=k;
					}
					if(a[n]<0)s.push_back(tm),a[n]=t++;
					n++;
					tm="";
				}
				else tm+=p[i][j];
			}
			a[n]=-1;
			for(k=0;k<t;k++)
			{
				if(s[k]==tm)a[n]=k;
			}
			if(a[n]<0)s.push_back(tm),a[n]=t++;
			n++;
			tm="";
			
			for(j=0;j<n-1;j++)
				for(k=j+1;k<n;k++)
					l[a[j]][a[k]]=true,l[a[k]][a[j]]=true;
			
		}
		
		for(i=0;i<t;i++)if(s[i]=="ERDOS")a[i]=0;else a[i]=10000;
		for(k=0;k<t;k++)
		{
			for(i=0;i<t;i++)
			{
				for(j=0;j<t;j++)
				{
					if(l[i][j] && a[i]>a[j]+1)a[i]=a[j]+1;
				}
			}
		}
		for(i=0;i<t;i++)
		{
			if(a[i]<10000)
			{
				s[i]+=' ';
				if(a[i]>=10)s[i]+=a[i]/10+'0';
				s[i]+=a[i]%10+'0';
			}
		}
		for(i=0;i<t-1;i++)
		{
            for(j=i+1;j<t;j++)
            {
                 if(s[i]>s[j])
                 {
                      tm=s[i];
                      s[i]=s[j];
                      s[j]=tm;
                 }
            }
        }
		return s;
	}
};
main()
{
      ErdosNumber a;
      vector<string> s;
      s.push_back("ERDOS A");      
      s.push_back("A B");      
      s.push_back("B AA C");
      a.calculateNumbers(s);
      return 0;
}
