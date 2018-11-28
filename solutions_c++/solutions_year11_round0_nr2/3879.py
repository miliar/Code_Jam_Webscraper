#include <cstdio>
#include <cstdlib>
#include <string>
#include <set>
#include <algorithm>
#include <map>
using namespace std;

map<string,string> atr,rep;


int main()
{
	int nt;
	scanf("%d",&nt);
	for(int kk=1;kk<=nt;kk++)
	{
		int C,R;
		scanf("%d",&C);
		char buff[4];
		atr.clear();
		rep.clear();
		for(int i=0;i<C;i++)
		{
			scanf("%s",buff);
			char n1[3];
			n1[0]=buff[0],n1[1]=buff[1],n1[2]='\0';
			if(n1[0] > n1[1])swap(n1[0],n1[1]);
			string key = n1;
			char n2[2];
			n2[0]=buff[2],n2[1]='\0';
			string val = n2;
			atr.insert(make_pair(key,val));
		}
		scanf("%d",&R);
		for(int i=0;i<R;i++)
		{
			scanf("%s",buff);
			char n1[3];
			n1[0]=buff[0],n1[1]='\0';
			string key = n1;
			char n2[2];
			n2[0]=buff[1],n2[1]='\0';
			string val = n2;
//			printf("reprlllllllll %s -> %s\n",n1,n2);
			rep.insert(make_pair(key,val));
			rep.insert(make_pair(val,key));
		}
		int NN;
		scanf("%d",&NN);
		map<char,int> stt;
		char str[128];
		scanf("%s",str);
		char out[128];
		out[0]=str[0];
		stt[str[0]]++;
		int oc=1;
		for(int i=1;i<NN;i++)
		{
			char cur = str[i];
			char curt=cur,pert;
			char prev = out[oc-1];
			pert=prev;
			char n1[3];
			if(cur > prev)swap(cur,prev);
			n1[0]=cur,n1[1]=prev,n1[2]='\0';
			string kk = n1;
			if(atr.find(kk)!=atr.end())
				kk = atr[kk];
			if(kk.length()==1)
			{
				stt[pert]--;
				out[oc-1]=kk[0];
				stt[kk[0]]++;
			}
			else
			{
				char s_S[2];
				s_S[0]=curt;
				s_S[1]='\0';
				char tt=rep[string(s_S)][0];
				if(stt[tt]==0)
				{
					out[oc++]=curt;
					stt[curt]++;
				}
				else
				{
					out[0]='\0';
					oc=0;
					stt.clear();
				}
			}
			out[oc]='\0';
//			puts(out);
		}
		out[oc]='\0';
		int ll=strlen(out);
		printf("Case #%d: [",kk);
		for(int i=0;i<oc;i++)
		{
			if(i==0)
				printf("%c",out[0]);
//			else if(i==oc-1)
//				printf(" %c",out[i]);
			else
			{
				printf(", %c",out[i]);
			}
		}
		printf("]\n");
	}
}
