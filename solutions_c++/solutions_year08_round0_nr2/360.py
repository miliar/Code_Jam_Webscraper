#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int penal;
int total,T;
int A,B;
int acount,bcount,anow,bnow;
vector<pair<int,int> > Aseq,Aretseq,Bseq,Bretseq;
int a,ar,b,br;
pair<int,int> tmp,tmp2;
vector<pair<int,int> > tpta,tptb;
pair<int,int> minus(pair<int,int> inp)
{
	if (inp.second<penal)
		return make_pair(inp.first-1,inp.second+60-penal);
	else
		return make_pair(inp.first,inp.second-penal);
}
int main()
{
	freopen("C:\\test.in","r",stdin);
	freopen("C:\\test.out","w",stdout);
	scanf("%d",&total);
	T=total;
	while (total--)
	{
		scanf("%d",&penal);
		scanf("%d%d",&A,&B);
		Aseq.clear();Aretseq.clear();Bseq.clear();Bretseq.clear();
		int i,j;
		for (i=0;i<A;i++)
		{
			scanf("%d:%d",&tmp.first,&tmp.second);
			Aseq.push_back(tmp);
			scanf("%d:%d",&tmp.first,&tmp.second);
			Aretseq.push_back(tmp);
		}
		for (i=0;i<B;i++)
		{
			scanf("%d:%d",&tmp.first,&tmp.second);
			Bseq.push_back(tmp);
			scanf("%d:%d",&tmp.first,&tmp.second);
			Bretseq.push_back(tmp);
		}
		sort(Aseq.begin(),Aseq.end());
		sort(Aretseq.begin(),Aretseq.end());
		sort(Bseq.begin(),Bseq.end());
		sort(Bretseq.begin(),Bretseq.end());
		a=ar=b=br=0;
		acount=anow=bcount=bnow=0;
		for (tmp.first=0;tmp.first<24;tmp.first++)
			for (tmp.second=0;tmp.second<60;tmp.second++)
			{
				tmp2=minus(tmp);
				while ((Aretseq.size()>ar) && (Aretseq[ar]==tmp2))
				{
					bnow++;
					ar++;
				}
				while ((Bretseq.size()>br) && (Bretseq[br]==tmp2))
				{
					anow++;
					br++;
				}
				while ((Aseq.size()>a) && (Aseq[a]==tmp))
				{
					if (anow==0)
						acount++;
					else
						anow--;
					a++;
				}
				while ((Bseq.size()>b) && (Bseq[b]==tmp))
				{
					if (bnow==0)
						bcount++;
					else
						bnow--;
					b++;
				}
			}
			printf("Case #%d: %d %d\n",T-total,acount,bcount);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
