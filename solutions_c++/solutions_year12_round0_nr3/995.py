#include<stdio.h>
#include<string.h>
int Digit(int x)
{
	int res=0;
	while(x)
	{
		x/=10;
		++res;
	}
	return res;
}
int main()
{
	int T, caseNum;
	scanf("%d",&T);
	static long long digit[20]={1,1};
	int i,j,k;
	for(i=2; i<20;++i)
		digit[i]=digit[i-1]*10;
	for(caseNum = 1; caseNum <= T; ++caseNum)
	{
		static int memo[10000001];

		memset(memo,-1,sizeof(memo));
		int A,B;
		scanf("%d%d",&A,&B);
		int n=Digit(A);
		int res=0;
		for(int i=A; i<=B; ++i)
		{
			if(memo[i]>=0)
				continue;
			int next=i;
			int t=1;
			memo[next]=1;
			for(j=1;j<n;++j)
			{
				int t1 = next/digit[n];
				next = (next*10+t1)%digit[n+1];
				if(A<=next && next<=B && memo[next]<0)
					++t;
				memo[next]=1;
			}
			res+=t*(t-1)/2;
		}
		printf("Case #%d: %d\n", caseNum,res);
	}
	return 0;
}
/*

Small�͑�������ŗ]�T�����ǁA
Large�͕�����Ȃ�g��Ȃ��Ǝ��˂�

�ŁA������Ƃ���Ȃ�H
n���̐�������]�����Ăł��鐔����n�A
���̂����A���鐔X�ȉ��ł���Ɣ��肷��ɂ́E�E�E


�E�E�ESmall��@���邩�E�E�E


�E�E�E���鐔n�����[�e�V�������Ăł��鐔�S��(n�܂�)����x�ł���Ƃ��A
x�̂͂��ׂāA���[�e�V�������邱�Ƃ�n���m�ۂł���A���Ȃ킿n�̌��ʂ��ŗ��p����΂悢
�E�E�E���������Ă����Ίy���H
�Ƃ������An�̃��[�e�V������A�ȏ�B�ȉ��ɂ�����̂�x����Ȃ�A���̃��e�[�V�������S����xC2=(x*(x-1))/2����Ȃ��́H


*/
