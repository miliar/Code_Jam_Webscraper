#include<stdio.h>
#include<algorithm>
#include<functional>
int main()
{
	int T, caseNum;
	scanf("%d",&T);
	for(caseNum = 1; caseNum <= T; ++caseNum)
	{
		int N,S,p,t[100],i,j;
		scanf("%d%d%d",&N,&S,&p);
		for(i=0;i<N;++i)scanf("%d",t+i);
		int res=0;

		std::sort(t,t+N,std::greater<int>());
		for(i=0; i<N; ++i)
		{
			if((t[i]+2)/3>=p)
				++res;
			else if( S && t[i] && (t[i]+1)/3+1>=p)
				++res, --S;
			else break;
		}

		printf("Case #%d: %d", caseNum,res);

		puts("");
	}
	return 0;
}
/*

�����ĂȂ�:�ő�̃X�R�A=(���v�X�R�A+2)/3
������:�ő�X�R�A=(���v�X�R�A+1)/3+1

�ȏ�A���v�X�R�A�������������×~�ɂǂ���

case#3�����J�����ċ�����


*/
