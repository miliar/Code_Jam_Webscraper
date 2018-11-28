#include <stdio.h>
#include <string.h>

int check1(char** arr, int i, int j, char c, int K, int N)
{
	if (j<K-1) return 0;
	for (int l=j;l>j-K;l--)
		if (arr[i][l] != c)
			return 0;
	return 1;
}

int check2(char** arr, int i, int j, char c, int K, int N)
{
	if (j<K-1) return 0;
	if (i<K-1) return 0;

	for (int l=0;l<K;l++)
		if (arr[i-l][j-l] != c)
			return 0;
	return 1;
}

int check3(char** arr, int i, int j, char c, int K, int N)
{
	if (i<K-1) return 0;

	for (int l=0;l<K;l++)
		if (arr[i-l][j] != c)
			return 0;
	return 1;
}
int check4(char** arr, int i, int j, char c, int K, int N)
{
	if (j+K>N) return 0;
	if (i<K-1) return 0;

	for (int l=0;l<K;l++)
		if (arr[i-l][j+l] != c)
			return 0;
	return 1;
}

int check5(char** arr, int i, int j, char c, int K, int N)
{
	if (j+K>N) return 0;
	for (int l=j;l<j+K;l++)
		if (arr[i][l] != c)
			return 0;
	return 1;
}
int check6(char** arr, int i, int j, char c, int K, int N)
{
	if (j+K>N) return 0;
	if (i+K>N) return 0;

	for (int l=0;l<K;l++)
		if (arr[i+l][j+l] != c)
			return 0;
	return 1;
}
int check7(char** arr, int i, int j, char c, int K, int N)
{
	if (i+K>N) return 0;

	for (int l=0;l<K;l++)
		if (arr[i+l][j] != c)
			return 0;
	return 1;
}
int check8(char** arr, int i, int j, char c, int K, int N)
{
	if (j<K-1) return 0;
	if (i+K>N) return 0;

	for (int l=0;l<K;l++)
		if (arr[i+l][j-l] != c)
			return 0;
	return 1;
}

void print_arr(char** arr, int N)
{
	for (int i=0;i<N;i++) {
		for (int j=0;j<N;j++) {
			printf("%c", arr[i][j]);
		}
		printf("\n");
	}
}

void func(int ccc)
{
	int N, K;

	scanf("%d %d\n", &N, &K);
	//printf("%d %d\n", N, K);

	// init array
	char** arr = new char*[N];
	for (int i=0;i<N;i++)
		arr[i] = new char[N];

	for (int i=0;i<N;i++) {
		for (int j=0;j<N;j++) {
			scanf("%c", arr[i]+j);
		}
		char t;
		scanf("%c", &t);
	}

	for (int i=0;i<N;i++) {
		int index = N-1;
		for (int j=N-1;j>=0;j--) {
			while (index>=0) {
				if (arr[i][index] == '.')
					index--;
				else
					break;
			}

			if (index<0) break;

			if (index!=j) {
				arr[i][j] = arr[i][index];
				arr[i][index] = '.';
			}else
				index--;
		}
	}

	//print_arr(arr, N);

	int r_checked = 0;
	int b_checked = 0;

	for (int i=0;i<N;i++)
		for (int j=0;j<N;j++)
			if (arr[i][j]!='.') {
				if (!r_checked && arr[i][j]=='R'){
					if (check1(arr,i,j,'R', K, N) ||
					check2(arr,i,j,'R', K, N) ||
					check3(arr,i,j,'R', K, N)||
					check4(arr,i,j,'R', K, N)||
					check5(arr,i,j,'R', K, N)||
					check6(arr,i,j,'R', K, N)||
					check7(arr,i,j,'R', K, N)||
					check8(arr,i,j,'R', K, N))
						r_checked = 1;
				}else if (!b_checked && arr[i][j]=='B') {
					if (check1(arr,i,j,'B', K, N) ||
					check2(arr,i,j,'B', K, N) ||
					check3(arr,i,j,'B', K, N)||
					check4(arr,i,j,'B', K, N)||
					check5(arr,i,j,'B', K, N)||
					check6(arr,i,j,'B', K, N)||
					check7(arr,i,j,'B', K, N)||
					check8(arr,i,j,'B', K, N))
						b_checked = 1;
				}
			}

	if (b_checked && r_checked) 
		printf("Case #%d: Both\n", ccc+1);
	else if (b_checked)
		printf("Case #%d: Blue\n", ccc+1);
	else if (r_checked)
		printf("Case #%d: Red\n", ccc+1);
	else
		printf("Case #%d: Neither\n", ccc+1);

	for (int i=0;i<N;i++)
		delete [] arr[i];
	delete arr;

}

int main()
{
	int T;
	scanf("%d\n", &T);
	//printf("%d\n", T);
	for (int i=0;i<T;i++)
		func(i);
	return 0;
}
