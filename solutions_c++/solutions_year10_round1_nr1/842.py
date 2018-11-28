#include <stdio.h>

bool line(char tmp[51][51],int n,int k,int i,int j)
{
	char c = tmp[i][j];
	if(c == '.') return false;

	int p = 1;
	for(;j + p < n && tmp[i][j+p] == c;++p);
	int q = 1;
	for(;q <= j && tmp[i][j-q] == c;++q);
	if(p+q-1 >= k) return true;

	p = 1;
	for(;i + p < n && tmp[i+p][j] == c;++p);
	q = 1;
	for(;q <= i && tmp[i-q][j] == c;++q);
	if(p+q-1 >= k) return true;

	p = 1;
	for(;j + p < n && i + p < n && tmp[i+p][j+p] == c;++p);
	q = 1;
	for(;q <= j && q <= i && tmp[i-q][j-q] == c;++q);
	if(p+q-1 >= k) return true;


	p = 1;
	for(;p <= i && j + p < n && tmp[i-p][j+p] == c;++p);
	q = 1;
	for(;i + q < n && q <= j && tmp[i+q][j-q] == c;++q);
	if(p+q-1 >= k) return true;
	return false;
}

int main()
{
	int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		int n = 0,k = 0;
		scanf("%d%d",&n,&k);
		char board[51][51];
		for(int i = 0;i < n;++i) scanf("%s",board[i]);
	//	printf("\n");
		char tmp[51][51] = { 0 };
		for(int i = 0;i < n;++i)
		{
			for(int j = 0;j < n;++j)
			{
				tmp[i][j] = board[n-1-j][i];
			}
			//printf("%s\n",tmp[i]);
		}
		//printf("\n");
		for(int i = 0;i < n;++i)
		{
			for(int p = n - 2;p >= 0;--p)
			{
				int j = p + 1;
				for(;j < n && tmp[j][i] == '.';++j);
				if(j == p + 1) continue;
				--j;
				tmp[j][i] = tmp[p][i];
				tmp[p][i] = '.';
			}
		}
		//for(int i = 0;i < n;++i) printf("%s\n",tmp[i]);
		int ret = 0;
		for(int i = 0;i < n;++i)
		{
			for(int j = 0;j < n;++j)
			{
				bool res = line(tmp,n,k,i,j);
				if(!res) continue;
				if('R' == tmp[i][j]) ret |= 1;
				else if('B' == tmp[i][j]) ret |= 2;
			}
		}

		//int ret = 0;
		//int rcount = 0,bcount = 0;
		//for(int i = 0;i < n;++i)
		//{
		//	rcount = 0;bcount = 0;
		//	for(int j = 0;j < n;++j)
		//	{
		//		char c = tmp[i][j];
		//		if(c == 'R') { rcount++;bcount = 0; }
		//		else if('B' == c) { bcount++;rcount = 0; }
		//		if(rcount >= k) ret |= 1;
		//		if(bcount >= k) ret |= 2;
		//	}


		//	rcount = 0;bcount = 0;
		//	for(int j = 0;j < n;++j)
		//	{
		//		char c = tmp[j][i];
		//		if(c == 'R') { rcount++;bcount = 0; }
		//		else if('B' == c) { bcount++;rcount = 0; }
		//		if(rcount >= k) ret |= 1;
		//		if(bcount >= k) ret |= 2;
		//	}
		//}
		//for(int i = 0;i < n;++i)
		//{

		//	rcount = 0;bcount = 0;
		//	for(int j = 0;i + j < n;++j)
		//	{
		//		char c = tmp[j][i+j];
		//		if(c == 'R') { rcount++;bcount = 0; }
		//		else if('B' == c) { bcount++;rcount = 0; }
		//		if(rcount >= k) ret |= 1;
		//		if(bcount >= k) ret |= 2;
		//	}

		//	rcount = 0;bcount = 0;
		//	for(int j = 0;i + j< n;++j)
		//	{
		//		char c = tmp[i+j][j];
		//		if(c == 'R') { rcount++;bcount = 0; }
		//		else if('B' == c) { bcount++;rcount = 0; }
		//		if(rcount >= k) ret |= 1;
		//		if(bcount >= k) ret |= 2;
		//	}
		//}
		printf("Case #%d: ",iCases);
		if(0 == ret) printf("Neither\n");
		else if(1 == ret) printf("Red\n");
		else if(2 == ret) printf("Blue\n");
		else printf("Both\n");
	}
	return 0;
}