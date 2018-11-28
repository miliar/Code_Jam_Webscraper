/*Magicka*/

#include<cstdio>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main()
{
	bool found;
	char invoke[105],str[5];
	int C,D,i,j,k,l,length,listlen,N,T;
	map<string,char> combine;
	map<char,vector<char> > oppose;
	string base,str1,str2;
	vector<char> elements;
	freopen("B-large.in","rt",stdin);
	freopen("B.out","wt",stdout);
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		scanf("%d",&C);
		for(j=0;j<C;j++)
		{
			scanf("%s",str);
			base=str[0];
			base+=str[1];
			combine[base]=str[2];
			base=str[1];
			base+=str[0];
			combine[base]=str[2];
		}
		scanf("%d",&D);
		for(j=0;j<D;j++)
		{
			scanf("%s",str);
			oppose[str[0]].push_back(str[1]);
			oppose[str[1]].push_back(str[0]);
		}
		scanf("%d %s",&N,invoke);
		elements.push_back(invoke[0]);
		for(j=1;j<N;j++)
		{
			elements.push_back(invoke[j]);
			if(elements.size()==1)
			{
				if(j+1<N)
					elements.push_back(invoke[++j]);
				else
					break;
			}
			found=true;
			do
			{
				length=elements.size();
				if(length==1)
					break;
				str1=elements[length-1];
				str1+=elements[length-2];
				str2=elements[length-2];
				str2+=elements[length-1];
				if((combine.find(str1)!=combine.end()) || (combine.find(str2)!=combine.end()))
				{
					elements[length-2]=combine[str1];
					elements.erase(elements.end()-1);
				}
				else
					found=false;
			}while(found);
			vector<char> &list=oppose[elements[length-1]];
			listlen=list.size();
			length=elements.size();
			for(k=0;k<listlen;k++)
			{
				for(l=0;l<length;l++)
				{
					if(elements[l]==list[k])
					{
						elements.clear();
						length=0;
					}
				}
				if(!length)
					break;
			}
		}
		printf("Case #%d: [",i);
		length=elements.size();
		for(j=0;j<length-1;j++)
			printf("%c, ",elements[j]);
		if(length)
			printf("%c]\n",elements[length-1]);
		else
			printf("]\n");
		combine.clear();
		oppose.clear();
		elements.clear();
	}
	return 0;
}