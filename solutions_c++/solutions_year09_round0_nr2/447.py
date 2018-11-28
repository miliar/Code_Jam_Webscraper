#include<iostream>
#include<string>
#include<vector>

using namespace std;


int N;

int T, H , W;

int h[100][100];
int code[100][100];

int father[10000];

int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};

char label[10000];

bool valid(int x, int y)
{
	return (x>=0 && x<H && y>=0 && y<W);
}

int getfather(int x)
{
	if (x == father[x]) return x;
	else return father[x] = getfather(father[x]);
}

void Union(int f_id, int son_id)
{
    father[son_id]=getfather(f_id);
}

int main()
{
   cin >> T;

for (int cc = 0;cc<T;cc++)
{
	cin >>H >>W; 
	for (int i = 0;i<H;i++)for (int j = 0;j<W;j++) 
	{
			cin >> h[i][j];
			code[i][j] = i*W + j;
	}
	for (int i = 0;i<W*H;i++) father[i] = i;
for (int i = 0;i<H;i++)for (int j = 0;j<W;j++) 
{
			int min = h[i][j]; int f_i = -1;
	for (int d = 0;d<4;d++)
	{

		int ii = i + dx[d]; int jj = j + dy[d];
		if (valid(ii,jj))
			if (h[ii][jj] < min) { min = h[ii][jj]; f_i = code[ii][jj];}

	}
			if (f_i !=-1) Union(f_i, code[i][j]);
}
if(false)
for (int i = 0;i<H;i++)
{
	for (int j = 0;j<W;j++) 
		printf(" %d", father[ code[i][j]]);
	printf("\n");
}

char codec = 'a';
memset(label,0,sizeof(label));
for (int i = 0;i<H;i++)for (int j = 0;j<W;j++) 
if (label[ code[i][j] ] == 0)
{
	int y  = getfather(code[i][j]);
	if (label[y] == 0) { label[code[i][j]] =  label[y] = codec++;}
	else label[code[i][j]]= label[y];
}
	printf("Case #%d:\n", cc+1); 
for (int i = 0;i<H;i++)
{
	printf("%c",label[code[i][0]]);
	for (int j = 1;j<W;j++) printf(" %c",label[code[i][j]]);
		printf("\n");
}

}
}