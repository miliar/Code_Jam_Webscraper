#include <stdio.h>

int main()
{
	FILE* fp=fopen("input.in","r"),*fp2=fopen("output.out","w");
	__int64 n,l,p,c,i,j,k;

	fscanf(fp,"%I64d",&n);

	for (i=1; i<=n; i++)
	{
		fscanf(fp,"%I64d%I64d%I64d",&l,&p,&c);

		j=0,k=0;

		do j++; while ((l=l*c)<p);

		// �̷��� j���� ���ڰ� ������?
		// ���� ��� 10, 1 ��.
		j=j*2-1;

		while (j>>=1) k++;

		fprintf(fp2,"Case #%I64d: %I64d\n",i,k);
	}
	return 0;
}