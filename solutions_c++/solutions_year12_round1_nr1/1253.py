#include <stdio.h>
//#define MAX 4//С����
#define MAX 100000//С����

double p[MAX];
 int main()
 {
	 freopen("C:\\A-large.in", "r", stdin);
	 freopen("C:\\1_large.out", "w", stdout);
	 int i,j,k, A, B,T, cases=0;
	 double expected, min, pp;
	 scanf("%d", &T);
	 while (++cases <= T)
	 {
		 scanf("%d%d", &A, &B);
			for(i=0; i<A; i++)	
			 scanf("%lf", &p[i]);
		//min = A+B+10;
		pp = 1;
		//����typing(����)
		j = 0;
		while(j<A)
			pp *= p[j++];
		min = pp*(B-A+1)+(1-pp)*(B-A+1+B+1);
		//ֱ�ӻس��϶���A<B
		expected = 1+B+1;
		if(min > expected)
			min = expected;
		
		pp = 1;
		for (j=0; j<A-1; j++)//��A-j-1�񣬻���j+1��(��ȫ��������)//����???
		{
			k = A-j-1;
			pp *= p[j];
			expected = pp*(B-(j+1)+1)+(1-pp)*(B-(j+1)+1+B+1);//�Ż�
			if(min > expected+k)
				min = expected+k;
		}
		if(min > A+B+1)//��ȫ
			min = A+B+1;
		 printf("Case #%d: %.6lf\n", cases, min);
	 }
	 return 0;
 }