
#include <stdio.h>
#include <stdlib.h>

#include <vector>
#include <algorithm>

using namespace std;

static vector<string> words;
static int sort_index[15][5000];
static vector<char> g_flags;

int Search(int D, char *s, int L)
{
	int l = 0, pos = 0;

	vector<char> flags = g_flags;

	for( ; l<L; l++)
	{
		if (s[pos]==0)
		{
			printf("bad pattern at %d chars", l);
			return -1;//bad pattern
		}

		vector<char> chars;
		if (s[pos]!='(')//固定字符, 只有一个选择
		{
			chars.push_back(s[pos]);
			pos++;
		}
		else
		{
			if (s[pos]==0)
			{
				printf("partten ')' not match at %D chars\n", l);
				return -1;
			}
			pos++;//跳过'('

			while(s[pos]!=0 && s[pos]!=')')
			{
				chars.push_back(s[pos]);
				pos++;
			}
			if (s[pos]==0)
			{
				printf("partten ')' not match at %D chars\n", l);
				return -1;
			}
			pos++;//跳过')'
		}

		sort(chars.begin(), chars.end());//模式字符排序

		int p_pos = 0;
		bool has_item = false;
		int i;
		for (i=0; i<D && p_pos < chars.size(); )
		{
			int k = sort_index[l][i];
			if (flags[k] )
			{
				char c= words[k][l];
				if ( c<chars[p_pos])
				{
					flags[k] = 0;
					i++;
				}
				else if (c==chars[p_pos])
				{
					i++;
					has_item = true;
				}
				else //c>chars[p_pos]
					p_pos++;
			}
			else
				i++;
		}
		if (!has_item)
			return 0;//已经没有词在备选项中了

		//剩余的词均设为无效
		for(; i<D; i++)
			flags[sort_index[l][i]] = 0;
	}

	int count = 0;
	for(int i=0; i<D; i++)
		count += flags[i];

	return count;
}

bool patten(FILE *in, FILE *out)
{

	char s[1024];
	int count;
	int L, D, N;
	fscanf(in, "%d%d%d", &L, &D, &N);
	if (L<1 || L> 15)
	{
		printf("Bad L\n");
		return false;
	}

	if (D<1 || D> 5000)
	{
		printf("Bad D\n");
		return false;
	}

	if (N<1 || N> 500)
	{
		printf("Bad N\n");
		return false;
	}

	//sort_index.resize(D);
	words.resize(D);
	g_flags.resize(D);
	for(int i=0; i<D; i++)
	{
		fscanf(in, "%s", s);
		words[i] =  s;
		for(int j=0; j< L; j++)
			sort_index[j][i] = i;
		g_flags[i] = 1;
	}


	//给词典按每个字母排序建立索引表在sort_index
	for(int l = 0; l<L; l++)//每个字母
	{
		for (int i=0; i<D-1; i++)//冒泡排序
		{
			for(int j=i+1; j<D; j++)
			{
				char c1 = words[sort_index[l][i]][l];
				char c2 = words[sort_index[l][j]][l];
				if ( c1>c2 )
				{
					int tmp = sort_index[l][i];
					sort_index[l][i] =  sort_index[l][j];
					sort_index[l][j] = tmp;
				}
			}
		}
	}

	//对每个case进行匹配,输出结果
	for(int i=0; i<N; i++)
	{
		fscanf(in, "%s", s);
		count = Search(D, s, L);
		if (count<0)
		{
			printf("failed\n");
			return false;
		}
		fprintf(out, "Case #%d: %d\n", i+1, count);
	}

	return true;
}

void usage()
{
	printf("jam0 in_file out_file\n");
}


int main(int argc, char *argv[])
{

	if (argc!=3)
	{
		printf("Bad parmater\n");
		usage();
		goto failed;
	}

	FILE *in, *out;
	in = fopen(argv[1], "rb");
	if (in==NULL )
	{
		printf("Can not open input file %s", argv[1]);
		goto failed;
	}
	out = fopen(argv[2], "w");
	if (out == NULL)
	{
		printf("Can not open out file %s", argv[2]);
		goto failed;
	}

	if (!patten(in, out))
		printf("Failed\n");
	else
		printf("OK\n");

	fclose(in);
	fclose(out);

failed:
	printf("any key exit...\n");
	getchar();
	return 1;
}
