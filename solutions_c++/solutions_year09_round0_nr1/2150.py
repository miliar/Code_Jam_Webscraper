#include <cstdio>

struct word{
	char w[16];
	bool match;
}dict[5010];

int main(){
	int len,ndict,nword;
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d%d%d",&len,&ndict,&nword);
	for (int i=0;i<ndict;i++)
		scanf("%s",dict[i].w);
	for (int count=1;count<=nword;count++){
		for (int p=0;p<ndict;p++)
			dict[p].match = true;
		char tmp[2000];
		int i=0;
		scanf("%s",tmp);
		for (int p=0;p<len;p++){
			char buffer[300];
			int j=0;
			if (tmp[i] == '('){
				i++;
				while (tmp[i] >= 'a' && tmp[i] <= 'z')
					buffer[j++] = tmp[i++];
				if (tmp[i] == ')') i++;
			}
			else
				buffer[j++] = tmp[i++];		
			for (int k=0;k<ndict;k++){
				if (!dict[k].match) continue;
				bool flag = false;
				for (int t=0;!flag && t<j;t++)
					flag = (dict[k].w[p] == buffer[t]);
				dict[k].match = flag;
			}
		}
		int sum = 0;
		for (int j=0;j<ndict;j++)
			sum += dict[j].match ? 1 : 0;
		printf("Case #%d: %d\n",count,sum);
	}
			

	return 0;

}