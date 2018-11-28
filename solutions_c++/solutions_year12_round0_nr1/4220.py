#include<cstdio>
#include<cstring>

int main()
{
	int T,cnt=0,len;
	char s1[200];
	int map[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};
	scanf("%d",&T);
	gets(s1);
	while(T--) {
		gets(s1);
		len=strlen(s1);
		for(int i=0;i<len;i++)
			if(s1[i]!=' ')
				s1[i]=map[s1[i]-'a']+'a';
		printf("Case #%d: %s\n",++cnt,s1);
	}
	return 0;
}
